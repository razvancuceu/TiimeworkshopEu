---
layout: page
title: TIIME 2017&#58; Session 16 Catching up with ORCID (15:30/Room A06) (T)
show_on_menu: no
menu: main
---


**Catching up with ORCID (Laura Paglione)**

[https://www.orcid.org](https://www.orcid.org)

We are a non-profit org, our vision is for everyone who participates in research, scholarship and innovation, to be able to do things without borders. This is a 16 character identifier, and it can be used in many fields. It might be getting funding from a gov funder, or submitting a manuscript for publication, and what we do is develop relationships with those orgs to use the identifiers, instead of having just a name.

They can use it throughout the career, they can change the things associated with the identifier, but the identifier stays the same. The key thing is to distinguish people from each other. We have 3.1 million researches that are using our identifiers. We have 11 national consortia, where a group of organizations join at the same time. For example, when the Italian consortium signed up, 94 organizations joined at the same time. The 645 global members have developed over 550 integrations. There are fewer integrations than memberships because it takes a bit of time to develop an integration, so it is just a time-shifted issue.

The associations are organizations like IEEE, the geophysical society, either national or international professional associations. A lot of them signed on as members quite early, and some also serve as members, so may be included in the publisher group instead.

To give you an idea of participation by region, EU is far ahead (52%), and the reason are because most of those consortia are in Europe. The US and Canada are grouped together, it&#39;s the second largest group. Asia pacific are next, there is also Middle East and Africa but they are the smallest piece of the pie.

Our view is from a researcher point of view and all of the things that the researcher might be connected to are shown around them. Peer review activity, funding etc. We have an ORCID record which is like an index to see information. Privacy data control and it&#39;s all person centered.

This image is about the programming that we communicate with the organizations. We get them through our progressive situation. They might just be collecting the data, collecting the ID to either pass along or because they are tied to this information. We really encourage them to go further, to display that ID. They may have collected the ID and they might&#39;ve displayed it on the profile now.

The next stage is connecting, that&#39;s where we encourage orgs to put their information into the ORCID record. In the connect stage we are encouraging a university for example to push the information about a student into the ORCID record.

**Berit** : Are these signed or?

**Laura** : They are signed to a degree. It&#39;s done through OAuth tokens and Oxford would have a client token and they would be pushing the information in at this time. Its signed to a degree.

**Allan** : But you can tell that it&#39;s verified from that org?

**Laura** : Yeah it says it&#39;s from that source. A good example is with the publications, I publish an article and a library knows it as well and they put it into the ORCID record so you can see three assertions for what I have written.

**Femke** : So the user is initiating with the university for example or is there a back channel.

**Laura** : An individual has the ability to sign into the ORCID record in order to transmit the data. That signing into the ORCID record can happen through an institutional sign in. We need to enable the sign in IDP.

**Berit** : Is it all on your servers?

**Laura** : it&#39;s a distributed system. We provide the ID to be pushed to the orgs that are collecting the IDs or the permissions for that information to come back into the ORCID. We provide the infrastructure for who is able to access the information. I as a researcher have a choice to share it with different entities either public or some other orgs or nobody.

In May of 2016 we launched our SP which enables individuals and we are registered with SURFconext. You could only sign in with ORCID credentials but now it&#39;s more than that. If somebody ends up in someone else&#39;s account due to the change that would be our fault.

If you are interested in how many connections are inserted, 28.5% of all institutions have had an attempted sign-in into the ORCID network. The 28% is divided into successful sign ins by 100 or more people from 28 institutions, successful sign ins by 10 or more people from 255 institutions and most importantly, previously unsuccessful but now successful sign in from 31 institutions. The people who can&#39;t sign in are presented with a page of the ORCID SP, what is required, not required and it goes on to say if you provide with a particular attribute.

Another thing that a lot of institutional members were interested in is that they signed with the IDP but there is no ORCID ID so what we&#39;ve done is that we used our OAuth model. When someone signs into ORCID that has the ability to collect information from the individual, we kick off the permission request. University adds permission-based assertion of affiliation on ORCID Record.

[https://www.youtube.com/watch?v=eTJgTWwWLUU](https://www.youtube.com/watch?v=eTJgTWwWLUU)

**Allan** : how does it work for the individuals? Do they register for free?

**Laura** : The registration screen is super easy. If you try to apply twice with two emails you will get reminded that you already have an ID. We don&#39;t ask for a verification for the email. http://imgur.com/a/xBJ5v

**Berit** : Are you certified?

**Laura** : We are certified by Truste, as we couldn&#39;t apply for the Privacy Shield.

**Laura** : We made a button so if a user clicks on it they are brought to a permission screen. Then we encourage them to share their data. It&#39;s not a link to our registration page, it includes the permissions that the university is trying to get so the individual is trying to create an ID and granting the permissions at the same time. It also doesn&#39;t create IDs for people who have it.

**aura** : We think that people should use one ID, but we don&#39;t restrict it. To be honest, for any particular interaction that the user has, it should be one. It shouldn&#39;t be multivalued.

**Allan** : if they want it multivalued they can use the values somewhere else.

**Thijs** : institutional IDs don&#39;t usually know ORCID Ids.

**Laura** : We are working on how we can get IDPs to get ORCID IDs.

It&#39;s much better to look at the LDAP then to look it up.

**Thijs** : We see LDAP as an account database and if there is no place there it&#39;s their decision and we think that&#39;s a given for now. We are looking at the attribute authority on the central level to do this. And if an IP provides it we don&#39;t have to use LDAP. The biggest challenge is that we have is how to use self-access and I get from the IDP some access. Then we have to have some kind of linking.

**Laura** : we are trying to facilitate in the ORCID registry because there is an opportunity to get additional information. We think that there is a place for both.

**Thijs** : I heard that there is an ORCID API that is free and paid for.

The fees are very low and we are still almost sustainable with membership fees. The difference in the APIs is the frequency of access, less access for non-member. The big difference is that the public API allows you to get an authenticator ID and do some basic searches. However, in order to retrieve limited access data (to be an individual&#39;s trusted org) you need to be a member. We have a basic and a premium is the difference is based on how many integrations you are having.

**Thijs** : What are the actual rate limits? They are listed as &quot;good&quot;, &quot;better&quot;, &quot;best&quot;

**Laura** : they are not implemented yet, so the actual limits are not yet set unfortunately.

_[Additional note from_ **Laura** _: we plan for there to be a difference in limits when traffic when we see increases in use.]_

**Laura** : we support 11 languages, and this year we added a translation tool. It means that more languages can be added more quickly.
