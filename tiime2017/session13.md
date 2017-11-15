---
layout: page
title: TIIME 2017&#58; Session 13 Central but Distributed PDP build with OAuth2 (14:15/Room A07)
show_on_menu: no
menu: main
---

**Central but Distributed PDP build with OAuth2 (Peter Gietz)**

Central but Distributed PDP build with OAuth2 and SAML as the identity layer.

Normal User-Browser IdP.

**Pre-Requisite** : SAML based Authentication

Open RBAC (Role based access control), uses an LDAP Server as backend: Users, Roles, Permissions, Resources, and Sessions.

The problem: Any kind of service, wants to interact with an REST API, which has some files hidden behind it.

**Basic idea** :

SAML based authentication, if allowed an OAuth2 Token is created.

&quot;This is a bit simplified:&quot;

A central management, but as many access points as you want.

You first get the authorization code and then the access code.

&quot;Why not just use OpenID?&quot; The left part of the drawing could be replaced with OIDC.

The LDAP Server can be distributed to other LDAP servers. Policy data can be distributed/high availability. The whole architecture could theoretically be distributed, has not been tested as such though.

Access Token not bound to a specific server? Should there be different authentication services to have a failover?

The answer to the question whether this system works as a distributed system, and the answer is physically yes, but not across different trust domains.

Is it based on RFC 7522?

SP --bearer assertion---&gt; OAuth2 AS
