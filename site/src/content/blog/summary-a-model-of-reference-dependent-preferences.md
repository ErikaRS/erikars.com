---
author: ErikaRS
description: "Originally published on Medium on July 13, 2018.  Source(https://pixabay.com/en/black-coffee-coffee-cup-desk-drink-2847957/)\
  \  The paper \u201CA Model of Reference-De..."
pubDate: '2018-07-13'
tags:
- On ErikaRS' Mind
title: 'Summary: A Model of Reference-Dependent Preferences'
---

*Originally published on Medium on July 13, 2018.*

[Source](https://pixabay.com/en/black-coffee-coffee-cup-desk-drink-2847957/)

The paper “A Model of Reference-Dependent Preferences” by Botond Koszegi and Matthew Rabin discusses the role of expectations in determining economic utility. By explicitly modeling expectations, various “irrational” human behaviors can be explained. I read the [freely available draft](http://webspace.pugetsound.edu/facultypages/gmilam/courses/econ291/readings/01-KozegiRabin.pdf); this is the purchase-requiring [published version](https://academic.oup.com/qje/article-abstract/121/4/1133/1855210?redirectedFrom=fulltext). What follows is a detailed but non-technical summary.

Traditional economic models evaluate outcomes based on consumption utility. In this paper, the authors model utility as a function of both the consumption utility of an outcome and the utility of that outcome relative to the *expectations* of the actor. The authors assume the expectations are rational: they are an accurate probabilistic representation of both the possible outcomes and the utility the actor would derive from each outcome. Even under these strict assumptions, the model predicts various experimental outcomes better than models which take just consumption utility into account and better than models which assume that reference based utility is relative to the status quo rather than expectations.

More concretely, the utility of an outcome is defined as the sum of the actual consumption utility of that outcome and the gain-loss utility of that outcome. The gain-loss utility is the probability weighed sum over all expectations of a utility function applied to the difference between the consumption utilities of the actual outcome and the expectation.

For example, if I expected

- $0 with 25% probability
- $50 with 25% probability
- $100 dollars with 50% probability

and I won $50, my utility, translated into dollars, would be

- $50 [consumption] + (0.25($50-$0) + 0.25($50-$50) + 0.50($50-$100)) [gain-loss]   
  = $50 + $12.5 + $0 + -$25   
  = $37.50.

In other words, the utility of the $50 would be decreased because I had a strong expectation of winning $100. If, on the other hand, I had more strongly expected to win nothing, than the utility of the $50 would be increased by my sense of gain relative to my expectation.

My example above assumed a linear gain-loss utility function: the utility of a gain relative expectations is equal to the utility of an equal sized loss relative to expectations. In practice, the authors build loss expectation into their model. They assume that the utility function has negative utility for losses greater than the positive utility of equally sized gains. They also assume, however, that this effect is more pronounced for smaller losses/gains relative to expectations and that for larger losses and gains, the relative consumption utilities dominate any loss aversion. Thus, this model does not explain loss aversion.

Although the authors do not discuss this, I believe this model puts loss aversion on a more solid footing than it traditionally sits on. This model does not say that a loss is worse than a gain. It says that a loss *relative to your expectations* is worse than a gain relative to those expectations. In other words, it says that not having your expectations met is worse than having your expectations exceeded. This seems more psychologically defensible than saying that losses are, axiomatically, worse than gains.

Much of the paper is devoted to discussing the consequences of this model. In deterministic environments, the consumption utility and actual utility will always match because the gain-loss factor will always be (1.0\*0) — complete certainty that there is no difference between the outcome and the expectation. However, in non-deterministic environments, consumption utility can vary from actual utility.

Another interesting consequence is that having expectations can leave us worse off than having no expectations. Someone with no expectations will always see any gain as positive. Someone with expectations (that they might have gained more) may see a gain as a loss. (Of course, they may also see a loss as a gain, so it’s all relative.)

Although the authors do not discuss it, this is applicable to situations like the ultimatum game. In this experiment, the proposer gets some amount of money and they offer some to a responder. If the responder takes the offer, they both get the money. If the responder doesn’t accept, neither gets the money. Since the alternative is nothing, a traditional economic model would predict that the responder would take any amount greater than zero. In practice, responders want much more fair amounts. Why they expect this has been discussed at length, but the relevance to this paper is that the responder has an expectation that they will get more and evaluate the outcomes based on this expectation.

This model also predicts a status quo bias. In the face of certainty, the model predicts that people are always willing to abandon their current reference point for an alternative that has a probabilistic expectation that is even marginally better. However, in the face of uncertainty, the expectation of the status quo is that you will continue having what you had already and the chance of ending up either worse off or better will be weighed against that expectation. For example, compare having $50 with betting that on a 75% chance of getting nothing and a 25% chance of getting $204. According to traditional expectations, (0.75\*$0 + 0.25\*$204) = $51 and so the bet is worth taking with a gain of $1. However, in a world where outcomes are evaluated relative to expectations and losses weigh more than gains (say, gains are worth only 90% of a loss), the expected gain comes out to

- (0.75($0-$50) + 0.25($204-$50)0.90)
- = -$37.5 + $34.65
- = -$2.85

and so the bet is not worth taking.

The endowment effect is when someone seems to ascribe more value to something because they own it. The canonical experimental setup is that someone is asked how much they would pay for something, like a mug (hence the photo), then given a mug, then asked how much they would sell it for. Often, people set a higher price for selling something they have been given than they had set for buying. However, this effect is not consistent; some experimental setups do not show this effect. The authors argue that when someone is given an object, they start forming expectations which are based on their continued possession of that object. If they are given the object with the expectation that they’ll be selling it, their expectations will shift and their valuation will not show the endowment effect.

This model also explains how people may come to spend more on an item than the consumption value they will get from it. Essentially, once you expect to get something, that feeds back into how much you are willing to pay for it because the value of the item to you is not just the consumption utility of acquiring the item, it is also how much you are willing to pay to avoid the missed expectation of not getting the item. The more you expect to get the item — the greater the loss from not getting it — the more you are willing to pay.

An odd variant of this is that the consumer’s demand for an item based on price is not, as classically assumed, a function based on only the price. Changing the price changes rational expectations about the price at which the object can be acquired which shifts the demand. Price and demand is a feedback loop, not a static function. Concretely, if a consumer is willing to buy shoes at price $X and then sees that they are on sale for 50% off, they may no longer be willing to buy the shoes at price $X. Alternately, a consumer may not have been willing to buy shoes at price $Y, but if they see that $Y is actually 50% off the full price, their expectations shift and they may see buying the shoes at $Y as a gain… as anyone who has ever bought something “because it was on sale” knows.

Another example the authors work through is whether or not increased wages decrease willingness to work. Their model predicts that increased wages will decrease someone’s willingness to work if those increased wages meet the worker’s wage expectations more quickly but not if it causes them to change their expectations. To put it another way, someone who expected to earn $200 in a day but instead earned it in half a day will not be inclined to work more. However, if they expected the day to be busy and adjusted their expectations accordingly — say, to $400 for the day — then they will be willing to work more. Thus, it is not higher wages that affect willingness to work. It is actual wages relative to expected wages.

Although this is a simplified model of how expectations affect utility, building expectations into the economic model still does a lot to make the modeled outcomes better reflect reality. In my view, this further supports the idea that when humans act “irrationally” relative to behavioral models, it is much more likely that the models are missing critical factors than that humans are truly as lacking in rationality as is sometimes implied.
