# Validation, and the Many Ways to Cheat

A team reports 94% accuracy. The number is real: they ran the code, the model produced it, and the test set was genuine. Six months later the system is in production and performing at 78%, and nobody can work out why.

The usual explanation is not fraud. It is that the 94% was measured, repeatedly, while decisions were being made in response to it. Every time the team changed a feature, a threshold, a model or a preprocessing step and re-measured on the same data, a little information from that data entered the model. After fifty such decisions, the test set had quietly become training data.

This chapter is about measuring performance without fooling yourself, which is harder than it sounds and entirely learnable.

## The Roles of Three Sets

The split has three members and each has one job.

The **training set** is where parameters are fitted. Nothing else.

The **validation set** is where decisions are made: which model, which features, which threshold, when to stop training. It is looked at many times, and that is fine, because it is being used for its purpose.

The **test set** is opened at the end, once, to produce the number you report. If you ever look at it and then change something in response, it has joined the validation set and you no longer have a test set.

In small projects, one validation set is noisy, and a lucky split can mislead. The standard fix is cross-validation.

## Cross-Validation

**k-fold cross-validation** divides the data into k parts. Train on k−1 of them, test on the remaining one, and repeat until every part has been the test set once. Average the results.

With k equal to five, each model sees 80% of the data for training and 20% for testing, five times. With k equal to ten, 90% and 10%, ten times. Leave-one-out is the extreme: k equals the number of rows.

The choice trades computation against stability. Five-fold is cheap and usually enough. Ten-fold gives a slightly less biased estimate and costs twice as much. Leave-one-out is nearly unbiased and has high variance, which is the opposite of what people expect; it is rarely worth it.

Two refinements matter in practice. **Stratified** folds keep the class proportions the same in each part, which is essential when the rare class is 3% of the data. **Repeated** cross-validation runs the whole procedure several times with different random splits, which gives an honest sense of how much the estimate moves.

And one rule that is broken constantly: all preprocessing, including scaling, imputation and feature selection, must be fitted inside each fold. Washing the whole dataset before splitting leaks information from the test fold into the training fold.

## Six Ways to Leak

Leakage is the presence of information in training that will not be available at prediction time. It is the most common cause of a model that looks excellent and fails.

| Leak | How it happens | The fix |
|---|---|---|
| Target leak | A column that is only filled after the event | Ask what is known at prediction time |
| Time leak | Random split on time-ordered data | Split by date |
| Group leak | Same patient or machine in both sets | Split by group |
| Duplicate leak | Near-identical rows in both sets | De-duplicate, then split |
| Preprocessing leak | Scaling or imputation fitted on all data | Fit inside each fold |
| Selection leak | Choosing features by their correlation with the test set | Select inside each fold |

Two of these deserve a story, because they are the ones that survive review.

The target leak is easy to spot once you know to look. A churn model included "number of cancellation emails received". It scored 0.97 AUC and was useless, because a cancellation email is the churn, not a predictor of it. The fix was not statistical; it was asking whether the value would exist for a customer who had not yet cancelled.

The time leak is subtler. A demand model was split randomly, so that some of its training data came from after its test data. It learned the seasonal pattern from the future and appeared to forecast well. Split by date, it lost most of its apparent skill. The fix costs accuracy and buys truth.

## A Protocol That Survives Scrutiny

None of this requires a statistician. It requires a sequence that is decided in advance and not changed when the results disappoint.

1. Write down the question, the target, the horizon and the cost of each error.
2. Fix the split before looking at any model. Save the test set aside and do not touch it.
3. Establish the baseline: the mean, the majority class, the previous value.
4. Develop on the training set, decide on the validation set, and keep a log of every decision.
5. When the development stops, run the test set once and report the result, whatever it is.
6. Report the uncertainty, not just the number.

Step five is the one that separates honest work from confident work. A team that opens the test set, dislikes the number, and goes back to development has destroyed its only independent measurement, and no amount of later rigour can restore it.

## Reporting Numbers Honestly

A result that can be checked has four parts: the number, the dataset, the uncertainty and the baseline.

"Our model achieved 91% accuracy" is a claim. "Our model achieved 91% accuracy (95% confidence interval 89–93) on 4,000 held-out parts from a single plant, against a majority-class baseline of 88%" is a result. The second costs one extra sentence to write and prevents a year of misunderstanding.

Uncertainty is easy to compute and usually omitted. For a proportion p estimated from n independent cases, the standard error is the square root of p(1−p)/n. With 4,000 cases and p equal to 0.91, that is about 0.0045, so a 95% interval is roughly plus or minus 0.9 percentage points. With 200 cases, the interval is plus or minus four points, and the difference between two models is likely to be noise.

| Test cases | Accuracy | 95% interval | Difference detectable |
|---|---|---|---|
| 100 | 0.91 | ± 5.6 points | More than 8 points |
| 1,000 | 0.91 | ± 1.8 points | More than 2.5 points |
| 10,000 | 0.91 | ± 0.6 points | More than 0.8 points |

The table answers a question that consumes enormous amounts of engineering time: how large does a test set need to be to tell two models apart? The answer is usually larger than the one available, which is why small improvements on small datasets should be treated as noise until repeated.

## Problems

1. You have 1,200 rows, 8% of them positive, and you want to compare five models. Describe the split and the validation procedure you would use, and say how many times each model is fitted.

2. A colleague scales all features before cross-validation, using the mean and spread of the whole dataset. Explain the leak and estimate whether it would matter more on 200 rows or 200,000.

3. A model predicts equipment failure using a column called "days since last maintenance". Is that a leak? Argue both sides, and say what information you would need.

4. With 500 test cases and 92% accuracy, compute the standard error and a 95% interval. Your colleague's model scores 93.5% on the same test set. Are the models distinguishable?

5. Write the reporting sentence for a result you have produced yourself, with all four parts: number, dataset, uncertainty and baseline.
