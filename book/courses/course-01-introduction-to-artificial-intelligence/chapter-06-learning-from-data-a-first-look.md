# Learning from Data: A First Look

> Course 1: Introduction to Artificial Intelligence - Chapter 6 of 10

## Opening

By the end of this chapter you can train a simple classifier on a small table of examples, test it honestly, and explain why a model that scores perfectly may still be useless.

Imagine a maintenance team with a year of records: for each week, the vibration of a pump motor, its temperature, and whether the pump failed in the following month. Nobody wrote a rule for predicting failure. The data itself contains the pattern, if there is one. This is the shift that changed AI after the 1990s: instead of asking an expert to state the rules, we show the machine hundreds of examples and let it find them. You can do the same thing by hand, with twelve rows and a pencil, and understand it better than most people who call a library and hope.

## Big Picture

**Machine learning** fits a rule from examples rather than from instructions. Each example has **features** — the numbers you measure — and a **label** — the answer you want to predict. The learner produces a **model**: a compact rule that maps features to labels.

The only thing that matters is whether the model works on examples it has never seen. That is called **generalisation**, and it is the whole game. A model can score 100% on the data it learned from and fail completely on new data, because it memorised the examples instead of the pattern. This is **overfitting**, and it is the most common failure in applied machine learning. The cure is simple and non-negotiable: hide some data before you start, train on the rest, and only ever judge the model on the hidden part.

## Key Words

- **Feature** - a measurable input, such as vibration in mm/s.
- **Label** - the answer you want to predict, such as "failed" or "did not fail".
- **Training set** - the examples the model learns from.
- **Test set** - examples held back and used only for judging.
- **Model** - the rule the learner produces.
- **Generalisation** - doing well on examples the model has never seen.
- **Overfitting** - fitting the training examples so closely that new examples fail.

## The Explanation

### Step 1 - Build a table of examples

Learning starts with a table. Rows are examples, columns are features, and the last column is the label.

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

Ten rows is tiny, but it is enough to see the method. Look at the vibration column: below about 3.4 mm/s, every pump survived. Above 3.4, every pump failed. There is a clean gap between 3.1 and 3.4.

The first model you should always try is the simplest possible one:

```
if vibration > 3.25 mm/s then "will fail" else "will not fail"
```

That is a **threshold model** with one parameter, 3.25, chosen as the midpoint of the gap. It has two numbers' worth of complexity and it may be right. Before reaching for anything fancier, check whether a straight line already solves the problem. In real industry, a surprising share of useful predictive maintenance is a threshold on one sensor.

### Step 2 - Try a second method and compare

A second simple method is **nearest neighbour**: to predict a new pump, find the most similar row in the training table and copy its label. If a new pump has vibration 3.5 mm/s and temperature 50 °C, the nearest row is pump 6 (3.4, 52, Yes), so predict "Yes".

Nearest neighbour has an attractive property: it needs no training at all, it just stores the data. It has two weaknesses. It stores everything, so memory grows with the dataset. And it is easily fooled by a feature that is measured on a large scale. If temperature were given in hundredths of a degree and vibration in whole mm/s, "nearest" would be decided almost entirely by temperature. This is why features are almost always scaled before comparison, a habit you will meet again in Course 3.

Now compare both methods on the same test. Hold back pumps 3, 5, 8 and 9. Train on the other six, then predict the four:

| Held-back pump | True label | Threshold prediction | Nearest neighbour prediction |
|---|---|---|---|
| 3 (2.1, 45) | No | No | No |
| 5 (3.1, 49) | No | No | No |
| 8 (4.0, 55) | Yes | Yes | Yes |
| 9 (4.4, 58) | Yes | Yes | Yes |

Both methods get 4 out of 4. So which is better? With four test cases, neither result means much — the difference between 4/4 and 3/4 is one example, well within luck. This is the honest conclusion, and writing it down is part of the skill. Small tests produce large uncertainties, and you must say so.

### Step 3 - Judge with a confusion matrix, not one number

A single accuracy number hides the kind of mistake. A **confusion matrix** shows both.

For a failure-prediction model there are two mistakes, and they are not equal. A **false alarm** means you service a healthy pump: it costs money and time. A **missed failure** means a pump dies in service: it costs production, and possibly safety. You must decide the trade-off before you tune the model.

Take a larger test of 100 pumps, 10 of which really fail. The model predicts 14 failures. Of those, 8 are real and 6 are false alarms. It misses 2 real failures.

| | Model says fail | Model says fine |
|---|---|---|
| Actually failed (10) | 8 | 2 |
| Actually fine (90) | 6 | 84 |

Accuracy is (8 + 84) / 100 = 92%. Precision — of the ones we flagged, how many were real — is 8 / 14 = 57%. Recall — of the real failures, how many did we catch — is 8 / 10 = 80%.

A system with 57% precision sends six healthy pumps to the workshop for every eight real problems. A maintenance manager will stop using it within a month, no matter what the accuracy says. Lowering the threshold to catch all ten failures would raise recall to 100% and probably drop precision further, flooding the team with false alarms.

There is no free choice here. There is only a decision about which mistake you can live with, made with the people who own the consequences. That decision is engineering, and it is yours to force into the open.

## Where It Goes Wrong

**Mistake 1 - Testing on the training data.** The model scores 100% and everyone is happy until it meets a new pump. *Fix:* split the data before you look at it, and never touch the test set during development.

**Mistake 2 - Leakage.** A feature secretly contains the answer, such as a "repair date" column that is only filled after a failure. *Fix:* ask of every column, "would I know this at prediction time?"

**Mistake 3 - Ten rows and a big claim.** A model trained on ten examples is a hypothesis, not a result. *Fix:* report the number of examples beside every score.

**Mistake 4 - Ignoring class imbalance.** When 95% of cases are "fine", a model that always says "fine" is 95% accurate and worthless. *Fix:* report precision and recall, and compare with the always-fine baseline.

**Mistake 5 - Tuning on the test set.** Trying twenty settings and keeping the best test score means the test set has become training data. *Fix:* keep a third set, the validation set, for tuning.

## Case Note

In 2008, Google launched Flu Trends, a service that estimated the level of influenza in a region from the volume of flu-related search queries. It was a genuine research success. In the United States, its estimates matched official surveillance data closely, and it reported them about two weeks earlier, because people search before they see a doctor.

Then it drifted. For several seasons, including the 2012–13 flu season, it substantially overestimated the number of cases. Some estimates suggested it was out by more than a factor of two. The reasons were ordinary: Google changed its search suggestions, people's search habits changed, media coverage changed what people typed. The model had been fitted to a world that no longer existed.

The most instructive part is the method. The model's search terms had been selected by checking how well they fitted past flu data. That is a mild form of using the test data for training: the terms were chosen partly because they matched the very seasons used to judge them. When new seasons arrived, the apparent success did not continue. The service was discontinued in 2015.

This is why the pump example in this chapter hides four rows before you choose a threshold. It is why the book insists on a test set that you do not touch, and on monitoring after launch. The pattern you find in data is the pattern of that data, and the world moves. A model is a hypothesis about the future that must be checked against the future.

## Mini-Lab

**You need:** paper and a pen.

**Do this:**
1. Copy the ten-pump table, but hide the labels of pumps 2, 5, 7 and 10.
2. Choose a threshold using only the visible six rows. Write down how you chose it.
3. Predict the four hidden pumps. Then uncover the labels and score yourself.
4. Build the confusion matrix for those four predictions.
5. Repeat with a threshold 0.5 mm/s higher. Which pumps change? Which mistake got worse?

**What you should see:** moving the threshold trades one kind of mistake for the other. There is no setting that removes both, which is the lesson.

**Why it matters:** every medical test, fraud detector and safety alarm you will ever build has this same trade-off, and someone must own it.

## Recap and Questions

**Three things to remember**

1. Learning fits a rule from examples; the only score that matters is on data the model has never seen.
2. Always try the simplest model first — often a single threshold is enough.
3. Accuracy hides the kind of mistake. Report precision and recall, and name the mistake you can live with.

**Check yourself**

1. Why is a 100% training score a warning sign rather than good news?
2. In the pump example, which mistake is more expensive? Argue both sides in one sentence each.
3. Your model has 95% accuracy and 20% recall. What does that mean in plain words?

**One thing to try next**

Find a dataset you already own — a spreadsheet of expenses, a fitness app history — and predict one column from another using a threshold you choose by eye. Then check it on rows you hid first. The surprise is the lesson.
