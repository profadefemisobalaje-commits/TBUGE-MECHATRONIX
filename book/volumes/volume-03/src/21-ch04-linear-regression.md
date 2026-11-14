# A Straight Line, Fitted Properly

A bearing runs for five hours. Its housing warms from 12 °C above ambient to 21 °C. Plot the two against each other and the points fall almost on a line. If that relationship holds, the temperature tells you how long the machine has been working, and — more usefully — a temperature that rises faster than the line predicts tells you something is wrong.

The straight line is the oldest model in statistics and the most useful first model in machine learning. It is not a toy, and it is not a stepping stone to something better. Many real relationships are close enough to linear that the line wins on every axis that matters: it is cheap, it is explainable, it needs little data, and it fails in ways you can see.

## The Line and Its Two Numbers

A straight line is written

> prediction = intercept + slope × input

The **slope** says how much the output changes when the input increases by one unit. The **intercept** says what the output is when the input is zero. Both have units, and the units are the fastest way to check that a fit is sensible.

Here is a table of five observations from a test rig: hours run, and temperature rise above ambient.

| Hours run | Temperature rise (°C) |
|---|---|
| 1 | 12.1 |
| 2 | 13.9 |
| 3 | 17.2 |
| 4 | 18.8 |
| 5 | 21.4 |

Fitting by eye, the line should rise by about 2.3 degrees per hour and pass near 16.7 at three hours. The arithmetic gives the same answer and tells you how confident to be.

## Least Squares, by Hand

The standard method chooses the line that minimises the sum of squared vertical distances from the points to the line. The formulas are short, and computing them once by hand removes the mystery.

First, the averages: the mean of the hours is 3, and the mean of the temperatures is 16.68.

Then two sums. For each point, take the deviation in hours from the mean and the deviation in temperature from the mean, multiply them, and add:

> (−2)(−4.58) + (−1)(−2.78) + (0)(0.52) + (1)(2.12) + (2)(4.72) = 23.5

Then take the squared deviations in hours and add:

> 4 + 1 + 0 + 1 + 4 = 10

The slope is 23.5 / 10 = 2.35 degrees per hour. The intercept follows from the line passing through the average point: 16.68 − 2.35 × 3 = 9.63 degrees.

So the model is

> temperature rise = 9.63 + 2.35 × hours

Two sanity checks, both done in seconds. The units are degrees per hour, which is what a slope should be. And the line passes through the average of the data, which it must, because least squares always does.

| Point | Hours | Actual | Predicted | Residual |
|---|---|---|---|---|
| 1 | 1 | 12.1 | 11.98 | +0.12 |
| 2 | 2 | 13.9 | 14.33 | −0.43 |
| 3 | 3 | 17.2 | 16.68 | +0.52 |
| 4 | 4 | 18.8 | 19.03 | −0.23 |
| 5 | 5 | 21.4 | 21.38 | +0.02 |

## Reading What You Fitted

The residuals — the differences between what happened and what the line predicted — are the most informative part of the output, and they are the part most often ignored.

The sum of squared residuals here is 0.523. The total variation of the temperatures around their mean is 55.75. The ratio gives R² = 1 − 0.523/55.75 = 0.991, which means the line explains 99% of the variation. The root mean squared error is 0.32 °C, and the mean absolute error is 0.26 °C.

Those four numbers describe different things. R² says the shape is right. RMSE says the typical error in degrees. The residual table says whether the errors are patternless. Here they alternate sign, which is what you want: no obvious curve left in the data.

The residuals also reveal what the model cannot tell you. Every point has a positive residual in the middle and negative at the ends — mild curvature. A real bearing's temperature does not rise linearly forever: it approaches an equilibrium where heat in equals heat out. The line is a good local description and a poor global one, and the residuals are the evidence.

## Where a Straight Line Breaks

Four failures are worth memorising, because each has a recognisable signature.

**Non-linearity.** The relationship curves. The residual plot shows a systematic bow: positive in the middle, negative at the ends, or the reverse. The fix is to add a squared term, transform an input, or fit a more flexible model.

**Extrapolation.** The line continues beyond the data because a line has no way to stop. A model fitted between 1 and 5 hours will happily predict 60 degrees at 20 hours, and be wrong, because the physics saturates. Never trust a regression outside the range of its inputs without independent reason.

**Interaction.** The effect of one input depends on another. Temperature rise may depend on hours *and* on ambient humidity, and the dependence may be different at high humidity. A model with additive terms cannot represent that; it needs a product term or a different method.

**Changing variance.** The errors grow with the input: small at one hour, large at five. Least squares assumes they do not, so the fit is dominated by the noisiest region. A log transform or weighted fitting is the usual repair.

| Symptom | Likely cause | First thing to try |
|---|---|---|
| Bowed residual pattern | Non-linearity | Add a squared term |
| Errors growing with input | Changing variance | Fit on a log scale |
| Line misses a subgroup | Missing variable | Add the group or an interaction |
| Excellent fit, terrible predictions at new values | Extrapolation | Restrict the range, or use physics |

## More Than One Input

Most real relationships involve several inputs, and the extension is straightforward: the model becomes

> prediction = intercept + slope₁ × input₁ + slope₂ × input₂ + …

Each slope now means something slightly different from before. It is the change in the output when that input rises by one unit, **holding the others constant**. That phrase is doing a lot of work, and it is the reason regression coefficients are so often misinterpreted.

Suppose a model of temperature rise is fitted with two inputs: hours run and ambient humidity, giving

> rise = 9.4 + 2.3 × hours + 0.12 × humidity

The reading is: each additional hour adds 2.3 degrees, for machines running in the same humidity; each percentage point of humidity adds 0.12 degrees, for machines that have both run the same number of hours. The second clause is almost never what a manager wants to know, because in practice humidity and hours are correlated.

That correlation produces the most common pathology in multiple regression, called **collinearity**. When two inputs move together, the model cannot tell which one is responsible, and the coefficients become unstable: add a few rows and the humidity coefficient swings from +0.12 to −0.30 while the predictions barely change. The model still predicts; it has simply stopped being a description.

The diagnostic is to compute the correlation between every pair of inputs. Correlations above about 0.8 are a warning. The fixes are to drop one of the pair, to combine them into a single feature, or to use a regularised model that distributes the effect stably rather than assigning it arbitrarily.

| Symptom | Likely cause | Response |
|---|---|---|
| Coefficients flip sign between datasets | Collinearity | Drop or combine a feature |
| Huge coefficient with tiny effect | Scaling or collinearity | Standardise inputs |
| Good predictions, nonsensical coefficients | Confounding | Use for prediction only |

This is the point at which prediction and explanation part company. A model can be excellent at predicting while its coefficients are meaningless as descriptions, and a model whose coefficients are meaningful may predict poorly. Deciding which you need is a requirement, not a technicality.

## Why Start Here

A more flexible model would fit these five points better. It would also be harder to check, harder to explain, and no more accurate on the region that matters. Starting with a line has three practical benefits.

It gives you a baseline that is not a flat average, so later models must beat something reasonable.

It exposes the structure of the data. Fitting a line tells you the sign, size and units of each effect, which is often the actual answer the business wanted.

It fails visibly. When a straight line is wrong, the residual plot says so. When a large model is wrong, the loss is lower and the failure is hidden.

## Problems

1. Fit a line by hand to the five points above. Confirm the slope and intercept, then predict the temperature at 6 hours and at 0.5 hours. Which prediction do you trust less, and why?

2. A regression predicts house price from floor area and gives a slope of 850 per square metre and an intercept of 40,000. Interpret both numbers in words, and say which of them is physically meaningful.

3. The residual plot of a model shows a clear U shape. What does that tell you, and what would you do next?

4. A model of energy use versus production volume is fitted on data from 20% to 90% utilisation. A manager asks for a prediction at 110%. Write the sentence you would say, and the number you would refuse to give.

5. Explain in three sentences why a straight line can be the best model even when a curved one fits the training data better.
