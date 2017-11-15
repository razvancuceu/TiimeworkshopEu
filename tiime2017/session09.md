---
layout: page
title: TIIME 2017&#58; Session 9 Mobile driver license (13:30/Room A07)
show_on_menu: no
menu: main
---

**ISO 18013-5 mobile Driver&#39;s License (mDL) (Oliver Terbu)**

All information provided is not decided and not part of any official standard. The information only reflects the personal opinion of the presenter. It is also not intended to create a new eID standard. Priority have attended use cases where the verifier and mDL holder have physical contact.

**Two models:**

- Offline out of scope for this workshop
- Online

**Problems**

OIDC feasible approach in general?

Mitigate privacy issues due to issuing authorities potentially seeing every transaction

Assurance level framework - NIST, eIDAS, gov.uk/etc. (which one/mapping?)

How does it play together with eIDAS, gov.uk/etc.?

Could we solve part of the &quot;which assurance framework?&quot; problem by using something like a refactored Kantara &quot;meta IAF&quot; as discussed in: [https://tiime.pad.sessiontracker.eu/p/sonofiaf](https://tiime.pad.sessiontracker.eu/p/sonofiaf)?

It turned out that for the use case specifying the authentication context class reference may be sufficient rather than using one specific assurance level framework. OIDC also supports means to express the authentication context class reference values.

**Architecture**

1. 1)Provisioning online token
2. 2)Token exchange
3. 3)Trust model
4. 4)Federation protocol or REST to exchange mDL data

**Requirements for this workshop**

- --mDL verification across jurisdictions
- --Uni-directional communication between verifier and mDL should be possible
- --Verifier authentication should be possible
- --Verification with online token should be possible when mDL is offline (pre-loaded tokens) - but mDL has to at least sometimes be online

**OIDC model**

- ---provide token + URL
- ---service discovery at URL
- ---dynamic client registration
- ---authZ request using token as login\_hint and retrieve id\_token after providing 2nd factor
- ---provide optional user info endpoint

**Assumptions:**

Verifier has:

ICAO PKI database access

Bilateral trust agreements between verifier and issuing agencies

**Questions**** :**

**TFP**?

Answer: out of scope

**Why using OIDC, which relies on browser TLS, which is not real security, rather than signed SAML?**

Answer: OIDC supports signed encrypted request objects and id tokens are also signed and optionally encrypted.

Remark: There are no consistent implementations available for this option.

**Why go online at all?**

Answer: in the online model you can get attributes from the issuing authority online - get immediate effect in status changes.

Discussion of payment system model - offline key used to sign a transaction with a reader, only the reader needs to be online. This could be a model when the mDL is off-line in case verification is needed.

With OICD all trust is derived from endpoints on the transport layer; extending it with signatures is not standard. It was also stated that OIDC does also support encrypted request objects which may be signed and id tokens are signed by the IdP and can be optionally encrypted.

Revocation (opposed to ICAO) should be possible

Two levels of key revocation needed:

- Issuing authority keys
- Individual credentials

Authentication of a driver&#39;s license online requires the entry of a second factor to prove presence - require specific authentication context

Four bridges forum as a federal PKI bridge - look into using this for rooting trust - US gov, pharmaceutical industry, UK/Netherlands gov&#39;t., Aerospace industry, etc.

Hooking into a heavy duty PKI infrastructure makes sense here because it is a government high-assurance use case. The most advanced instance are the PKIs linked up in the Four Bridges Forum ( [http://www.the4bf.com/](http://www.the4bf.com/))

The use case requires secure message exchange, metadata registry, LoA, message level encryption. SAML has that out-of-the-box, with OIDC this is years away until becoming mature. The key benefits for OIDC are message compactness and ease of use for JavaScript clients. It was also mentioned that OWASP considers OIDC as secure and stable.

After further discussions it turned out that it is not possible to register every SP i.e. verifier. SAML typically relies on a metadata registry.**OIDC feasible approach in general?**

Mitigate Privacy issues because issuing Authorities can potentially see every transaction

Assurance Level Framework (NIST,eIDAS.GOV.UK,etc.)

How does it play together with eIDAS.GOV.UK etc.?

**Architecture**

1.
  1. Provisioning of mDL DATA, or online token (out of scope)
  2. mDL data , or token exchange (in scope)
  3. Trust Model (in scope)
  4. Federal protocol, or REST (in scope)

For example a simple bar code should have enough information to give someone the priority to drive a car for example.

**Requirements:**

1. mDL Verification across jurisdictions
2. Uni-directional Communication between Verifier and mDL SHOULD be possible
3. Verifier Authentication SHOULD be possible
4. Verification with online token should be possible

**OIDC model**

1. Provide token-URL

2, 3.Service discovery URL

4, 5. Dynamic Client Registration

6, 7. Create authorization request using the token as log in

8, 9. Optional user info endpoint

In most cases we should use a browser but in this case the token is being used.

Actually the biggest pro of this system is that you will not need any more a physical id which you need to use but this also opens a big issue with copying the information.

There are two models the online and the offline model the online is not required is actually an added option.In common and similar systems only the reader needs to be online but the user doesn&#39;t wait every let&#39;s say 10 transactions in order to refresh.

It is based on explicit trust. If let&#39;s say someone is using open id connect because it is easy for implement but then you lose the benefits of it because it is different.

There is also this bilateral trust problem because if the key does not work it will need to be replaced and basically someone else could steal the information this way. The person needs to be authenticated as well and there will also be a second factor.

It cannot be done without any central registry so there is a big complexity so it is years away from any realistic implementation. The problem is that it actually is not scalability use cases.

The only way to do authentication well is by challenge and response all the other ways like time based authentication is not secure enough.

The second factor could be by a challenge for example.

A driving licenses can be used as a proving device for many things like buying age restricted items , showing nationality , etc. this device can be used for all other means of authentication , it is only one device . The holder will be authenticated.
