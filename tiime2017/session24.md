---
layout: page
title:  Session 24 &lt;Mobile Native SSO &amp; Difference between Oauth2 and OpenID-connect&gt; (11:30/Room A06) (T)
show_on_menu: no
menu: main
---


**Mobile Native SSO &amp; Difference between Oauth2 and OpenID-connect** **(Rainer Hörbe, Mischa Salle)**

There is a lot of confusion about OAuth2 vs OpenID-Connect tokens. The OAuth2 token can sometimes be used incorrectly. How to use OAuth tokens.

The ID tokens are for encapsulating ID of a user.

What do you do with the next step? If I have a bearer token, what do I do with it? Nothing prevents the resource from using the access token to connect to other resources.

That&#39;s token mining. The point of it is to get tied to the TLS session.

**Mischa** : But then it&#39;s not a bearer token. So you are not supposed to send the access token? I personally think it&#39;s a security risk.

**Uros** : And if you need to go through the proxy, how would the third service refresh the session?

**Mischa** : It would get a new access token.

**Klaas** : The bottom line is when OAuth started out it was supposed to be as simple as possible, you go to the door, show the ticket and the door is opened. Stuff is pulled on top. The bearer token gets diluted to something that&#39;s not a bearer token anymore. If someone else uses that bearer token you should verify it comes from the wrong end point and refuse to accept it.

**Mischa** : in standard OAuth2, the client sends the access token to the RP, and the RP sends the token with the OAuth2 service to get the user info, but that latter connection cannot be bound to the token.

**M** : You need the information from the request otherwise you can&#39;t encrypt it. If you do pure OAuth2 you still have bearer tokens.

**Peter G.** : The misuse is because of the need of delegation and there had been draft 2009 on OAuth security so my question is to Leif is that there have been some attempt to define delegation in OAuth and oauth2 but they never became any final standards.

Delegation example: https://github.com/rescrv/libmacaroons - [https://dx.doi.org/10.14722/ndss.2014.23212](https://dx.doi.org/10.14722/ndss.2014.23212) - &quot;Macaroons: Cookies with Contextual Caveats for Decentralized Authorization in the Cloud&quot; ( [https://research.google.com/pubs/pub41892.html](https://research.google.com/pubs/pub41892.html))

The summary is that people misuse OAuth2 bearer tokens, there is something missing, so who has the time to get into the oauth2 group? Oauth2 is on purpose vague on implementation, being high-level and generic, while OpenID connect is much more precise and detailed on the implementation.**MOBILE NATIVE SSO**

**Rainer** : Providing native mobile apps with single sign on. It has been discussed for some time what are the options how to sign in. One method is to use an embedded browser that is also called web view, the other one system or captive browser. The System browser has the advantage of OS-wide security settings as opposed to the embedded browser. This advantage of the embedded browser is primarily from programmers PoV that the app is not losing control. I realized that QT5 there is a programming framework which is really portable but poorly interfacing with iOS or android. We found some practical difficulties with that. The OpenID foundation has a working group and put some code on GitHub to have a token agent. A native app would have a standardized interface available for the agent and it sounds quite like good news for me as it would lessen the burden for a native app. What is the state of the art?

**Klaas** : I was in the beginning of this native token app but then I moved onto doing other things.

**Leif** : There is a draft called ietf oauth native apps. I think it&#39;s meant to also some of this stuff.

Reference: [https://tools.ietf.org/html/draft-ietf-oauth-native-apps](https://tools.ietf.org/html/draft-ietf-oauth-native-apps)

[http://openid.net/wg/napps/](http://openid.net/wg/napps/)

SDK SURFnet: [https://github.com/SURFnet/nonweb-sso](https://github.com/SURFnet/nonweb-sso)(and blog: [https://blog.surf.nl/en/federated-login-to-native-applications-sdk/](https://blog.surf.nl/en/federated-login-to-native-applications-sdk/))

Embedded browsers do not usually respect privacy settings.

From a usability PoV there is a third option now, the system can be integrated into the app so you aren&#39;t leaving the app. The app can&#39;t have any access to the cookies. It will benefit from browser sessions. There is an extension to the OAuth proof key auto exchange, there is an authorization protocol. It can perform the authorization outflow on android or apple. You don&#39;t run into the risk that someone can catch the authorization code itself. RFC 7636: [https://tools.ietf.org/html/rfc7636](https://tools.ietf.org/html/rfc7636)

The problem is that I don&#39;t know any reference if any identity provider is already supporting it. Some are supporting the OAuth. The question is how to do SSO nowadays? This is a very good question. We have the napps, one login, we can use openid connect. What is the best approach?

**Mischa** : It would be good to have something where you can get a token. Now you have credentials in chrome for all different devices.

**Leif** : It&#39;s relatively new. TV display is like 4 PIN code. Short-lived. You can use that to provision the cross-state. It&#39;s specified as an OAuth2 cloud.

**James** : What&#39;s the reference on that?

Leif: [https://tools.ietf.org/html/draft-ietf-oauth-device-flow-03](https://tools.ietf.org/html/draft-ietf-oauth-device-flow-03)

geteduroam

[https://play.google.com/store/apps/details?id=nl.nikhef.eduroam](https://play.google.com/store/apps/details?id=nl.nikhef.eduroam)

Src code: [https://github.com/synnack/nikhef-eduroam/tree/master/android/src/nl/nikhef/eduroam](https://github.com/synnack/nikhef-eduroam/tree/master/android/src/nl/nikhef/eduroam)

**Leif** : You want to write an app in a framework that enables you for the app to be able to be on multiple platforms.
