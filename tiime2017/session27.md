---
layout: page
title:  Session 27 &lt;Push-MDQ&gt; (11:30/Plenary)
show_on_menu: no
menu: main
---


**Push-MDQ  (Leif Johansson)**

**Problem statement**

Consider the following aggregator setup: A provides an upstream to B which provides downstreams to C and D. Changes at A take X hours to reach B and even more hours to reach C and D. We need this to go faster. One approach is to just update more often but this is wasteful and scales poorly. Instead we propose a push-based notification mechanism for metadata changes based on ATOM and PuSH

**Strawman approach**

- Each endpoint at an aggregator supporting PMDQ indicates this by permitting content negotiation for application/atom+xml in addition of the default application/samlmetadata+xml
- When requesting /foo with Content-Type: application/atom+xml the aggregator will return the changes associated with /foo (subject to some reasonable TTL based on validUntil etc.).
- The /entities change-feed is the &quot;all in&quot; change feed - contains all changes
- Each object in the ATOM feed should contain a reference to signed metadata that is at least as fresh as the one that was current at the time of the change.
- This &#39;change feed&#39; could also implement PuSH (pubsubhubbub) in the normal way
- An aggregator could implement its own PuSH hub or use an existing hub (superfeedr etc.)

This leads to the following behavior associated with the example

- Aggregator B fetches the ATOM change feed associated with /upstream-to-B and parses the Link header to find the pubsubhubbub H
- B registers as a consumer of  http://A/upstream-to-B at H
- When something happens at aggregator A to the entities in /upstream-to-B the aggregator updates the /upstream-to-B ATOM change feed and notifies H
- H notifies B which can download the change feed and fetch metadata.
