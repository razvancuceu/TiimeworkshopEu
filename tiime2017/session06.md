---
layout: page
title: TIIME 2017&#58; Session 6 Multi Factor/Strong Authentication (11:30/Room A10)
show_on_menu: no
menu: main
---

**Multi Factor/Strong Authentication (Pieter van der Meulen)**

The problem with OTP is that they have very little entropy, for example this makes birthday attacks very easy, if we run a program through all possible birthdays we will get a hit at some point so we don&#39;t look which identity we are stealing.

If there is a rate limit the problem can be resolved but it is not easy to implement this. For example a lot of users have the same passwords so they overlap if we than add another identifier let&#39;s say birthday it is very easy to iterate through all this numbers let&#39;s say 10.000, 100.000 times.

If we are talking about two factor authentication let&#39;s say over SMS the easiest way to steal the information would be with a malware which intercepts the message, but let&#39;s google one time passwords that can be iterated very easily.

Austria for example started with the Smart Card system but nobody used it outside the government, it is very problematic to make a new system that is going to be widely used. People have already started putting out apps in U2F (Fido alliance) but it still has not taken over, so basically it is only about time when it will become the standard.

If keys are stored on a phone the biggest problem is that the attack cannot be scaled, if someone steals the phone that person will only have access to that persons data it can&#39;t be widespread. There is always the option to make bigger stronger passwords but the problem with that is in more expensive hardware, software and usability, if the passwords get to big and to complicated they are not anymore usable for the end consumer.

It is really challenging with all the diversity and the offers to make a good list of ways how a user can authenticate. That is one of the reason that google authenticator is used so much. Recently google has stopped putting resources to google authenticator anymore. They stopped for the reason that they got to many questions from the users how to use the system, so they basically they didn&#39;t continue with the system just for the reason that people actually did not know how to use it, they had too many problems with it. Some people also have problems with a centralized IdP.

The user can chose what he or she likes. Today there are still many SMS authenticators but this is probably going to change. It is too expensive in the first place if we consider a few cents for just one authentication. Strong authentication is not just a federation protocol, some services can be centralized but some cannot. The problem lies in trust, can we trust those providers, and trust is based locally so if a trusted system is connected with another one users will trust in the system at that point. So the problem lies in system integration.
