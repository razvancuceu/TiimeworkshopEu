---
layout: page
title: # TIIME 2017 Session 31: SAML Proxy Options (14:15/Room A06)
show_on_menu: no
menu: main
---

**SAML Proxy Options (Mads, Rainer)**

**First half**

**Mads** : This is a double proxy tool. We ended up in a hub. We discovered we had a problem with what we call a double discovery when you go into eduGain you had to select wave and the real IP behind wave. The next problem was that problem that the entity was not the customer and they wanted to have another entity. We make proxies and then send all the proxies into gain and now you can have one customer per entity and the customer selecting the IDP.

You can say that we have a mesh federation on the inside.

**Mads** : It&#39;s a political decision and not a technical one. We need to be able to say to our SPs if you want to be in eduGain with a wise connection just tell us and make a check in the registry then you are in eduGain. So the idea is that instead of operating one hub we are operating two, five, and all.

**Rainer** : but you could do it with a single hub?

**Mads** : No.  The idea is to easily connect to the hub. The point is that the SPs can connect to us and just be made available to the eduGain community.

**Rainer** : So what do you do with the endpoints, does a proxy re-write the endpoint addresses?

**Mads:** You can expose each service as an individual service with an arc.

**Rainer** : Why would the IDP still have an arrangement?

**Mads** : It&#39;s much easier for them. It&#39;s easier to connect to one end point. We couldn&#39;t get people to install SIP at that time, so everybody used SAML. But the wave is fully SAML and the other things can be OIDC.**Second half**

**Rainer** : As I mentioned there are a couple of use cases to deploy SAML proxies. A mesh federation has a legacy protocol. The Dutch federation has collected some selected use cases. We have 20 use cases in a government project where you have to pay the IPD per SP; so if you proxy many apps with a single SP you are saving lots of money. We are doing the reverse of what you are doing, slashing expenses. Then our citizen eID scheme is conformant, it accepts various country credentials. We don&#39;t understand why. On the national side it&#39;s just talking SAML. To integrate into an IDP with various authentication methods it would be impossible to just integrate our national eID SAML as a SAML proxy. Then we have the use case of hub and spoke as I understand in Netherlands as well as Denmark where it&#39;s much cheaper to integrate many SPs in a hub and spoke than a mesh model. Would you agree that these are the main generic use cases for proxies? Protocol conversion, H+S, integrating other authentication methods.

**Leif** : There is at least one working by using a double proxy set up for doing a double blind. You don&#39;t actually get any privacy by doing double blind. They did end to end crypto of all attributes. They did a plugin and a handshake that you used to do for establishments and then you encrypt the attribute not hop by hop but all the way.

**Rainer** : Good point.

Did you use something like a connection between the…?

**Leif** : No it was only used for encrypting the attribute back. It all looked like one attribute. I can&#39;t remember the details.

**R** : I think that&#39;s the only sensible version as you need an attribute container. You need an attribute format which is not SAML specific. Wrap it as Verifyable Claim in a SAML attribute and forget about the SAML attribute structure.

We have now collected 4 major use cases and a long list of products which do proxies. So what I wrote on the top of my head are Corto, Gluu, larpe, Shibboleth, SSP, WSo2, ZXid.

**Scott** : In common is that a lot of people that want to use OAUTH, a hosted service that will translate in between SAML and OIDC.

**Mads** : Corto is a kind of pseudo code. It was &quot;spiefeger&quot; or so I thought. Then the SURFnet came to corto and it was kind of the basis of the interblock for a few years. It had a funny development history. The first version was for the BX services. So it was just as a mass proxy and using something we called meaningless URs. The problem with that and with others is that they are kinda too much. So the newest one that I made is a massive library where you have an API and you make your proxy by coining your library.

What are the key use cases for SATOSA?

**Scott** : we will release SATOSA for an astronomic project in Australia and China.

**Rainer** : There is a Shibboleth-based proxy project at CSC in Finland.

**Henri** : So if you download Shib IDP you can&#39;t use it as a proxy by default but we developed all kinds of identifications including plugins as a part of a project called MPASS and it&#39;s a system towards services who want to authenticate their school pupils and teachers. Usually they exist in directories ran by municipalities. We haven&#39;t implemented all possible plugins.

**Rainer** : this is a SP-IDP combination or an extension of an IDP?

**Henri** : it&#39;s an extension of the IDP. Source code exists at: [https://github.com/Digipalvelutehdas/MPASSid-proxy](https://github.com/Digipalvelutehdas/MPASSid-proxy)

**In a nutshell: we came up with 5 general use cases for SAML proxies**

1. Protocol conversion
2. Aggregating IDPs and SPs
3. Easy of deployment and operation (H+S federation)
4. Double blind proxies
5. Augmenting assertions with attributes from local VOs