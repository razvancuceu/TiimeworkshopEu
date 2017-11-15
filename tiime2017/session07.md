---
layout: page
title: TIIME 2017&#58; Session 7 Mapping between (e.g.) SAML &amp; OIDC attributes (11:30/Room A11)
show_on_menu: no
menu: main
---

**Mapping between (e.g.) SAML &amp; OIDC attributes (Mischa Sallé)**

Best practice - SAML -- OIDC attributes/claims mapping

Various attempts

Started with informal group.   REFEDS mailing list archive: [https://lists.refeds.org/sympa/arc/oidcre](https://lists.refeds.org/sympa/arc/oidcre)

Wiki page: [https://wiki.refeds.org/display/GROUPS/OIDCre](https://wiki.refeds.org/display/GROUPS/OIDCre)

RFC working doc: [https://github.com/refeds-oidcre/eduperson-jwt-claims](https://github.com/refeds-oidcre/eduperson-jwt-claims)

Planning/mapping spreadsheet: [https://docs.google.com/spreadsheets/d/1YirGURSkivafVSZCykDuqQjKGKlUu4uHHNHTNB-n\_Ic/edit](https://docs.google.com/spreadsheets/d/1YirGURSkivafVSZCykDuqQjKGKlUu4uHHNHTNB-n_Ic/edit)

A few people (Niels van Dijk, Jim Basney, ..) discussed this already and presented this at EWTI December 2015.

Notes from the previous EWTI session: https://rhoerbe.github.io/wwwTiimeworkshopEu/identityworkshop.eu/past-events/ewti-2015/proceedings/18-december-2nd/102-session-18-mapping-eduperson-to-oidc-claims.html

We have a distributed federation in the SAML world whereas OIDC does not, although some work is going on.

Very pragmatic thing where we come up with a best-practice-recommendation in SAML. In the end it is always an implementation-choice if you do mapping.

Markus is displaying documents from the OIDCre wiki:

[https://wiki.refeds.org/display/GROUPS/Transforming+Identifiers+between+OIDC+and+SAML](https://wiki.refeds.org/display/GROUPS/Transforming+Identifiers+between+OIDC+and+SAML)

[https://wiki.refeds.org/display/GROUPS/Mapping+SAML+attributes+to+OIDC+Claims](https://wiki.refeds.org/display/GROUPS/Mapping+SAML+attributes+to+OIDC+Claims)

**Straight mapping from A to B**

At the mapping &quot;I want to make sure that it goes both ways&quot;.

We are talking about page 24 in [https://aarc-project.eu/wp-content/uploads/2016/06/MJRA1.3-Design-for-the-integration-of-an-Attribute-Management-Tool.pdf](https://aarc-project.eu/wp-content/uploads/2016/06/MJRA1.3-Design-for-the-integration-of-an-Attribute-Management-Tool.pdf)

It shows a mapping of eduperson to oidc attributes. Remark: sub is not scoped, but local. To be unambiguous you need to write iss+sub.

We should define something so that anybody can participate to work on this.

Two mapping strategies in use at the same time: map some of the basic information (should work with a basic client out-of-the-box). Next: additional profile to provide mapping to claims that have the complete set of eduPerson attributes

Extensions for clients for advanced scenarios.

Next we see a table. All that is yellow is problematic.

Potential issues (Column &quot;Remark&quot;):

Roland can no longer chair the REFEDS OIDCre WG, Niels Van Dijk volunteers to pick it up.

Maarten is proposing to forward this as a strawman proposal to Nicole, and ask her to start a consultation in REFEDS. Registration can happen afterwards. Chances to have this recognized by the OCID group are low. The proposal should be limited to the R+S attribute.

It would be nice if Nils sends a message to Nicole at the end of the session.

First we will solve the simple mapping scenario:

How to deal with the identifier? Red parts at the table (gender birth date...). we should be able to come up with a safe list.

Niels&#39; proposal for order of handling things:

1. Simple mapping
2. All (of the useful parts of) eduPerson/SCHAC
3.  R&amp;S

Double-checking of what is the &#39;simple mapping&#39; list:

-Identifier (proposal in comment from Tom Scavo on the OIDCre wiki [https://wiki.refeds.org/display/GROUPS/Transforming+Identifiers+between+OIDC+and+SAML?focusedCommentId=13107203#comment-13107203](https://wiki.refeds.org/display/GROUPS/Transforming+Identifiers+between+OIDC+and+SAML?focusedCommentId=13107203#comment-13107203))

**The problematic attributes:**

eduPersonAffiliation

eduPersonScopedAffiliation

eduPersonEntitlement

We already have a global community to give feedback.

**Proposal:**

Everyone who wants can join the REFEDS OICDre (https://wiki.refeds.org/display/GROUPS/OIDCre) working group.

Leif suggested to start a claims registry at IANA for having easy unambiguous handles to any OIDC/SAML/etc attribute. Actually there could be an IETF FO-working group for a couple topics, which would provide the resources for this.

There should be an IETF-workstream. We need to write a RFC.

Niels will be writing a proposal about what attributes to use.

Niels will present the conclusions in the summary session.
