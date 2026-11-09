# Overfitting, and the Two Kinds of Being Wrong

A student preparing for an examination has two ways to fail. They can learn too little, arriving with a few general principles and no grip on the specifics, and be unable to answer anything. Or they can learn last year's paper by heart, answering every question on it perfectly and collapsing on anything new.

Machine learning has exactly the same two failures, and they are the two ends of a single dial. Turning the dial towards more flexibility reduces the first and increases the second. The skill is finding the setting that minimises the total, and the instrument that measures it is data the model has not seen.

## The U-Shaped Curve

The demonstration is best done with numbers, so here is one. Take twenty points from a smooth curve with a little noise, and fit polynomials of increasing degree.

| Model | Parameters | Error on training data | Error on new data |
|---|---|---|---|
| Straight line | 2 | 0.42 | 0.45 |
| Cubic | 4 | 0.08 | 0.09 |
| Degree 9 | 10 | 0.001 | 0.35 |
| Degree 15 | 16 | 0.0001 | 2.10 |

Read the last two rows carefully. The degree-9 model fits the training data almost perfectly and is four times worse on new data than a cubic. The degree-15 model fits the training data better still and is catastrophic.

Nothing went wrong in the fitting. The extra parameters were used exactly as intended: to accommodate the particular positions of twenty noisy points, including the noise. Between the points, and beyond them, the curve swings wildly, because that is what a high-degree polynomial does when asked to pass through arbitrary points.

This is **overfitting**: the model has learned the sample rather than the pattern.

## Two Errors, One Total

The behaviour is best understood by splitting the error into three parts.

> expected error = bias² + variance + irreducible noise

**Bias** is the error caused by the model being too simple for the truth. A straight line through a curve has high bias, and no amount of data will remove it.

**Variance** is the error caused by the model being sensitive to the particular sample it was trained on. A degree-15 polynomial has high variance: train it on a different twenty points from the same process and it produces a completely different curve.

**Noise** is the part of the target that cannot be predicted from the inputs at all. It is the floor, and no model can go below it.

The trade between the first two is the reason the curve in the table is U-shaped. As flexibility rises, bias falls and variance rises. The best model is somewhere in the middle, and where exactly depends on how much data you have: more data reduces variance, so more data allows a more flexible model.

| Data size | Model that usually wins |
|---|---|
| 30 rows, 5 features | A simple linear model or a shallow tree |
| 3,000 rows, 20 features | Regularised regression, random forest |
| 300,000 rows, many features | Flexible boosted models, neural networks |

The practical rule that follows is uncomfortable and correct: complexity must be paid for with data. A model with a thousand parameters trained on two hundred rows is not ambitious; it is a memory of two hundred rows with a thousand knobs to turn.

## Regularisation: Paying for Complexity

There is a way to have a flexible model and still control it: add a penalty for large parameters to the loss.

For a linear model, **ridge regression** minimises

> squared error + λ × sum of squared coefficients

The first term wants the model to fit the data. The second wants the coefficients small. The dial λ sets the exchange rate. At λ equal to zero you have ordinary least squares; as λ grows, coefficients shrink towards zero and the model becomes simpler and more stable.

**Lasso regression** uses the sum of absolute values instead, which has a useful side effect: it drives some coefficients exactly to zero, performing a kind of automatic feature selection.

The effect on the polynomial example is direct. Fitted with a large penalty, the degree-15 model's coefficients are forced small, and the curve becomes smooth again. The flexibility is still there, but it is expensive to use, so it is used only where the data insists.

Regularisation is not magic. It works because it encodes a belief: that large coefficients are usually a sign of fitting noise rather than signal. On a problem where large coefficients are genuinely justified, the penalty fights the truth and must be set small. Choosing λ is, once again, a job for validation data.

## Learning Curves

A second diagnostic shows whether more data would help.

Plot error on the vertical axis and training-set size on the horizontal, with two lines: training error and validation error.

If both curves are high and close together, the model is underfitting. More data will not help; a better model will.

If training error is low and validation error is much higher, with a visible gap, the model is overfitting. More data will usually help, and so will regularisation.

If both curves have converged to a low value and close together, the model is working, and the remaining error is close to the noise floor.

| Pattern | Diagnosis | Action |
|---|---|---|
| Both high, close | Underfitting | More flexible model, better features |
| Training low, validation high | Overfitting | More data, regularisation, simpler model |
| Both converging low | Healthy | Stop; measure the floor |
| Validation worse than training, gap growing | Data quality or leakage | Investigate the split |

## Stopping Early, on Purpose

There is a regulariser that requires no extra term at all, only patience: stop training before the model finishes learning.

The mechanics are visible in the U-shaped curve. Training error falls monotonically, always. Validation error falls, bottoms out, and rises. The rising phase is not random: the model has begun to fit the particular noise of the training set, and that noise is absent from the validation set. If you stop at the bottom, you keep the general part and discard the memorised part.

| Epochs | Training loss | Validation loss |
|---|---|---|
| 5 | 0.61 | 0.58 |
| 10 | 0.44 | 0.46 |
| 20 | 0.29 | 0.43 |
| 40 | 0.13 | 0.49 |
| 80 | 0.04 | 0.68 |

The table is a small model on a small dataset, and it is typical in shape. Training loss falls by a factor of fifteen; validation loss falls by a quarter, stops, and then climbs by more than half. The best model is the one at epoch twenty, and everything after that is wasted computation producing a worse system.

The practical implementation is a checkpoint rule: after every epoch, evaluate on the validation set, keep the weights if the score improved, and count how many epochs have passed without improvement. When the count exceeds a patience setting — five or ten epochs is usual — stop and return the best checkpoint rather than the final one.

Two caveats matter.

Early stopping makes the validation set part of training, in a weak sense, because you are choosing a stopping point using it. This is why the test set must be untouched until the end. If you choose the epoch on the test set, the test score is no longer an estimate of anything.

The stopping point is a fitted hyperparameter, and it moves when the data changes. A model that stopped at epoch twenty on last year's data may need thirty on this year's, which is a further argument for automating the choice rather than hard-coding it.

## Why This Is the Central Skill

There is a reason this chapter sits in the middle of the volume rather than at the end. Every method in Part Two can be overfitted, and every tool in Part Four exists to detect it. A practitioner who understands the trade can use any library competently; one who does not will report excellent numbers and be surprised in production.

The habit to build is scepticism about good news. When a model reports a dramatic improvement, the first question is not "which feature helped?" but "what did it memorise?". The second question is "what data did I use to measure that, and was it really held out?".

## Problems

1. Using the table above, compute the difference between training and test error for each model. Which model would you deploy, and does your answer change if you have ten times as much data?

2. A model has high bias and high variance simultaneously. Is that possible? Explain what it would look like on a learning curve.

3. Ridge regression with λ = 0, 1 and 100 is applied to a model whose coefficients were 3.0, −2.0 and 0.5. Describe qualitatively what happens to the coefficients as λ rises, and what happens to the predictions on new data.

4. Your model has a training error of 0.02 and a validation error of 0.30. Name three things you would try, in order of likely benefit.

5. Explain in two sentences why adding parameters to a model requires adding data, using the idea of variance.
