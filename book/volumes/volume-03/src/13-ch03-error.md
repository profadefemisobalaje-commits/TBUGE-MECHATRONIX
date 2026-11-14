# Measuring Error

A model is trained by being punished. The punishment is a single number, the **loss**, and the model adjusts its dials to make that number smaller. Everything about what the model becomes follows from the shape of that number.

This is a short chapter with a long reach. Two models trained on identical data with identical architecture will behave differently if they are trained with different losses, because the loss is where you state what you consider a mistake.

## Squared Error, and What It Rewards

For regression, the default loss is the squared difference between prediction and truth, averaged over the data.

> loss = average of (prediction − truth)²

Squaring has two effects, and both matter. It removes the sign, so that misses above and below do not cancel. And it punishes large misses disproportionately: an error of 0.3 costs nine times as much as an error of 0.1.

A model trained this way becomes careful about extremes. If one row in the table is a typo of ten times the true value, the model will deform itself to reduce that one error, often at the cost of being worse everywhere else. That is why cleaning outliers matters before fitting, and why mean absolute error is the alternative when the tails are noise.

For reporting, the root mean squared error is preferred because it returns to the original units: a prediction of machine temperature in degrees should be scored in degrees, not in degrees squared. The mean absolute error is preferred when you want to describe the typical mistake rather than the worst one.

## Cross-Entropy, and Why It Is Not Squared Error

For classification, the model usually outputs a probability, and the loss is different.

If the model says the probability of the true class is p, the cross-entropy loss for that example is

> loss = −log(p)

Take three predictions for a true class:

- p = 0.9 gives a loss of 0.105.
- p = 0.5 gives a loss of 0.693.
- p = 0.1 gives a loss of 2.303.

Two things are worth noticing. Confident and right is cheap. Confident and wrong is expensive — the loss grows without limit as p approaches zero — which is exactly the behaviour you want from a system that will be used to make decisions.

Compare this with squared error on the same probabilities: 0.01, 0.25 and 0.81. Squared error punishes a confident mistake less severely than cross-entropy does, and it punishes a correct confident answer almost not at all. For probabilities, cross-entropy is the loss that matches the question.

| Prediction for the true class | Squared error | Cross-entropy |
|---|---|---|
| 0.9 | 0.01 | 0.11 |
| 0.7 | 0.09 | 0.36 |
| 0.5 | 0.25 | 0.69 |
| 0.1 | 0.81 | 2.30 |

## R-Squared and the Temptation of a Single Number

For regression, software often reports **R²**, the fraction of the variation in the target that the model explains. It ranges from zero (no better than predicting the average) to one (perfect), and it can be negative when the model is worse than the average.

The appeal is obvious: one number, bounded, comparable. The danger is equally obvious once you say it out loud. R² says nothing about the size of the errors in the original units, nothing about the worst case, and nothing about whether the model's assumptions hold outside the range of the data.

A model can have an R² of 0.99 on a dataset spanning 10 to 30 degrees and be useless at 40, because it has never seen 40 and its straight line may not bend the way physics does. Always report R² beside the root mean squared error, and always plot the residuals.

## Baselines: The Number You Must Beat

Before any model, compute the simplest possible predictor. It takes ten minutes and it redefines the whole project.

For regression, the baseline is usually the mean of the target. A model that cannot beat "predict the average" has learned nothing.

For classification, the baseline is the majority class. If 96% of parts are good, a model that says "good" to everything scores 96% accuracy, and any reported accuracy must be read against that.

For forecasting, the baseline is "tomorrow will be like today", which is surprisingly hard to beat for many real series.

| Problem | Baseline | Typical baseline score |
|---|---|---|
| Will this part be defective? (4% defects) | Always "not defective" | 96% accuracy |
| What will demand be tomorrow? | Today's value | Often 80–90% of the best model's performance |
| Which customers will churn? (8% churn) | Always "stay" | 92% accuracy |

A result is a comparison. "Our model achieved 91% accuracy" is not a finding; "our model achieved 91% against a 96% baseline" is a finding, and it is a bad one. The habit of computing the baseline first, and reporting it beside every result, is the single cheapest protection against self-deception in this field.

## Choosing the Loss Before the Model

The practical sequence is: decide what a mistake is, express it as a number, then choose a model that can minimise it.

A maintenance team cares about the cost of an unexpected failure and the cost of an unnecessary inspection. Those two costs imply a loss that weights the two errors differently — a cost matrix, which Chapter 10 turns into thresholds. A team training with plain accuracy has decided, silently, that those two costs are equal, and that decision was made by nobody.

The same logic applies to a regression. If over-predicting a drug dose is dangerous and under-predicting is merely ineffective, symmetric squared error is the wrong loss, because it treats a 5 mg overdose and a 5 mg underdose as equally bad. The fix is an asymmetric loss, and it is a design decision that belongs to the clinicians.

## The Accuracy Trap

Accuracy is the ratio of correct predictions to all predictions, and it has a property that makes it dangerous: it is dominated by the majority class.

Take a factory producing 1,000 parts, 30 of which are defective. A system that declares every part good scores (970/1000) = 97% accuracy, and catches nothing. A real system that catches 24 of the 30 defects, at the cost of flagging 36 good parts, scores (24 + 934)/1000 = 95.8% accuracy — lower than doing nothing, and vastly more useful.

| System | True positives | False positives | Missed defects | Accuracy |
|---|---|---|---|---|
| Flag nothing | 0 | 0 | 30 | 97.0% |
| Real detector | 24 | 36 | 6 | 95.8% |

The table is the whole argument for cost-sensitive evaluation, and it can be summarised in one sentence: when the thing you care about is rare, accuracy rewards ignoring it.

Three habits follow.

Always compute the majority-class baseline first, and report it beside every accuracy figure.

Report precision and recall, or a confusion matrix, so the reader can see what the model actually finds.

Keep the class proportions of your test set the same as production. A model evaluated on a deliberately balanced test set — half positives, half negatives — will look far better than it will perform in a world where positives are 3%.

The last point deserves an example, because balanced test sets are common in research and rare in life. A detector with 80% recall and 40% precision, evaluated on a balanced set, looks like a reasonable system. Evaluated at 3% prevalence, the same sensitivity and specificity produce a precision of about 5%, because the false positives overwhelm the true ones. Neither number is a lie. The second is the one that describes the factory.

## Problems

1. Compute the squared error and the cross-entropy for predictions of 0.95, 0.8, 0.6, 0.4 and 0.05 on the true class. Plot both on the same axes by hand and describe the difference in shape.

2. A regression model has an R² of 0.94 and an RMSE of 0.8 °C. A second has an R² of 0.90 and an RMSE of 0.5 °C. Which would you deploy for temperature control, and why?

3. A dataset has 3% defects. Compute the accuracy of the majority-class baseline. Then explain why a model with 94% accuracy might be worse than useless.

4. Design an asymmetric loss for a system that predicts how much insulin to deliver, where a dose 1 unit too high is four times as costly as a dose 1 unit too low. Write the loss as a formula and explain how it changes the model's behaviour.

5. Take a reported result you have seen in the news — accuracy, precision, error rate — and write the baseline that should have accompanied it.
