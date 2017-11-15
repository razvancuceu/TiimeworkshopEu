---
layout: page
title: TIIME 2017&#58;  Session 15 Second Factor as a Service (14:15/Room A11)
show_on_menu: no
menu: main
---


**Second Factor as a Service (Niels van Dijk)**

Niels: Exploring possible scenarios for using 2nd factor as-a service (2FaaS).

If you leave the service to the service-provider, we will get like 20 implementations. It is quite annoying for the end-user, because the user ends up with many different tokens.

If you leave it to the IDPs, it won&#39;t happen when only a few users of the IdP need it.

So centrally makes sense. A central proxy is a solution. But then you have central proxy it is more difficult to scale. And when multiple communities start offering 2FaaS then you end up with multiple proxies.

One of the biggest challenge to do 2nd-factor collaborations you have to fit the identity.

Scalability is also a main problem in 2nd-factor.

**How could we apply federation to 2nd-factor?**

**Scenario 1**** :**

**Second-factor-only-IdP**

We create a separate IDP that authenticates just the 2nd factor of the user. The flow is that end users first authenticate at their &quot;normal/home/1st factor&quot; IDP and then register their get their 2nd factor at the central 2nd factor IdP. The 2nd factor IDP has a database that links the identifier of the user at their normal IDP to the identifier of the second factor.  That is where the collaborative organization comes in. We provide (centrally) a workflow to let other users vet the association between the 1st and the 2nd factor.

IDP has a workflow so that end-user can come in and register and others can link the information.  The registration-workflow is behind an IDP so that the user can register with his own Home-IdP.

IDP does not have to store private information, just an identifier.

This scenario is already usable with the current software-stack (= OpenConext Stepup [https://github.com/OpenConext/Stepup-Deploy](https://github.com/OpenConext/Stepup-Deploy))

What about hiding this workflow behind a SP?

That is technically exactly what is happening.

IDP is also an Attribute Authority (AA) and SP can request them. You can build in the same function without an AA.

As we are storing information anyway it would be useful for SP to discover the fact that a 2nd-factor for a user is already stored.

------------------

|1st factor IdPs|

------------------

      ------------------

      |DB linking      |

      |1st F to 2nd F|

      ------------------

          |

          |

------------------              -----

|2nd factor IdP|   -------  | SP |

------------------              ------

|  workflow      |

| Vetting          |

|  Registration|

Now a flow-diagram is shown (cf. [https://wiki.geant.org/display/gn42jra3/Identity+Assurance+Service+Attribute+Authority](https://wiki.geant.org/display/gn42jra3/Identity+Assurance+Service+Attribute+Authority)).

End user tries to authenticate. The Home IdP releases the attributes, the other SP (e.g. SP1) checks the attribute and if there is a 2F-LoA-Attribute, then the Access is granted.

If not, the AA tries to get more information. The SP1 fires a workflow where the user shall create a 2nd factor (SP2). Finally SP1 detects a 2nd-factor for the user and it gives access.

Only difference to the first scenario described above is that this one misses user interaction.

Why does it matter if the user has 2nd factor or not? SP actually require it. That is an authorization decision. The actual 2F authentication is not shown.

Why is the AA actually in there? Just verify that the user is allowed to do this operation?

The basic idea is to help both IDPs and Home-Organizations which are not able to implement a 2nd-factor-authentication-workflow.

The AA-Query is running in background, the user does not get the chance to authenticate himself.

Is the 2nd-IDP standalone? The idea is to have it central.
