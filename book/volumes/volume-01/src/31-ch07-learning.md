# Learning from Examples

A maintenance team has a year of records: for each week, the vibration of a pump motor, its temperature, and whether the pump failed in the following month. Nobody wrote a rule for predicting failure. There is no engineer who can tell you the exact vibration level at which a bearing starts to go, because it depends on the pump, the load, the alignment and the weather. But the records exist, and somewhere inside them is a pattern.

This is the situation that machine learning was invented for, and the shift it represents is easy to state. Instead of asking a person to write the rule, you show the machine examples and let it find the rule. What the machine finds is not wisdom. It is a compact description of the examples, and whether that description is useful depends entirely on whether the examples resemble the world the machine will meet. That is why half of this chapter is about testing, and why the next two chapters are about measurement.

## Twelve Pumps

Learning begins with a table. Rows are examples, columns are **features**, and the last column is the **label** — the thing you want to predict.

| Pump | Vibration (mm/s) | Temperature (°C) | Failed within a month? |
|---|---|---|---|
| 1 | 1.2 | 41 | No |
| 2 | 1.8 | 43 | No |
| 3 | 2.1 | 45 | No |
| 4 | 2.6 | 47 | No |
| 5 | 3.1 | 49 | No |
| 6 | 3.4 | 52 | Yes |
| 7 | 3.6 | 51 | Yes |
| 8 | 4.0 | 55 | Yes |
| 9 | 4.4 | 58 | Yes |
| 10 | 4.8 | 60 | Yes |

Ten rows is a very small dataset, and it is enough to see the method. Look down the vibration column. Below about 3.2 mm/s, every pump survived. Above it, every pump failed. There is a clean gap between 3.1 and 3.4.

That gap is a gift, and the first thing to do with a gift is to notice it before reaching for anything complicated.

## A Line in the Sand

The simplest model you can build from this table is a threshold:

> if vibration is above 3.25 mm/s, predict failure; otherwise predict no failure.

The number 3.25 is the midpoint of the gap, which is the safest place to put a boundary when you do not know more. The model has one parameter and can be written on the back of a receipt.

Before dismissing it, consider how much of industrial practice looks like this. A vibration limit, a temperature cut-out, a pressure relief valve: all of them are thresholds, and many of them are still doing useful work decades after they were set. The threshold is not less intelligent than a neural network. It is a different amount of assumption, and assumptions are only worth making when the data supports them.

The cost of a threshold is that it cannot express interactions. What if the pump is fine at 3.5 mm/s when it is cool, and dangerous at 3.5 mm/s when it is hot? A single threshold cannot say that. A model with two features can.

## Neighbours, and the Trouble With Distance

A second simple method is **nearest neighbour**. To predict a new pump, find the most similar row in the table and copy its label.

A new pump has vibration 3.5 mm/s and temperature 50 °C. The nearest row is pump 6, at 3.4 and 52, which failed. So predict failure. If the new pump were at 2.9 and 46, the nearest row would be pump 4, at 2.6 and 47, which survived.

Nearest neighbour has an attractive honesty: it needs no training at all. It simply stores the data and compares. It also has a trap that catches almost everyone the first time.

Suppose temperature were recorded in hundredths of a degree and vibration in whole mm/s. Two pumps differing by 0.1 mm/s in vibration and 5 °C in temperature would be judged “close” in temperature terms — 500 units apart — and “far” in vibration terms, 0.1 units apart. The comparison would be decided almost entirely by the units, not by what matters.

The fix is to **scale** the features before comparing them: subtract the mean and divide by the spread, so that every feature contributes on the same footing. It is a one-line operation and it changes results enormously. When a nearest-neighbour system behaves bizarrely, the first thing to check is whether anybody scaled the columns.

## Hide Four Rows First

Now the part that most introductions rush. Before choosing a threshold, before trying a second method, hide some of the data.

Pumps 3, 5, 8 and 9 go into a drawer. The model sees only the other six rows. Only after the model is fixed does the drawer open.

Using the visible rows, the gap between 3.1 and 3.4 still exists, so the threshold stays at 3.25. On the hidden four:

| Held-back pump | True label | Threshold prediction |
|---|---|---|
| 3 (2.1, 45) | No | No |
| 5 (3.1, 49) | No | No |
| 8 (4.0, 55) | Yes | Yes |
| 9 (4.4, 58) | Yes | Yes |

Four out of four. A perfect score, and the correct response is not celebration. It is to say plainly that four cases cannot distinguish a good model from a lucky one. The difference between four out of four and three out of four is a single pump. If the threshold had been set at 3.15 instead of 3.25, pump 5 might have flipped, and the story would be different.

Honesty about the size of the evidence is part of the skill. A student who writes “the model achieved 100% accuracy” has told you almost nothing. A student who writes “the model classified four held-out cases correctly; with four cases, the uncertainty is large, and eight more cases are needed before this result is meaningful” has told you what they know and what they do not.

## Memorising the Answers

Here is where learning goes wrong in the most instructive way.

Imagine a student who has a copy of last year's examination paper with the answers. They memorise every answer. On a re-run of the same paper they score 100%. On a new paper they score 40%, because they learned the answers rather than the subject.

A model can do exactly this. Give it ten points and let it fit a curve with nine bends, and it will pass through every point. The error on the training data is zero. The curve between the points, and beyond them, wanders wildly, because the extra bends were used to accommodate noise rather than structure.

| Model | Error on the ten training pumps | Error on twenty new pumps |
|---|---|---|
| Threshold on vibration | 0 of 10 | 3 of 20 |
| Curve with nine bends | 0 of 10 | 9 of 20 |

The simpler model is wrong on more training cases and right on far more new ones. That trade-off is the whole content of the phrase **overfitting**, and it explains why a perfect training score is a warning rather than good news.

The remedies are not mysterious. Use fewer parameters when the data is small. Keep a held-out set and judge only on that. Add a penalty for complexity, which is called regularisation and gets its own treatment later in the programme. And above all, remember what the ten pumps can and cannot support: with ten examples and one clean gap, a threshold is about as much structure as the evidence can bear.

## Exercises

1. Copy the pump table, but hide the labels of pumps 2, 5, 7 and 10. Choose a threshold using only the visible six rows, and write down how you chose it. Predict the four hidden pumps, uncover the labels, and build a confusion matrix for the four predictions.

2. Repeat with a threshold 0.5 mm/s higher and with one 0.5 mm/s lower. Which pumps change? Which kind of mistake got worse?

3. Compute the mean and spread of the vibration column and of the temperature column. Scale both columns, and recompute the nearest neighbour for a pump at 3.5 mm/s and 50 °C. Does the answer change? Explain why in one sentence.

4. Sketch, on paper, ten points that lie roughly on a rising line with visible scatter. Draw a straight line through the middle of them. Then draw a curve that passes through every point. Which one would you trust for a point at the far right of the page, and why?
