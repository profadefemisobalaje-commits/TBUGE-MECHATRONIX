# From a Number to a Probability

The previous chapter predicted a temperature. This one predicts whether a part will fail, a customer will leave, or a patient has a condition. The output is a category, and the natural way to produce a category is to produce a probability and then apply a threshold.

That move — from score to probability to decision — is where most of the practical difficulty of classification lives. A model that outputs 0.73 has not said "yes". It has said something that a human, a policy or a cost calculation must convert into an action.

## Why Not Just Use a Line?

You could fit a straight line to a yes/no outcome, treating "yes" as 1 and "no" as 0, and many people have. It produces predictions like 1.4 and −0.3, which are not probabilities, and it treats a case near the boundary as no more uncertain than a case far from it.

The better approach keeps the linear part but passes it through a curve that squeezes any number into the range between 0 and 1. The curve is the **logistic function**:

> probability = 1 / (1 + e^(−z))

where z is the linear score, built from the inputs exactly as in regression. Large positive z gives a probability near 1. Large negative z gives a probability near 0. z equal to zero gives exactly 0.5.

The quantity z is called the **log-odds**, and it has a clean interpretation: it is the logarithm of the ratio between the probability of the event and the probability of no event. A log-odds of zero means even chances. A log-odds of 1 means about 2.7 to 1 in favour.

| Linear score z | Probability | Odds |
|---|---|---|
| −3 | 0.05 | 1 to 19 against |
| −2 | 0.12 | 1 to 7.4 against |
| −1 | 0.27 | 1 to 2.7 against |
| 0 | 0.50 | Even |
| 1 | 0.73 | 2.7 to 1 in favour |
| 2 | 0.88 | 7.4 to 1 in favour |
| 3 | 0.95 | 19 to 1 in favour |

The table is worth internalising, because it tells you how a logistic model behaves: most of the action happens in a narrow band around zero, and the tails saturate. A large change in a feature that is already pushing the score to 3 will barely move the probability, which is why interpreting coefficients as "effect sizes" needs care.

## A Small Model, Worked

Suppose a maintenance model uses two inputs: vibration in mm/s and temperature in °C. Fit the parameters, and suppose the result is

> z = −8.0 + 1.4 × vibration + 0.06 × temperature

Take a pump reading 2.5 mm/s and 50 °C:

> z = −8.0 + 3.5 + 3.0 = −1.5

The probability is 1 / (1 + e^1.5) = 1 / (1 + 4.48) = 0.18. The model says an 18% chance of failure within the month.

Now take a pump at 3.5 mm/s and 55 °C:

> z = −8.0 + 4.9 + 3.3 = 0.2

The probability is 1 / (1 + e^−0.2) = 0.55. A one-unit change in vibration and a five-degree change in temperature moved the probability from 18% to 55%.

This sensitivity is a property of the model, not of the pumps, and it is a warning. If the true relationship were gentler, the fitted model would still produce a dramatic swing around the boundary, and decisions built on it would be brittle. The coefficients are only as good as the data, and the data is often thirty examples.

## How the Parameters Are Found

Linear regression has a formula: the least-squares solution can be written down in one line. Logistic regression does not, and the parameters are found by search.

The loss is cross-entropy, which for a single example with true label y and predicted probability p is

> loss = −log(p) if y is 1, and −log(1 − p) if y is 0

The training procedure starts with arbitrary parameters, computes the loss, works out which direction to nudge each parameter to reduce it, and repeats. That procedure is gradient descent, and its details belong to the volume on neural networks. What matters here is that the loss is smooth and the problem is well behaved, so the search usually finds a good answer — and that the answer can be unstable when features are highly correlated or when one class is very rare.

## The Threshold Is a Decision, Not a Default

Software will report a 0.5 threshold because 0.5 is the obvious place to split a probability. In most real systems it is the wrong place.

The correct threshold comes from the relative costs. If a missed failure costs 500 and a false alarm costs 20, you should flag far more cases than the 0.5 rule would. Chapter 10 turns that intuition into arithmetic; here is the short version.

Suppose the model's probability is a genuine probability. Then flagging when p is above a threshold t costs

> expected cost = (1 − p) × cost of false alarm + p × cost of miss

Setting the two costs at 20 and 500, the threshold at which the expected costs of acting and not acting are equal is 20 / (20 + 500), about 0.038. Anything above a 3.8% chance of failure is worth inspecting, because the inspection is cheap and the miss is not.

| Miss cost | False alarm cost | Threshold |
|---|---|---|
| 500 | 20 | 0.04 |
| 100 | 20 | 0.17 |
| 20 | 20 | 0.50 |
| 20 | 100 | 0.83 |

The table explains a great deal of real-world behaviour. Screening programmes use low thresholds because missing a disease is expensive. Spam filters use higher thresholds because blocking a real message annoys users more than letting one spam through. Neither is a property of the model; both are properties of the decision.

## What a Coefficient Means, and What It Does Not

Because logistic regression is linear in the log-odds, a coefficient has a clean reading: increasing that feature by one unit adds its coefficient to the log-odds, which multiplies the odds by e raised to that coefficient.

A coefficient of 1.4 multiplies the odds by about 4. A coefficient of 0.06 multiplies them by 1.06, or 6%.

Two cautions. The effect on the probability depends on where you start: the same coefficient produces a large change in probability near 0.5 and a tiny one near 0.95. And a coefficient is not a cause. It describes an association in this dataset, and datasets encode the processes that produced them, including the biases of the people who made the decisions recorded in them.

## Problems

1. Compute the probability for z = 0, 1, 2, 3 using the logistic function, and check your answers against the table.

2. A model has z = −6 + 0.9 × vibration + 0.05 × temperature. Compute the probability for a pump at 3 mm/s and 60 °C, and for one at 5 mm/s and 40 °C. Which feature is doing more work, and how do you know?

3. With a miss cost of 400 and a false alarm cost of 25, compute the threshold. Then explain in two sentences what a manager would notice if you deployed at 0.5 instead.

4. A coefficient multiplies the odds by 3. What does that mean in words, and why is it not the same as tripling the probability?

5. Write the logistic model you would use to decide whether to send a customer a retention offer. Name the inputs, the label, the horizon, the costs and the threshold — before writing any code.
