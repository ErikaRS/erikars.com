---
author: ErikaRS
description: 'Originally published on Medium on December 29, 2018.  Background: I
  spent about 7 years working on one of the backends that powered, among other things,
  part of...'
pubDate: '2018-12-29'
tags:
- On ErikaRS' Mind
title: Hurray, hurray, we did okay!
---

*Originally published on Medium on December 29, 2018.*

*Background: I spent about 7 years working on one of the backends that powered, among other things, part of Google+. Much of that time (5 years) I owned a data migration to deal with technical debt that came out of the original implementation. Although G+ is not the only source of these musings, its impending turndown was top of mind as I wrote. That said, I have no insight into the actual turndown of G+ and have been off of that team for 2 years now.*

Let’s take a break from our regularly scheduled musings on ethics and society to think about software engineering.

We all know that we should design maintainable systems. But what does that mean? For non-mission critical consumer products, here’s one perspective: **Design for mild success.**

If we start with the assumption that our product is going to be wildly successful, we will likely commit at least one of over-engineering or taking too many shortcuts. When we over-engineer, we build a system that is ready to enable the features we imagine now but can’t build yet. When we take shortcuts, we build things in a way that works today but relies on a complex and brittle set of assumptions. Seemingly opposites, a common assumption behind both of these sins of software engineering is that there will be time and resources invested into the code later.

But chances are, the product will not be wildly successful. Maybe it will be a complete failure and we can delete the whole thing (although even a good cleanup can take a long time — that 5-year data migration I mentioned took another two years to clean-up the old system).

If the product manages not to fail, it will most likely be *mildly* successful. We will have created something with real value in limited circumstances or for a small set of users. We won’t want to kill the product, but we will have a hard time justifying an engineering team to clean up those hacks and implement all of those good ideas we planned for (plus, we were wrong about what users would want).

Now those over-engineered classes and workaround hacks start to call in their debt. Products are only worth keeping as long as the benefits (to us and our users) outweigh the costs. Sadly, since our mildly successful system was engineered to require an unjustifiable ongoing investment, the cost does not justify the benefit.

Where does that leave us? With a useful and valued product that is a drag on our team. We have a system that’s disheartening to work on because whoever ends up paying the maintenance cost has to run just to stay in place given the technical debt they were burdened with.

Now we have a choice: keep paying the cost of maintenance or turn down the product and pay the cost in the goodwill of your users. You cannot escape the payment.

So remember to engineer for mild success. Design a system that is easy to maintain and solves the problems you need to solve today. Generalize when it becomes a net saving (even though it will be incrementally more expensive). Be specific, but not hacky. And remember, you always pay a price for tech debt. Like with debt in the real economy, the question is only whether or not the overall growth reduces the relative cost of the payment.
