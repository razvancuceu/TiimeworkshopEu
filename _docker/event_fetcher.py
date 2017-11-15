# fetch attendee list from eventbrite and insertit into a markdown template

import csv
import json
import logging
import os
import requests
import sys
import time


class EventFetcher:
    def __init__(self):
       # READ IN OAUTH2 TOKEN
        api_key_dir = os.path.expanduser('~')
        oauth2_token = os.path.join(api_key_dir, 'EVENTBRITE_PERSONAL_OAUTH2_TOKEN')
        with open(oauth2_token, 'r') as f:
            self.oauth_token = f.readline().rstrip()
        with open(os.path.join(os.path.dirname(__file__), 'registration.template')) as f:
            self.template = f.read()

        self.endpoint = "https://www.eventbriteapi.com"
        self.api_version = "v3"

    def get_resource(self, resource):
        uri = "{}/{}/{}".format(self.endpoint, self.api_version, resource)
        headers  = { "Authorization": "Bearer {}".format(self.oauth_token)}
        logging.debug(uri)
        return requests.get(uri,
                            headers = headers,
                            verify = True,  # Verify SSL certificate
                        )
        
    def fetch_events(self):
        resource = "users/me/owned_events"
        response = self.get_resource(resource)
        return response.json()['events']

    def fetch_attendees(self, event_id):
        attendee_list = []   # each list item is a Eventbrite attendee object
        page = 1
        count = 0
        while True:
            resource = "events/{}/attendees/?status=attending&page={}".format(event_id, page)
            response = self.get_resource(resource).json()
            if 'error' in response:
                print(response['error'] + ': ' + response['error_description'] + ', resource: ' + resource, file=sys.stderr)
                sys.exit(1)
            # Check the pages
            if 'pagination' in response:
                logging.debug(response['pagination'])
                if page < response['pagination']['page_count']:
                    attendee_list += response['attendees']
                    count += len(response['attendees'])
                    page += 1
                    time.sleep(1)
                else:
                    attendee_list += response['attendees']
                    count += len(response['attendees'])
                    break
            else:
                attendee_list += response['attendees']
                count += len(response['attendees'])
                break


        logging.info('received {} attendees (status = attending)'.format(count))
        return attendee_list

    def get_country(self, addresses):
        try:
            return addresses['work']['country']
            return addresses['bill']['country']
            return addresses['home']['country']
            return addresses['ship']['country']
        except KeyError:
            return ''

    def reformat_attendees(self, attendee_list):
        markdown_doc = self.template
        # make a dictionary of the attendees
        attendees = {}
        for attendee in attendee_list:
            name = last_name = company = country = ""
            if 'last_name' in attendee['profile']:
                last_name = attendee['profile']['last_name']
                if last_name == 'Hörbe':
                    continue
            if 'name' in attendee['profile']:
                name = attendee['profile']['name']
                name = name.replace(last_name, '')
            if 'company' in attendee['profile']:
                company = attendee['profile']['company']
            attendees[last_name + name + company] = [last_name, name, company,
                                                     self.get_country(
                                                         attendee['profile']['addresses'])]
            # logging-debug('%' + ', '.join(attendees[last_name+name+company]), file=sys.stderr)

        for key in sorted(attendees, key=lambda s: s.lower()):
            markdown_doc += "|{}|{}|{}|{}|\n".format(attendees[key][0],
                                                     attendees[key][1],
                                                     attendees[key][2],
                                                     attendees[key][3])

        return markdown_doc

    def make_dict_by_email(self, attendee_list):
        # make a dict of the attendees
        email_dict = {}
        for attendee in attendee_list:
            name = last_name = company = country = ""
            if 'last_name' in attendee['profile']:
                last_name = attendee['profile']['last_name']
            if 'name' in attendee['profile']:
                name = attendee['profile']['name']
                name = name.replace(last_name, '')
            if 'company' in attendee['profile']:
                company = attendee['profile']['company']
            if 'email' in attendee['profile']:
                email = attendee['profile']['email']
                country = self.get_country(attendee['profile']['addresses'])
                email_dict[email] = (last_name, name, company, country,)
        return email_dict


    def make_list(self, attendee_list):
        # make a list of attendees; each attendee is a tuple of attributes
        list = []
        for attendee in attendee_list:
            name = last_name = company = country = ""
            if 'last_name' in attendee['profile']:
                last_name = attendee['profile']['last_name'].strip()
            if 'name' in attendee['profile']:
                name = attendee['profile']['name']
                name = name.replace(last_name, '').strip()
            if 'company' in attendee['profile']:
                company = attendee['profile']['company'].strip()
            if 'email' in attendee['profile']:
                email = attendee['profile']['email'].strip()
            list.append((email, last_name, name, company,
                         self.get_country(attendee['profile']['addresses']),'Yes'))
        return list


if __name__ == '__main__':
    if sys.version_info < (3, 4):
        raise "must use python 3.4 or higher"  # utf-8
    if 'DEBUG' in os.environ:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    fetcher = EventFetcher()
    # Take the id of the first event
    event_id = fetcher.fetch_events()[0]['id']
    time.sleep(1)
    # Fetch the attendees
    attendee_list = fetcher.fetch_attendees(event_id)
    formatted_list = fetcher.reformat_attendees(attendee_list)
    # Write list in vairous formats
    if 'DEVL_PREFIX' in os.environ:
        outdir = os.path.join(os.environ['DEVL_PREFIX'], '')  # development
    else:
        outdir = '/output'   # running in docker container
    datadir = os.path.join(outdir, 'data')
    os.makedirs(datadir, exist_ok=True)
    with open(outdir + '/registration.md', 'w', encoding='utf-8') as fd:
        fd.write(formatted_list)
    with open(datadir + '/registration.json', 'w', encoding='utf-8') as fd:
        fd.write(json.dumps(fetcher.make_dict_by_email(attendee_list), indent=4))
    with open(datadir + '/registration.csv', 'w', encoding='utf-8', newline='') as fd:
        csvwriter = csv.writer(fd, quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(('email', 'last_name', 'first_name', 'company', 'country', 'TIIME2017',))
        for a in fetcher.make_list(attendee_list):
            csvwriter.writerow(a)

