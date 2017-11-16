---
layout: page
title: Topics
position: 2
permalink: /topics
show_title: no
menu: main
---


 <div class="row topics-list">
    <div class="column">
 {% for post in site.posts %}
  {% if post.categories contains 'topics' %}
	<div class="post">
        <div class="featured-image">
            <a href="{{post.more}}" title="{{ post.title }}" alt="{{ post.title }}">
                <img src="{{ site.url }}/{{ site.baseurl }}/topic/images/{{post.img}}">
                <div class="featured-category {{post.color}}"><span class="bkg"></span><span class="text">{{post.cat}}</span></div>
            </a>
        </div>
		<h3 class="title"><a href="{{post.more}}" title="{{ post.title }}" alt="{{ post.title }}">{{ post.title }}</a></h3>
		<div class="entry">
            <a href="{{post.more}}" title="{{ post.title }}" alt="{{ post.title }}">
			{{ post.content | strip_html }}
            </a>
		</div>
	</div>
  {% endif %}
{% endfor %}

    </div>
</div>

## Explore Identity Management Issues and Initiatives

Internet identity, identity federation and personal data online are complex, continually evolving areas. 
Participants will seek deeper understanding, and better solutions to challenges like:

* Technology. Developing feasible and open standards.
* Community projects and OSS software. Who, what and how?
* Privacy. Improve quality and scalability of privacy practices and controls.
* Personal data ecosystem. Vendor relationship managelemt, personal clouds, data sovereignty.
* Trust Frameworks. Establishing new paradigms and policy sets.
* Usability. How can users navigate different identities and understand their data?
* Economy. How can identity services fit into businesses requirements and opportunities for all stakeholders?
* Interoperability. On which levels and areas is interoperability necessary or feasible? This is a cross-cutting concern for technical, legal and business views.
* Deployment and operation. How can different options be supported and exploited in the best way, given the whole range of places and devices.
* eIDAS integration challenges.


Besides discussing specific topics in the above areas, there will also be plenty of opportunities for networking among solution providers and seekers, startups, investors and technology pundits. EIW provides a place where skilled people from a wide range of functions and projects in the identity ecosystem gather and work intensively for two days.

The unconference format puts into the foreground what is important for the participants. How much attention topics receive is driven by active participation. Results will be collected and published at the and as proceedings. After the brief introduction on the first day there are no formal presentations, no keynotes, no panels.

What happens then? We will make the schedule when we are face to face the first day of the conference.

We use a method called Open Space Technology to support unconference where the topics most important to the participants that day are discussed. How much attention topics receive is driven by active participation. This supports a self-organized and self-responsible group unleashing the great creativity and passion of the participants. Results from sessions will be collected and published at the end as proceedings.

## Communicate Across Initiatives

There are numerous IDM-related efforts and projects in both private and public sector. The workshop is a place for direct talks skipping hours of time-consuming powerpoint presentations. Take the opportunity to form the contents yourself!

## Topics

After the morning keynote, the agenda will be created dynamically by participants at the beginning of each day. Participants have 
the option to propose topics via a survey in advance. The context of the workshop suggests topics such as:

### Categories

* Connecting different types of stakeholders (startups, enterprise, investors, privacy experts)
* Federation & cloud identity
* Identity interoperability (cross-border, across sectors, different assurance levels, technologies)
* Trust Frameworks - business, legal, governance
* PKI and secure collaboration
* Identity initiatives - connect, learn, contribute, join
* User-centric identity management

### Subjects

* Attribute management
* Business cases for federated IDM
* Discovery service, Account Chooser
* Delegated authZ, UMA
* Data protection regulation; consent
* Identity proofing and verification
* Mobile Strong authentication
* Mozilla BrowserId
* Privacy preserving IDM
* Online reputation
* Payment and Identity
* Personal Data Store / Personal Cloud
* SAML/OpenID/OAuth: Competing vs. hybrid scenarios
* SCIM
* WebSSO technologies: OpenID Connect, OAuth, JWT, JOSE
* XDI

 
## Topics from the 2013 survey

### I want to present about:

- Country: Austrian's govermental identity federations
- Country: Denmark eID status and developments
- Country: Finland's Federated identity , trust chains that it creates between banks, telcos and the government. Telcos are now offering strong authentication based on Mobile PKI. wo government IDP-proxies have been interlinked using IDP discovery based on a common domain cookie to reduce costs and comply with government agency service mandate policies
- Country: Sweden's Federation Initiatives (e.g. eId and School federation)
- Federated Identity as a Service (Federated Identity Brokers)
- Personal information and privacy: Markets
- Project: Biobank Cloud Security
- Project: DARIAH as example of a Virtual Organisation as member of a Federation in eResearch contexts
- Project: Efforts to eliminate paper from many student related processes like paperless Erasmus or Digital Student Data Depositories.
- Project: SSEDIC (Eurepean Expert Network on Digital Identity) results
- REFEDS
- SaaS 1-click provisioning of providers
- SAML and OAuth worlds in a seemingly secure way, for mobile applications (University)
- SAML Test Harness
- SCIM
- SPML dead or alive?
- STORK/SAML use cases for existing federations (2) follow up discussion on SAML interop. w.r.t. STORK, collecting proposals from the SSI-WG (especially on harmonisation) for STORK to eventually share with ISA STORK Sustainability Action. If other topics are discussed (i.e. benefits/gaps for integration with some existing federations) I can also convey this to STORK.
- W3C wifi device API and spec to configure EAP (namely eduroam connections).

### I want to learn about:

- Agent technology for privacy and identity management
- AuthN: Second factor authentication and new second factor authentication methods
- AuthN: (Multi-factor) authentication as a service: Solutions for identity vetting in order to assign individual users higher LoA
- Cloud Identity
- Consent: Organization of consent services
- Data interoperability issues
- Delegated authZ, UMA
- Delegation mechanisms to encrypt data in cloud computing
- eID/LoA mapping
- eID national practices and proposed EU regulation The applicability of OpenId Connect to bridge national eID's Trust/accountability frameworks User centric services
- eID: Regulatives for what is identity and its different types. + what are more like "attributes"
- EU Data Protection Directive / General Data Protection Regulation and its relationship to federated identity models. Privacy-enhanced SAML to deal with the above
- FIM: Business cases for federated IDM
- FIM: Practical ways to increase the scope of current federations
- FIM: Linking of other identities to "our" (NREN federation) identities. ("Other" in this respect are: - Facebook / Google - Government ID)
- Group management (as a wide concept)
- Higher Ed: How can systems developed in the Higher Education sector be adopted/adapted by/for the wider community, or seamlessly interwork with the wider community? How can we better manage personal attributes? eg common international definitions of attribute values.
- Identity as a service & open standards
- Mobile/Telco related identity projects or initiatives (eg GSMA Mobile Identity project) -
- New identity mechanism
- Personal data access and secure identity management from mobile applications
- Personal data and privacy in general
- Personal Data Store / Personal Cloud
- PKI
- OATH (2)
- OAUTH (2)
- OpenID-connect (4)
- SAML: Any work on identity or SAML is of interest.
- SAML for mobile devices/installed applications in general
- SAML/OpenID/OAuth: Competing vs. hybrid scenarios Mobile Strong authentication
- SAML Metadata Management
- SCIM
- Signature services, signature APIs
- Shibboleth (2)
- Shibboleth and OpenID: Differences
- SLO standard based solutions
- UMA
- Unobservability with trusted 3rd parties

