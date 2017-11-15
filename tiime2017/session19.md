---
layout: page
title: TIIME 2017&#58; Session 19 SaToSa evolution (15:30/Room A11)
show_on_menu: no
menu: main
---


**SaToSa evolution (Heather Flanagan)**

The main repo: [https://github.com/SUNET/SATOSA](https://github.com/SUNET/SATOSA)

The docker image that SUNET is using: [https://github.com/SUNET/docker-satosa](https://github.com/SUNET/docker-satosa)

A repo to setup a local dev-environment with docker: [https://github.com/SUNET/satosa-developer](https://github.com/SUNET/satosa-developer)

SaToSa is a proxy-service.

**Agenda:**

Possible list of the microservices that VOs will need to make use of SaToSa. There is a list in order to use SATOSA. Take an identifier and query it on the server.

How do we do development? We lost the key contributor. We need to get organized. Who holds the keys?

Separation of configurational stuff in metadata: The proxy&#39;s IDP and SP metadata need to be configured from separate metadata feeds, which can be MDX.

Who is already deploying SaToSa and what?

**Who has SaToSA in production**

**Rainer** : Two upcoming projects. SAML to SAML conversation, in another one OIDC to SAML. Still researching which product to use.

**Chris** : Process of building a VO without a proxy. Not going to work. Going into deployment next month.

**Leif** : Multiple dependencies

**Niels** : Part of eduTEAMS  and InAcademia, both GEANT projects that need proxy functionality. (IDHub)

**Scott** : Evaluating proxies deploying for Chris &#39;infrastructure in NIH. We will likely always recommend proxies.

**Nick** : Likely using SaToSa as a proxy for Internet2 CoManage deployment.

**Ioannis** : Incorporating proxies in infrastructures. Project with Roland to make SaToSa OIDC Federation aware (whatever that means), also likes Python

SuNet: working on national services regarding identity management. Investment is very long-term. What should the long-term IPR support-situation look like? Typically SUNET stuff is under BSD license. (Roland&#39;s repository has the Apache2-Licence)

CLA (contributor license agreement): Whoever writes code for a project gives the owner of the project the right to use it

**SUNet support for the project?**

- --Has several core services that rely on pySAML (basis for SaToSa)
- --Investment is very long term
- --Would like to know what the IPR/maintenance/support situation should look like; Commons Conservatory is one option - Leif, Niels, and Roland to follow up

**Steps to get IPR into shape:**

- License of the pieces of the code varies; the bit 2 close BSD (?) license is used by whatever SUNet/NORDUnet pays for; all the code can be traced back to the copyright holder;
- Figure out who will hold the IPR (which legal entity holds the code);
- Identify copyright holders of existing code (and new code going forward) and have then sign a suitable CLA, as determined by the IPR holder;
- Relicense code in accordance with new IPR and CLAs, if needed.

**How do we develop?**

We don´t have lots of contributors. Maybe a review-session would be good if someone writes a lot of code. Can we get some common understanding where we want to move in this project? Some PR are stuck for a long time.

Can we use issue-threads? It would be better to have another place where you could discuss certain topics e.g. Security issues.

It would be nice to organize a hackathon.

It would be good to develop a culture of testing.

Distributed nature is good to enrichen the codebase but it sucks at a production model. Someone needs to be in charge. In SUNET exists already some responsibilities to ensure that things get done.

Maybe it would be good to have a switch to turn certain functionality of or on but have all of the functionality in the codebase of SUNET.

It should be able to check a list of identifiers where the IRDP should be sent. I want to configure SATOSA on what identifiers I want to get.

Now we have only unit test but we need more functional tests.

**How do we do development? How do we review each other&#39;s work, and accept code?**

- --We will have lots of contributors, there is a source code repo
- --Would like to add some mutual review
- --Would like to have someone coordinating the work, a place to record who is working on what; perhaps use GitHub issue threads to sort this out?
- --Hackathon!
- --Really need a benevolent dictator/product manager for this, to make sure the process is happening
- --SUNet needs a Travis set up
- --SUNet to create a developer mailing list - satosa-dev@lists.sunet.se

**Proposal** :

- Organize this request as issues in Github
- Each PR should target the different supported platforms.
- We should organize a developer meeting in spring in Stockholm. What kind of setup? Design-session or hackathon? It should be at least 2 days long. GEANT has funding for that. Need to identify who will work on making this happen. John will create a list of the subjects the meeting will be about.
- Micro services are right now integrated in the main codebase, which has to change. But they are already different entities. There are no reasons to build them in the main-codebase.
- What is a micro service for SaToSa? - It is a plug in which you put into the application so that it does a certain task. E.g. statistic service, which gathers different kinds of statistics.
- We should pull micro services out to a contributor-directory. But there are many project who fail at this task.
- We should have a public Travis setup for integration. You should use Docker in Travis to test for different target platforms.
- We need the functionality so that a simple make-command triggers all kinds of python-modules.
- Mailing-list is missing to drop some of the ideas? But maybe GitHub is enough.
- Need ability to take combinations of identifiers to create a key.
- Need for some SP to create a custom name-ID based on the identifier. The existing one is not quite flexible.

**Possible list of micro services that VOs will need to make the most use of SaToSa?**

- --Organize these as GitHub issues and label them as improvements; we need to get out of the business of having the microservices included in the core code base
- --Existing examples: consent service presents users with a consent screen; account linking; statistics gathering; LDAP as a source of attributes (they should all be moved to a contrib repo)
- --People need to check for an ordered list of identifiers, and if criteria aren&#39;t met, redirect users to an external service that will display a project-specific error to a user (Scott to write that up as an improvement)
- --OAUTH backend module, to leverage ORCID, GitHub, etc, as providers of identity
- --There are several more; Scott will pull out of the NIH requirements list and post them

**Looking at the separation of config and GUI?**

- Niels will right out some issues as a feature request
