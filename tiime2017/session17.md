---
layout: page
title: TIIME 2017&#58;  Session 17 Backchannel attributes flow  (15:30/Room A07)
show_on_menu: no
menu: main
---


**Backchannel attributes flow (Davide Vaghetti)**

Problem where the idea/desire to discuss this came from: Attribute Release Problem

An attributes flow that is happening without user intervention or even without the user knowing.

**Two points of concern:**

- Consent
- Attribute Release Policies

Browser is accessing ServiceProvider, can contact authorative AA.

IDP can also contact AA via Backchannel

Case: IDP/SP Proxy, then through IDP, then to SP. Can ask for consent.

One case where the responsibility to ask for consent is on the SP side, which is out of our control.

**Example AA strategy** : SURFconext: User can add themselves to teams, then consent is asked to store the information and to release when asked. The AA asks the user for a consent to send this information to ANY service providers that asked. Consent is implemented by default with all the IDPs, but it can be disabled on an IDP basis if they for example have some other arrangements. The responsibility to handle this rightfully lies with the home organisation IDP.

&quot;There is a ground&quot; for this information to be passed to the supplier.

**Summary** : Consent can be asked one time before, for specific AA and attribute set.

**Law says** : If you cannot operate your business without this information, you do not necessarily have to get consent.

**Legal ground** : Consent, legitimate interest

**Idea from eduID** : Central IDP only has some information about the user. All of the details about the user relationship with the home organisation, are kept with the IDP home organisations themselves, which are part of the Switch Identity Federation. Combined they are one big trust domain. The central IDP will decide based on the central Attribute Release Policies, what to release (instead of all the home organisations having their own policies). Each time there is a request, the central hub receives all the users&#39; data, but then only releases the ones based on the policies.

Why would an IDP customize their ruleset? Wouldn&#39;t there be the same needs, at two universities?

**Suggestion** : First make an inquiry about the needs of the IDPs and then build something.

**Netherlands** : A minimization of the attributes which are released, the proxies have the policies and are controlled by the federation. One policy for all IDPs by one Service Provider.

Take another look at the definition of data processor. The data processor just implements/applies the data, but does not make any decisions.

&quot;You collect - you&#39;re responsible&quot;. An entity can be both data processor and data collector.

Another scenario: IDP/SP Proxy connected with eIDAS (authentication &amp; some attributes) via a trust relationship

**Summary** :

Different scenarios as solutions to the Attribute release problem, focusing around a centralized structure and policies. It´s one thing to start off with a centralized proxy structure, and another to try and clean up a lot of different policies and structures.
