---
layout: page
title: TIIME 2017&#58; Session 4 Attribute Aggregation (11:30/Room A06)
show_on_menu: no
menu: main
---


**Attribute Aggregation (Thijs Kinkhorst)**

**Synopsis** :  _Project about implementing a proxy to handle user attributes that belong to multiple service providers easier._

**Thijs** : There are several steps that have to be done. One is how to release the attributes and we have two options or we get the proxy. We kind of tried both approaches as both have advantages and disadvantages. With attributes it&#39;s easy to prioritize, but the SP can read the information. This is the model that we can use in our university because the servers are trusted. For outside we are trying to employ a proxy model.

**Femke** : With the consent we are trying to implement a good solution, where we show the user and we want to release these attributes, and the user can approve it, deny or check the box don&#39;t ask me ever again. Most said &#39;never ask me again&#39;. You have the consent from users and they are happy.

**Slavek** : If you have the proxy solution the attribute authority needs to entrust that this proxy will indeed be the only querying.

**Thijs** : We can register users outside of the organization, the users come and we store them in our system. We store them when they come the first time.

**Slavek** : That might prompt your question, how do you know that the attributes change?

**Thijs** : We don&#39;t know about the change immediately, but we can later then choose, it&#39;s okay for users to renew the membership after a year. If there are some special requirements, you can shorten the period, or you can renew the membership once a month for sensitive data.

**Slavek** : When you start a virtual machine, the user doesn&#39;t need to log in to utilize it.

**Thijs** : We had the same challenge with SSH, the user logs into a portal. One solution would be to have an emergency procedure that you can just call a number and someone will disable it. Might also be sufficient based on how many times you expect this to happen. It&#39;s fine if it happens once a month, and the user is not compromised on a daily basis.

**Slavek** : the expiration of the users is the issue and they can still run virtual machines with SSH and you need to think out of the box.

**Thijs** : What happens if user is logged in at 5 different service providers, what do we do?

**Slavek** : You just wait for it to expire, after 10 hours for example.

**Thijs** : It is a challenge because we are adding more and more service providers, we can call them now and say it&#39;s compromised, but it&#39;s too many it&#39;s hard to call everyone.

**Femke** : There is a difference if you have the ORCID ID which you can cash for a long time or attributes which should be live for when you check the attribute if they are still there.

**Raluca** : Lady from ORCID said how other people are doing it, they integrate their ID in their systems.

**Femke** : We are not only thinking about attribute queries but we can use OIDC.

**Thijs** : That&#39;s the nice thing about it, we can have different back-ends

**Raluca** : Everyone dreams of different back-ends.

**Thijs** : If we are dreaming, this is the first step to add more information. At least in our world and that&#39;s it and we are trying to make a new step here but if you look at it, it&#39;s the other way around, any attributes might come from a different source. The fact that I am an employee at university X will be queried from university x. It will say I am a student there or that I am associated with this faculty so they will not have passwords. Students are very mobile; they are not interested in 5 different accounts in 5 different universities.

**Slavek** : I think it&#39;s doable in your federation. You have the proxy and if the university is willing to provide you with attributes, you are half way done.

**Thijs** : They think that it&#39;s fine, we thought they would be protective. They were okay as they said that their core business is not managing these identities. I think it&#39;s already too difficult.

**Femke** : There are other problems and if you have an account on two universities, some students are enrolled in three unis because of one course together and I don&#39;t think it&#39;s the way it should be, it should be one identity or a number where you can recognize the user.

**Thijs** : That&#39;s one of the big challenges. We talked about eIDs and it looks like that this is a solution to our problem, so I use my password to enroll at university and I get a card from the university that opens the doors. You don&#39;t have to go with your password to the desk anymore, you just use your eID. It will be good for daily use. What are you trying to accomplish?

**Raluca** : So basically we are piloting ideas from ESA. They have attributes from different products. They are going to divide their system in communities and they should rely on the same authority. They were looking how everybody has done it. We have talked about the authority but it&#39;s still a matter if its fits. If you are talking about different technologies its aggregation as well and how you are going to manage but my idea is proxy.

_ALL AGREE_

I am curious as well how they did it from the technological point of view.

**Thijs** : As we already approve the concept, our federation has a big proxy in the middle, we are simply augmenting our proxy with it. It&#39;s only a proof concept that works and it&#39;s not production ready already or scalable. We currently have about 70 million login a year, they all pass through the proxy.

**Femke** : When it gets slower, what are we going to do?

**Thijs** : That&#39;s also one of the challenges, not all offers millions of logins, but have already aggregated attributes. Maybe it will be different later. Now if we look at ORCID, it will probably be 10 or 20 people per uni. When the server needs ORCID attributes, we will send the user to ORCID. So basically it&#39;s in the target service provider.

**Femke** : I think with approval of concept the user goes there and link the ORCID account but we don&#39;t think it&#39;s user friendly, so we hope that we can do it within the flow or use the same identifier.

**Thijs** : I think that if we have the same identifier, probably they already know each other. At least in our current scheme. If our attributes also know this, then there has already been interaction. The other alternative is that the user indicates who he is and that it&#39;s possible to pre-enroll people for access.

**Raluca** : If it can get the country from another part then why should I store it?

**Thijs** : We are trying to reduce the amount of information that we store.

**Slavek** : If you get different information from multiple sources, can you check it somehow with some algorithms?

**Thijs** : IDP is the most trusted source but if it doesn&#39;t have it, you can invert, if the attribute authority knows it and other doesn&#39;t, it can simply discard it.

**Femke** : Some attributes have more values or you can ask the user what attribute you want.

**Thijs** : In an ORCID case, if you have two ORCIDs, it doesn&#39;t make too much sense, as it&#39;s a single identifier which is multivalued.

**Raluca** : I think there will be many answers at ORCID.

**Thijs** : It&#39;s the first use case that we want to explore. We know SPs. It&#39;s a much bigger problem than ORCID. We have more use cases with ORCID, but we also have questions there. Some of our providers want the memberships so that they can use AOL to ask for memberships, but when someone has more than a hundred group memberships, and they should be available for the group providers. We also have to think about it.

**Slavek** : you are trying to implement a solution for some use cases, there are SPs and you can dial which group can access which SP and it provides specific information to the SPs.

**Thijs** : It of course has the drawback because the sides need to know about each other, and you know to know beforehand, so it&#39;s for some use cases but not all.

**Slavek** : it works quite well if they do know each other though.
