---
layout: page
title:  Session 28 &lt;IDP category types&gt; (13:30/Room A06)
show_on_menu: no
menu: main
---


**IDP category types (Niels van Dijk)**

Especially in eduGain, there are large piles of IDPs, about 2500, as you are probably aware the fact that you are in eduGain it doesn&#39;t mean that you are in academic IP. A Dutch IDP would always be an academic IDP. You can have a complete mesh of types of IDPs.

For most scenarios that&#39;s fine and you want whatever goes but there are several scenarios where it matters. It&#39;s the technical way that I propose this to label the entities in the metadata. The definition was carefully crafted. It turned out very differently for US and EU, of what academic entails. That became even worse when we found out that there isn&#39;t a definition of academic in the world at all.

Can we still use this concept of labelling IDPs but come up with a less controversial way of labelling them? There are a couple of ways that we have in mind. Together with Nicole I had a quick discussion on this topic. Let&#39;s run through the examples that have value.

One of the entities that seems an easy one is Self-signup, which would be an IDP that has a self-sign process for getting the members on board. There are 5 in eduGain, mostly coming from UK. United IDP would follow but it&#39;s not using sign up as user and password. If you are running a self-signup, you would want to be noted as a guest IDP.

**Leif** : There is a term. LDAP of last resort, a group that has been writing up a list of requirements that a LDAP must fulfill. We could take that and say that people who self-label like this have to fulfill this requirement.

**Klaas** : There are also verified users, the IDP category can&#39;t be put on that.

**Niels** : You are talking about the proxy right now. The solution that we have is one proxy but in the metadata all IDPs are different entities.

**Leif** : Entity is not a proxy, this isn&#39;t a proxy issue. I don&#39;t think that there is a proxy problem.

**Niels** : In technical way is to present two metadata instead of one. That is a very simple technical solution.

**Klaas** : It&#39;s on a wrong semantic level, not on the IDP level because you have to force the IDPs. Express it in attributes for what you need!

**Leif** : Usually you do both as the tagging is something that the federation operator controls. So sometimes you have some important attributes and the fact that you allow is the combination of them that you rely on.

**Klaas** : Yes but if you believe that we are going into a world where your identity is a back of attributes asserted by different entities, it gets complicated.

L: This is not about attributes though. They can be distinguished.

**Niels** : \*writes K12 on the board\* These exist in multiple federations and multiple are in eduGain as well.

\*writes above K12\* We are not stating what that is but it&#39;s not K12.

What about the China common values? It&#39;s an attribute value but it does the same thing.

**K** : Why not sticking it in the attribute?

**N** : You are missing the mark like this though.

**Rainer** : If the entity category can deliver it then it should be possible for a specific person as well.

**N** : We must make sure that if we do that that they are aligned. The Stockholm organization was kicked out as it was defined on a per country base.

**Leif** : its not a bad idea, it&#39;s very much more than academic.

**Ioannis** : My question is would K12 be accepted?

**Leif** : It&#39;s not really, it&#39;s entirely opposite.

**R**** :** Self signup needs a better specification. It is just the standalone way to create an account, right? - Yes.

**N** : Public library, anyone?

**K**** :** These are the walking users right?

You get an ID card and with it you can ask for books at the library so there is an agreement.

You have to have VPN privileges.

N: What is confusing is that if you are a student or a staff or a faculty, then you have to be a member as well, but it doesn&#39;t say that the reverse is true.HL7 is the thing that defines it IHE. There are thousands and thousands of pages of it.

**Ioannis** : Do we actually need multiple categories? I think that one covers most of the use cases.

**N** : In the Netherlands the hospitals are independent IDPs.

**I** : there are different IDPs, there is just not a standalone entity that is affiliated with the university.

**N**** :** K12? What we should do is to find a UNESCO definition. \*writes UNESCO? On the board\*

**N** : \*writes value?? On the board\*

Are there any not in my list that should be there? Any difficult use cases? \*writes government, other and VO on the board\*

**Jan** : Or maybe just &quot;other&quot;? We have 5 categories, academy of science, libraries, hospitals and then other. In other there is csnet, also bbmri based in Austria and it&#39;s practically a category for anyone who doesn&#39;t fit in the categories previously mentioned.

**N**** :** I know that the umbrella ID is moving to the UK federation.

**N**** :** It would be very wise to state in the whole document &quot;Its always for the local federation to decide&quot;.

**Leif** : I honestly think that &quot;other&quot; is not a good category. We are talking stuff that can be determined there, not other.

**Rainer** : you can mark them as uncategorized which gives the impression that they need to do something in order to get categorized.
