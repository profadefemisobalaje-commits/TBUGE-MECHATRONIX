# Beyond Accuracy

Two defect detectors are offered to a factory. The first catches three quarters of the cracked welds and flags eighty parts a week. The second catches nearly all of them and flags three hundred. Both report similar accuracy. One of them will keep its job; the other will be switched off within a month.

Which one is better depends on what a flag costs and what a missed crack costs, and that is a question about money and risk rather than about mathematics. This chapter is about turning that question into numbers a team can argue with.

## The Four Counts

Every binary classifier produces four counts, and everything else is arithmetic on them.

|  | Predicted positive | Predicted negative |
|---|---|---|
| Actually positive | True positives | False negatives |
| Actually negative | False positives | True negatives |

From those four, the useful ratios follow.

**Precision** is true positives divided by everything predicted positive: of the cases we flagged, how many were real?

**Recall**, also called sensitivity, is true positives divided by everything actually positive: of the real cases, how many did we find?

**Specificity** is true negatives divided by everything actually negative: of the healthy cases, how many did we leave alone?

**F1** is the harmonic mean of precision and recall, a single number that is high only when both are high.

## A Worked Comparison

Take a test set of 1,000 welds, 40 of which are cracked.

Model A catches 30 cracks and flags 80 parts in total. Model B catches 38 cracks and flags 300 parts.

| | Model A | Model B |
|---|---|---|
| True positives | 30 | 38 |
| False negatives | 10 | 2 |
| False positives | 50 | 262 |
| True negatives | 910 | 698 |
| Precision | 37.5% | 12.7% |
| Recall | 75% | 95% |
| Accuracy | 94.0% | 73.6% |

A has better precision and accuracy. B has better recall. Neither dominates, and the argument between them cannot be settled without costs.

Suppose a missed crack costs 500, because a weld that fails in service is a catastrophe, and a false alarm costs 20, because an inspector must look at the part again.

- Model A: 10 × 500 + 50 × 20 = 5,000 + 1,000 = 6,000.
- Model B: 2 × 500 + 262 × 20 = 1,000 + 5,240 = 6,240.

Model A wins, narrowly, despite finding fewer cracks, because its extra false alarms are cheap and B's are numerous. Change the miss cost to 2,000 and the answer flips: A costs 20,000 + 1,000 = 21,000, B costs 4,000 + 5,240 = 9,240.

This is the whole content of cost-sensitive evaluation. The model does not decide; the costs do. Any team that reports accuracy without costs has decided, silently, that every mistake is equally expensive.

## ROC and Its Limits

A classifier's threshold can be moved, trading false positives for false negatives. Sweeping the threshold traces out a curve, and the **receiver operating characteristic**, or ROC, plots the true positive rate against the false positive rate at every threshold.

The **area under that curve**, AUC, summarises it in one number. An AUC of 0.5 means the model is no better than a coin. An AUC of 1.0 means perfect separation. Values around 0.75 are common and useful; 0.9 is excellent; on hard problems, 0.65 may be the state of the art.

AUC has two attractive properties and one serious trap.

The properties: it does not depend on the threshold, and it does not depend on the class balance, because it is computed from rates rather than counts.

The trap: it is dominated by the easy negatives. When the positive class is 1% of the data, a model can achieve a high AUC while being useless at the operating point you care about, because most of the curve is built from cases that were never in doubt.

For rare events, the **precision–recall curve** is more informative. It shows what happens to precision as recall rises, and it makes the cost of catching the last few positives visible. Report both, and report the operating point you will actually use.

| Situation | Best summary |
|---|---|
| Balanced classes, choosing a threshold | ROC and AUC |
| Rare positives (under 5%), choosing a threshold | Precision–recall curve |
| A deployed system with fixed costs | Expected cost per decision |
| Communication with non-specialists | Confusion matrix in counts |

## Choosing the Threshold

The curve is not only a summary. It is a menu, and the operating point is chosen from it.

Suppose a plant inspects 1,000 parts a day and 30 are defective. The model produces a score, and the threshold converts the score into a decision. Four candidate thresholds, evaluated on a validation set of exactly that composition, give the following.

| Threshold | Caught | False alarms | Missed |
|---|---|---|---|
| 0.2 | 26 | 180 | 4 |
| 0.4 | 22 | 70 | 8 |
| 0.6 | 15 | 24 | 15 |
| 0.8 | 7 | 6 | 23 |

No threshold is best in the abstract. The choice depends on what each kind of mistake costs. Say a false alarm costs 60 units — an inspector's time, a re-check, a delayed line — and a missed defect costs 900, because it reaches a customer.

| Threshold | Cost of false alarms | Cost of misses | Total |
|---|---|---|---|
| 0.2 | 10,800 | 3,600 | 14,400 |
| 0.4 | 4,200 | 7,200 | 11,400 |
| 0.6 | 1,440 | 13,500 | 14,940 |
| 0.8 | 360 | 20,700 | 21,060 |

The best threshold is 0.4, and it is not the one that maximises any standard metric. It is not the one with the fewest false alarms, nor the one with the most catches. It is the one where the two costs trade evenly at the margin, and it is discoverable only because both costs were written down.

Two disciplines follow from this.

Choose the threshold on validation data, once, and then leave it alone. Adjusting it after seeing test results is a way of importing the test set into the model.

Report the threshold. A precision of 55% is meaningless without the rule that produced it, and the same model at a different threshold would report a different number from the same weights.

There is a useful sanity check available: the cost-optimal threshold sits where the model's scores have the density that balances the two costs. If the chosen threshold falls outside the range where the model produces scores at all, something is wrong with the costs or with the model, and the arithmetic will not save it.

## Calibration: Does 0.8 Mean 80%?

A model that outputs probabilities makes a stronger claim than one that outputs scores: it claims that among cases where it says 0.8, about four in five are positive.

**Calibration** is the agreement between that claim and reality. It is measured by bucketing predictions and comparing the predicted rate with the observed rate in each bucket.

A model can be excellent at ranking, with a high AUC, and badly calibrated. It may order cases correctly and consistently overstate the probability, which matters enormously when the probability feeds a decision rule or a published risk.

Two repairs are standard. **Platt scaling** fits a logistic curve to map scores to probabilities. **Isotonic regression** fits a monotonic step function, which is more flexible and needs more data. Both must be fitted on data the model has not seen, or they will inherit the same overconfidence they are meant to fix.

The **Brier score** summarises calibration and accuracy together: it is the mean squared difference between the predicted probability and the outcome. Lower is better, and it cannot be gamed by a confident, wrong model.

## Reporting a Classifier

A useful report contains six things, in this order.

The confusion matrix, in counts, so the reader can compute anything else.

Precision and recall at the operating threshold, with the threshold named.

The baseline: the score of predicting the majority class or the mean.

The curve, ROC or precision–recall as appropriate, so the reader can see what other thresholds would cost.

The calibration, ideally as a small table of buckets.

The uncertainty, as an interval on the headline measure.

Anything less invites the reader to invent the missing parts, and they usually invent them favourably.

## Problems

1. A test set has 500 cases, 25 positive. A model flags 40, of which 20 are positive. Build the confusion matrix and compute accuracy, precision, recall and specificity.

2. With a miss cost of 300 and a false alarm cost of 15, compute the expected cost of the model in question 1. Then compute it for a threshold that catches 23 positives with 90 flags. Which is cheaper?

3. Explain in two sentences why a high AUC does not guarantee a good system when the positive class is 1% of the data.

4. A model outputs 0.9 for 100 cases, and 60 of them are positive. Is it calibrated? What would you do about it?

5. Find a reported classifier result — a paper, a product page, a news story — and list which of the six reporting items are present and which are missing.
