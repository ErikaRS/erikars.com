---
author: ErikaRS
description: "I recently finished reading\_Why Greatness Cannot Be Planned(https://www.goodreads.com/book/show/25670869-why-greatness-cannot-be-planned).\
  \ The basic thesis is t..."
pubDate: '2021-03-27'
tags:
- On ErikaRS' Mind
title: The Tyranny of the Objective
---

I recently finished reading [*Why Greatness Cannot Be Planned*](https://www.goodreads.com/book/show/25670869-why-greatness-cannot-be-planned). The basic thesis is that setting objectives is futile for significant innovation. Objectives can be useful for incremental improvements, but for innovation, we do not know that the path that progress requires. Measuring incremental improvements against the final goal is likely to result in the pursuit of dead ends that seem like they should be moving closer but which are actually missing a vital stepping stone. The vital stepping stones usually require going in a non-obvious direction. You can read more in [my goodreads review](https://www.goodreads.com/review/show/3547109271).

As a colleague noted in a book club discussion of this book, the argument presented in the book is somewhat lacking. It focuses overly much on the particular path that was used to get to some interesting end. E.g., “Computers are great! They needed vacuum tubes. Who would have thought *that* when first trying to invent computers?” They observe that this assumes that reaching a particular objective is fully path dependent: there is only one particular way to get there from here. In practice, there are likely to be multiple ways to get to a particular end. Vacuum tubes may have been how we first got to scalable computation, but they likely were not the only path to silicon. Bicycles may have been one path to commercial flight, but that doesn’t mean they’re the only one.

A better argument for the futility of objectives to reach ambitious objectives is one that pulls from [*The Tyranny of the Ideal*](https://www.goodreads.com/book/show/27311863-the-tyranny-of-the-ideal) ([my review](https://www.goodreads.com/review/show/2730568557)). In that book Gerald Gaus develops the idea that targeting an ideal is a futile effort. That book describes the ideals in the context of the landscape of justice. I will generalize to talk about objectives more generally.

A [fitness landscape](https://en.wikipedia.org/wiki/Fitness_landscape) provides a way of thinking about how well different agents are doing relative to a particular fitness function. The fitness is the “height” of point in the landscape while the other dimensions of the space represent how similar two points in that landscape are to each other (where closer implies more similarity). In biological evolution, the fitness function is reproductive success and the units being assessed for similarity are genotypes. Fitness landscapes are usually *visualized* in two or three dimensions. Reality is, of course, often has many more dimensions.

*A rugged fitness landscape ([source](https://en.wikipedia.org/wiki/Fitness_landscape)*)

The thing that makes a fitness landscape interesting is that two points that are close to each other may not have similar fitness. For example, a small mutation can cause an organism to die, reducing its fitness to zero.

Gaus differentiates between fitness landscapes that are smooth, rugged, and random. These are a spectrum more than distinct types, but I will describe them as types for simplicity.

In a smooth fitness landscape, following the gradient of increasing fitness will always lead you to a global maxima of fitness. In the diagram above, if the fitness landscape consisted only of peak B, it would be smooth.

In a rugged fitness landscape, following the gradient of the fitness function will generally lead to greater fitness. However, a particular position may be a local maxima—there is no more “up” to follow locally—yet globally there are better places to be. The diagram above depicts a rugged fitness landscape. For the red ball, both A and B represent increased fitness, but they do not achieve the same maximum.

In a random fitness landscape, there is no predictability. A step one direction may dramatically increase fitness while the next step may plunge it to nothing. There is nothing to rely upon. It’s hard to survive in a random landscape. Gaus notes that the justice landscape is rugged, like the landscape of many other complex systems.

(Note that a fitness landscape need not be static static. They can be dynamic or, to use the more poetic term, dancing (coined, I believe, by Scott Page). A dancing landscape is one that changes over time. It can change in response to external forces or it can change in response to internal forces, such as when plants evolve to be more attractive to pollinators.)

What does this have to do with objectives? Objectives specify a destination we are trying to get too. In the thinking of *Why Greatness Cannot Be Planned*, objectives are often used to derive an *objective function* where the direction we explore is determined by measuring the distance between where we currently are and the objective. Distance from the objective becomes our fitness function.

The thesis of *Why Greatness Cannot Be Planned* is that using objectives this way is doomed to failure because charting a course straight for an objective means that you miss out on critical stepping stones that may seem, at first, to take you further from the objective. The world of innovation is a rugged landscape. Following what looks like the obvious direction may land you at a dead end, a local maxima from which no more progress can be made.

So that addresses one of the objections to objectives made in *Why Greatness Cannot Be Planned*: objective functions are bad for innovation because innovation occurs in a rugged fitness landscape.

But that does not explain why Stanley and Lehman, the authors of *Why Greatness Cannot Be Planned* reject objectives as firmly as they do. You can have an *objective* without using it as an *objective function*. While I think they take the rejection of objectives a bit far, we can delve further into Gaus’ work to see why there is a seed of truth in their rejection of objectives.

Gradient ascent—simply following the path up—is not the only way to move through the search space. We can look further afield. If we can see the whole landscape, we can figure out which direction to go even if simply maximizing the objective function will lead us down the wrong path. But can we do this? Stanley and Lehman use a metaphor of using stepping stones to navigate across a foggy lake. Gaus states this idea more precisely. He defines a *neighborhood* as the region in a fitness landscape that we can make reasonably well founded predictions about. Regions in our neighborhood represent small deltas from our current world. Like in the stepping stones metaphor, as we move through this rugged landscape, we learn more and revise our vision of where we can go.

We can only chart a reliable path to an objective when it’s within our neighborhood of knowledge. Because of this fogginess, if the global maxima is not in our neighborhood, then we have no idea where it is. It might be along the current direction of ascent or it might be in a completely different direction. Of course, the neighborhood is really a continuum, not a binary. Thus, there’s not really a strict cutoff of areas where objectives are or are not useful. Rather, the lesson to take away is that the further an objective is from your current knowledge base, the less able you are to navigate there. This is true even when the objective itself can be precisely stated.

Inverting this, we can understand the situations where objectives are useful. When everything we need to know to reach the objective is within our neighborhood of knowledge, then an objective can useful. The objective function still isn’t useful; we may still need to go down before we go up the right hill. Rather, because the objective is nearby, we can chart reliable turn-by-turn directions to our destination. And if the objective is just outside our neighborhood of knowledge, we can do work to expand our neighborhood of knowledge (e.g., building MVPs) to increase the feasibility of being able to meet our objectives.

So, to sum up, in *Why Greatness Cannot Be Planned* Stanley and Lehman argue that objectives are misleading because the path from here to there may require some unforeseeable side quests. Looking at this through the lens Gaus develops in *The Tyranny of the Ideal* we can make this more precise: because innovation is a rugged landscape, using distance from an objective as a objective function gives little guidance about which way to go. Furthermore, the limitation of our knowledge to local neighborhoods—the fog between stepping stones—means that we cannot reliably chart out a course even if we are willing to deviate from a more seemingly direct path.
