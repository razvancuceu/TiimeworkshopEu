---
layout: page
title: TIIME 2017&#58; Session 8 Federated Identities at the Command Line (13:30/Room A06) (T)
show_on_menu: no
menu: main
---


**Federated Identities at the Command Line (Gerben Venekamp)**

The concept on how you do federal identity management, and do use the IDP. We would like to make it available to federations. A very simple web interface.

**Gerben** : The portal was able to create an OTP and the IOTS site was used to fetch the password and if the user was authenticated could be told. Someone started to mention co-manage later and that got me excited as a lot of things were missing from my portal, so I started using co-manage and now I am at the point where I can do SSH uploading and fetching an SSH key while granting the user access to the command line. I would like to comment and discuss the ideas about the use cases. We have a portal, SURFconext and the IDP. There is the user goes to the portal, and then to the SURFconext which then communicates with the IDP. Portal communicates with SURFconext with SAML and SURFconext to the portal with an assertion. The portal itself is connected to LDAP. SSH is able to get something from LDAP. IRODS(?) can do the same.

**Jim** : The picture looks very similar to what we are doing for (CILogon2) [http://www.cilogon.org/2] and we are planning to support OAuth tokens so that you can link OAuth apps also.

**Gerben** : You have plugins in co-manage which has its database.

**Marcus** : We had a very similar solution, you go to the portal and you are given an OAuth token, and then on the services that you log in with, you use LDAP. We wanted to replace the pam module, which can process the password and talk to the server which makes the token.

**Gerben** : One should try to do something with what is already there. You don&#39;t expect in having difficulties in getting that employed, trying to use a standard component.

**Marcus** : What is the user experience of it?

**Gerben** : One of the nice things is to have strong passwords so that you can randomly generate one. You can give users where they can type in their own passwords.

**Jim** : We want to generate the password for the users.

**Gerben** : Precisely.

**Peter** : Do the passwords expire?

**Gerben** : No, for example I think you want to have the passwords live longer but it depends. What SURFconext offers is that I can check when the user has lost an application-specific password.

**Jim** : don&#39;t OTPs expire straight away?

**Gerben** : It operates on a base of ad-hoc, 30 seconds time frame. There is a clocks-queue, you don&#39;t want to have a strict matching. If you run out of time you have to generate a new one.

**Mischa** : I might have missed some of the use case, but you have the SSH key uploaded now. Why would you need the password? We have a similar setup, you can use the ssh key to run specific commands.

**Gerben** : These people want to have application passwords. They start to understand, we want to use SSH.

**Marcus** : Maybe one comment on these OTP things, what we were considering is to put the access token with Openconext. There are some limitations to the password field and you can&#39;t put more than 64 characters, but in principle you can use that one and then use a different centered server.

**Mischa** : There was a recent RFC for mobile. If you want to get a credential in a command line, you want it to pop out in the browser and to get it back. I think there is a RFC that you can implement in other platforms. ( [https://tools.ietf.org/html/draft-ietf-oauth-native-apps](https://tools.ietf.org/html/draft-ietf-oauth-native-apps))

**Gerben** : But how do you do it with SSH? One of the things that I would like to do is to have an operator that authorizes keys.

**Mischa** : Ben you had this nice file with Niels.

**Ben** : Yes for soft federations.

**Mischa** : The SSH keys are managed by the commands. You have instant access. The keys are maintained by co-manage. I don&#39;t want to have to copy a key phrase, but just to have the key there and log in. If you want to have something that is password based, I would implement something with the browser to pop-up. There are plans for it.

**Gerben** : It&#39;s a nice idea but there is a lot of effort necessary.

**Ben** : Different use cases will require different solutions. SSH keys where plausible, OAuth tokens, etc, or passwords (ASPs) where no other option works.

**Gerben** : Any more questions?

**Marcus** : For SSH we have a fight, that is a slightly different flow and the focus was on deploying SSH keys, there is an instance to which you connect by Openconext for which you use SAML proxy and from there you can upload the key and then other services can subscribe to that key.

**Gerben** : But that&#39;s also managed then, as in who can subscribe or not.

**Marcus** : At that level you have people that want to subscribe to the keys. The concept that we keep for the demo and implement later is to use a mechanism whenever a user comes there, he gets the keys but he can also register and whenever the user uploads a different key and its updated in the whole structure.

**Gerben** : One of the things is that there is only LDAP on my drawing here, but there are usually multiple LDAPs

(Discussion of resource allocation and management using Co-manage, started by Chris)

**Gerben** : You don&#39;t want to have one central LDAP so if you are going to have a really large base then you get into trouble as you have to put a lot of things into a single LDAP. If you have multiple apps then you have to set your ACL, and if it&#39;s configured correctly the application can access it with different applications.

Co-manage should be able to work with multiple LDAPs, this is something that has to be checked.

**Ben** : there is a coordination step that has to happen.

**Niclas** : Important is that this co-manage instance, it says I have this user you should probably create it and there is a whole set of policies on the side that says if the user is allowed to go to the site. There are some legislations that you have to comply with. And then use all of this information to store in my LDAP.

**Ben** : In the model that you are describing you throw some stuff over the wall and then the system decides what to do with them.

**Niclas** : This is just an idea.

**Chris** : you don&#39;t do anything from that on your side?

**Jim** : Succeed has its own system and user database.
