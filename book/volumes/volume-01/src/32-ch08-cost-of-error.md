# The Cost of Being Wrong

Every model makes mistakes, and every project eventually has to answer a question that sounds simple and is not: how wrong is acceptable?

The question is not answered by accuracy, because accuracy treats all mistakes as equal. In most real settings they are not equal at all. A smoke alarm that wakes you at three in the morning for burnt toast is an annoyance. A smoke alarm that stays silent during a fire is a catastrophe. Any measure that scores those two errors the same has misunderstood the job.

So before a model is trained, somebody has to decide what a mistake costs. That decision is not technical, and pretending otherwise is how projects end up optimising the wrong thing with great precision.

## Two Ways to Punish a Mistake

Start with a single prediction. A robot arm predicts a reach of 0.52 m; the true distance is 0.50 m. The error is 0.02 m.

If you add raw errors across many cases, positive and negative cancel. A miss of +0.3 m and a miss of −0.3 m add to zero, and the model looks perfect. So the sign has to go, and there are two common ways to remove it.

**Squaring.** The squared error here is 0.0004 m². Squaring has a second effect that matters more than the first: it punishes large misses much harder than small ones. A miss of 0.1 m costs 0.01 in squared units. A miss of 0.3 m costs 0.09 — nine times the cost for three times the error.

Averaging the squared errors across the data gives the **mean squared error**, usually written MSE. Taking its square root gives the **root mean squared error**, RMSE, which is back in the original units and therefore readable.

**Absolute value.** The absolute error is 0.02 m, with no sign and no squaring. Averaging gives the **mean absolute error**, MAE. Every miss counts in proportion to its size; nothing is amplified.

Take three errors: 0.02 m, 0.04 m and 0.10 m.

- Squared: 0.0004, 0.0016 and 0.01. They sum to 0.012 m². Divide by three: MSE is 0.004 m². The square root is 0.063 m.
- Absolute: 0.02, 0.04 and 0.10 sum to 0.16. Divide by three: MAE is 0.053 m.

Both are correct. They answer slightly different questions. RMSE is dominated by the worst cases; MAE describes the typical case.

## The Tail Is the Story

Change one number and the difference becomes dramatic. Suppose the errors are 0.02, 0.04 and 0.30 m — perhaps a sensor glitch, or a genuine event.

- Squared: 0.0004, 0.0016 and 0.09. MSE is 0.0307 m², RMSE is 0.175 m.
- Absolute: 0.02, 0.04 and 0.30. MAE is 0.12 m.

The outlier now drives RMSE almost entirely. A model trained to minimise MSE will bend itself towards that case, because that is where the punishment is concentrated. A model trained on MAE will accept a little more error everywhere in exchange for not chasing the outlier.

Which is right? It depends on whether the outlier is noise or signal. If the 0.30 m came from a faulty sensor, MAE is the better choice, because you do not want a glitch to reshape the model. If it came from a person stepping into the robot's path, you want the model to care very much, and MSE is the better choice.

This is the sentence to carry out of the chapter: **the way you score a mistake is how you tell the model what you care about.** It is not a detail added at the end. It is a statement of values, written in arithmetic.

## Of the Flagged and of the Real

Classification problems have a different shape of error, and the vocabulary is worth knowing precisely, because it is used carelessly in almost every discussion of these systems.

Take a test that looks for cracks in welds. On a batch of 100 welds, 10 are cracked. The system flags 14 as cracked. Of those 14, 8 really are cracked, and 6 are sound. It misses 2 cracked welds entirely.

|  | Flagged | Not flagged |
|---|---|---|
| Actually cracked (10) | 8 | 2 |
| Actually sound (90) | 6 | 84 |

Accuracy is (8 + 84) / 100, or 92%. That number is true and nearly useless, because it hides the two different failures.

**Precision** asks: of the ones we flagged, how many were real? Here, 8 / 14 = 57%.

**Recall** asks: of the real ones, how many did we catch? Here, 8 / 10 = 80%.

A system with 57% precision sends six sound welds to inspection for every eight real cracks. An inspector who has to re-check six good parts for every eight bad ones will, quite reasonably, stop trusting the system within a month. And a recall of 80% means one cracked weld in five leaves the factory.

Neither number alone describes the system. Precision without recall is a system that flags almost nothing and is right when it does. Recall without precision is a system that flags everything. The pair together, with the costs attached, is a description.

## Choosing the Threshold from Costs

A classifier does not usually output a yes or a no. It outputs a probability, and a threshold turns that into a decision. Moving the threshold trades one error for the other, and the trade should be made with costs, not with taste.

Suppose a false alarm costs 20 units — an unnecessary inspection — and a missed crack costs 500 units, because a cracked weld that fails in service is a disaster. The system scores 100 welds.

At the current threshold it catches 8 of 10 cracks and raises 6 false alarms:

> Expected cost = 2 misses × 500 + 6 false alarms × 20 = 1,000 + 120 = 1,120 units

Now lower the threshold so that it catches all 10 cracks but raises 30 false alarms:

> Expected cost = 0 × 500 + 30 × 20 = 600 units

The second setting is cheaper, by nearly half, even though its precision is far worse and its accuracy is lower. Anyone judging by accuracy would have chosen the first. Anyone judging by the cost of being wrong would choose the second, and would be right.

That is the entire argument for cost-sensitive evaluation, done in four lines. It also explains a political fact about real projects: the person who defines the costs has more influence over the system's behaviour than the person who writes the code.

## When You Cannot Agree on Costs

Sometimes the costs are genuinely contested. A hospital screening programme may find that a false alarm costs a patient weeks of anxiety and a follow-up procedure, while a missed case costs a life, and no committee can agree on the exchange rate.

In that situation, do not invent a number and hide it inside the model. Instead, produce the curve. Report the recall achieved at every false alarm rate, and let the clinical team choose a point on it. The technical contribution is the curve. The choice is theirs, and it should be visible, recorded and revisited.

The worst outcome is a system whose threshold was set by an engineer's intuition, deployed for years, and never examined. The second worst is a system tuned to maximise accuracy on a dataset whose class balance happens to reward doing nothing.

## Problems

1. Five reach predictions for a robot arm are 1.02, 0.97, 1.10, 0.95 and 1.30 m. The true distance is 1.00 m. Compute the MSE, the RMSE and the MAE by hand.

2. Remove the 1.30 m case and compute all three again. Which measure changed most, and why?

3. A defect detector scores 100 parts: 12 defective, 9 caught, 15 flagged. Build the confusion matrix and compute accuracy, precision and recall. Write two sentences a production manager would find useful, and two they would find misleading.

4. False alarms cost 10 units; a missed defect costs 300. Compute the expected cost at a threshold that catches 9 of 12 with 15 flags, and at one that catches 12 of 12 with 40 flags. Which would you deploy, and what would you tell the manager who preferred the other?

5. Name one decision in your own life where the two kinds of mistake are clearly unequal in cost. Write the ratio honestly, as a number, and then decide what evidence you would need before acting.
