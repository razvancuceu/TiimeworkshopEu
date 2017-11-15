---
layout: page
title: TIIME 2017&#58;  Session 20 Provisioning (10:45/Room A06)
show_on_menu: no
menu: main
---


**Provisioning (Femke Morsch)**

There is a use for daily provisioning and 20% of institutions are doing provisioning themselves and they also ask us if we can help them with the provisioning.

**Femke** : Deprovisioning is a problem. We can&#39;t ignore it. It&#39;s not really a problem of the federation. We would like to hear from you the best practices for provisioning.

**Ioannis** : We are one of the examples that provided a solution like that for our customers. A couple of months ago we rolled out a service to allow a provision. This is something that we have been asked by the university and we had support from Microsoft for that. It was a bit tricky but what we ended up doing is that we used is that people log into the SP and that SP uses the platform. It worked quite well, we had good feedback, and we handle the deprovisioning part. We set expiration dates on an account. For students expiration is OCT of next year and faculty gets an account forever. This came up after discussing it with Microsoft and the university. There is a grace period to get all of the data back from the service.

**How does the grace period work?**

**Ioannis** : You have three months that the account stays and you get an extra month and then your data is deleted, but we want to do the same thing for Google Apps. For Google apps the plan is to use homogenization to access google apps, so if you don&#39;t deprovision the accounts they won&#39;t be able to access their data.

**Niels** : Would you make a massive proxy to handle multiple SPs?

No, as it scales pretty badly.

**Klaas** : I can tell a bit about how I did this. For those that don&#39;t know the past 2 and a half years I worked as an identity manager for cisco clouds. To understand what we did I need to say a bit more about the architecture of the whole thing. The business model is that the large SPs resell cisco cloud services. Many telecoms resell it. We built a federation where we control the hub and the SP. We have looked at SCIM and in the end we went with a rudimentary approach. We made the identity providers register every user at proxy. Authentication happens at the IDP and that&#39;s where we control provisioning and deprovisioning. You have to go to the proxy and if the user doesn&#39;t go to the proxy the user doesn&#39;t have access to the service.

How did you provision them to the proxy?

We built an interface, in the shape of a web form. But it needs a manual approach.

**Leif** : We have been talking about using the built in features. LMSs is one of the situations where you would want to do the provisioning. People decided that we needed that. Deprovisioning is easier. OIDC adds a bit of complexity. We discovered that people were uncomfortable having firewalls opened. The refresh token is sent back but the point is that you can get it, you can keep refreshing that user info for as long as you like, which is deprovisioning. The only thing that you need to add to this is a notification, if you have an IDP that says that the user doesn&#39;t exist anymore, then you need a long-term log out. This user has logged out, period. That is where the OpenID comes in.

SCIM is used in connect to provision software statements which is to make claims about collections of clients. People would rather use SCIM as the implementation is easier.

Another scenario which was discussed was to see if we could use a SAML query to provide real time information if the user was still alive. It could be a polling model. We are seeing some service systems.

**And you think you can get them to implement SCIM?**

It&#39;s easier to get to SCIM. If you look at the google user database. If they make another endpoint for management, it&#39;s going to be amazing.

The message format is the question. You would recommend to derive the message format? It&#39;s a signed JSON and there are a few standardized parameters.

**Mads** : I want to mention if you remember STINUS, I had a provision service, and I thought I was too old fashioned. Have specific plugins and to have a premise as nobody wants to authenticate from the outside. The services then need to be provided. The stores in the middle are only for configurations, no user data was stored in the middle. High performance is present in the middle.

**Ioannis** : That&#39;s another aspect that became relevant. When you think about the model that you will use, if you put a proxy in front of a service that might not be possible for all services, as they are something that you buy. Microsoft didn&#39;t want us to have a proxy but to have users go directly to Microsoft. That might not be possible for all services. We do have LMSs and they wouldn&#39;t have issues with the proxy but some bigger companies would not be fine with it perhaps.

**Mads** : You can do some provisioning, you don&#39;t have to have a proxy but only an endpoint. Anyone that allows you to stick their IDP doesn&#39;t let you have a choice. It doesn&#39;t have to all be in the same protocol. Could we bootstrap trust for SCIM? Stuff like that could be pretty useful.

**Peter G.** : We had a couple of projects where we had old style SAML and in some projects this wasn&#39;t enough and we had to think about provisioning and deprovisioning. All the schools in a part of Germany were using eLearning and they needed to know whether the student was still in the class or not. What we did is again old style SPML which we then extended to AR and then we decided if the endpoint will write any documents but talk directly to SCIM.

**Femke** : You think that SCIM can become mature enough.

**Peter G.** : SCIM is much faster than SPML.

**Femke** : In Greece where provisioning is done by the user is a nice approach. I am not sure if our institutions would like it as the user should be set before he starts with university.

**Ioannis** : Nobody was thinking about a platform like this and that might change as the users are stopping to care about their mail server. Then the things might start changing. For now, the use case is a bit specific for us, but I can see that that might change in the future and that might affect how relevant provisioning is.

**Niels** : Leveraging can be attribute authority anyway and we would just have a scenario where you would have to provide account status which would be tied to the person. The SP can make a query to check if the person is still alive.

**Leif** : Let&#39;s say you are an SP and need to check if the user is still alive. You can either do nothing or to send an email and to see if something comes back. But you are as an SP totally in the dark.

**Rainer** : There would be an alternative to keep the user data for a long time, 2 and a half years and before you deprovision after some idle time send a message to the user and ask for a decision. I am going to delete your stuff if you keep being inactive. (Assuming you have the email address)

It depends how much content you keep for the user because if there is a lot then you don&#39;t want to keep it for that long.

**Femke** : It&#39;s nice to have a look in the scheme of &quot;is the user alive&quot; and it&#39;s something good to look at.

**Niels** : If you are a federation it&#39;s a good thing to look into. If we run into a SP talking to a federation 1 and getting different results back.

**Leif** : There is a one strong suggestion is to turn off that the ID events don&#39;t pay attention. This is why we want to extend the scheme. By the time internet 2 figure out that they need to go to SCIM their working group will be closed. They would&#39;ve had significant impact.
