# Features and the Pipeline That Produces Them

In most tabular projects, the model is a small part of the work. The larger part is turning raw columns — timestamps, category names, missing values, free text, sensor readings at irregular intervals — into a table of numbers that a model can use. That transformation is the **pipeline**, and in practice the pipeline is the model: change it and the model changes, often more than swapping algorithms would.

This chapter is about building pipelines that are correct, reproducible and impossible to leak.

## Fit on Train, Apply Forward

Every transformation that learns something from data must be fitted on the training set and then applied, unchanged, to validation, test and production data.

Scaling is the simplest example. Standardisation uses the mean and spread of each feature. If those are computed over the whole dataset, the test set's statistics have entered the model, and the model has seen the future. The effect is small on large datasets and substantial on small ones, and it is a leak regardless.

The same rule governs imputation. A median computed over all rows, including test rows, is a leak. A median computed on training rows and applied everywhere is correct.

The clean way to express this is a pipeline object that bundles the transformations and the model into one unit. Fitting the pipeline fits the transformations on training data only. Predicting applies them in order. There is no opportunity to leak, because there is no separate step in which somebody forgot.

## Categories, and the High-Cardinality Trap

Models consume numbers, so categories must be encoded.

**One-hot encoding** creates a column per category, with a 1 where the category applies. It is simple, interpretable and explodes in size when a category has many values: a postcode with 3,000 distinct values becomes 3,000 columns, almost all zero.

**Ordinal encoding** assigns each category a number. It is compact and it invents an order, which a linear model will take seriously. It is appropriate for ordered categories such as small, medium and large, and misleading for unordered ones.

**Target encoding** replaces a category with the average outcome for that category. It is powerful and dangerous: the category's average includes the row being encoded, so the model can see part of its own label. The defences are to compute the encoding inside cross-validation folds, to smooth it towards the global mean for small categories, and to add noise.

**Hashing** maps categories to a fixed number of buckets. It handles unbounded vocabularies and loses interpretability.

| Encoding | Size | Interpretable | Leak risk |
|---|---|---|---|
| One-hot | Grows with categories | Yes | None |
| Ordinal | One column | Partly | None |
| Target | One column | No | High without folds |
| Hashing | Fixed | No | None |

## Time, Windows and the Shift

Sensor and business data almost always arrives as a time series, and time-series features are where leakage hides most comfortably.

A rolling average is a natural feature: the mean of the last hour's readings. If that average is computed over a window that includes the current row, the row's own value is inside its own feature, and the model will exploit it.

The rule is to use only information available strictly before the moment of prediction. That means shifting the window back by one step, and being explicit about the forecast horizon. A model predicting the next hour cannot use this hour's reading; a model predicting tomorrow can.

Lags are the other workhorse: yesterday's value, last week's value, the value at the same hour seven days ago. They encode the persistence that makes naive forecasts hard to beat, and they are safe as long as the lag is at least as long as the horizon.

## Reproducibility, or the Model You Cannot Rebuild

A model that cannot be rebuilt is a liability. Six months after deployment, the team will be asked why it behaves as it does, and the answer must not be "we are not sure which version of the data we used".

Five practices make a project reproducible.

**Version the code** in a repository, with every experiment as a commit.

**Snapshot the data.** A hash of the training file is enough to tell you whether the data has changed, and a stored copy is better.

**Fix the seed.** Random splits, random forests and neural initialisation all depend on the seed; without it, results move between runs and comparisons become noise.

**Record the configuration.** The model type, hyperparameters, feature list and threshold should be a file, not a memory.

**Log the environment.** Library versions change behaviour; a model trained under one version may not be reproducible under another.

None of this is exotic. All of it is skipped on small projects, and small projects are exactly where the model will be handed to somebody else.

## Features That Carry Meaning

A feature is a hypothesis about what matters, expressed as a number. Good features often beat good algorithms, and they come from understanding the domain rather than from the library.

A maintenance dataset has a vibration column. Useful derived features include the ratio of current vibration to the machine's own baseline, the rate of change over the last week, and the count of days above a threshold in the last month. Each encodes a different belief about how machines fail: gradual drift, sudden change, cumulative exposure.

A retail dataset has transaction timestamps. Useful features include days since last purchase, average interval between purchases, and whether the customer bought in the same month last year.

The discipline is to write down, for each feature, the sentence it encodes. If the sentence is nonsense, the feature will be noise. If the sentence is a leak, the model will be brilliant and useless.

## Problems

1. List the transformations in a pipeline for a table with numeric columns, a category with 12 values, a date column and a column with 15% missing values. Mark which must be fitted on training data only.

2. A target encoding gives a category with 3 rows an average of 1.0 and a category with 300 rows an average of 0.4. Which is more trustworthy, and how would you smooth it?

3. You build a feature "average sales in the last 7 days" for a model that predicts tomorrow's sales. Explain the shift you must apply and what happens if you forget.

4. A colleague cannot reproduce your model's score from last week. Name five things that might have changed and how you would detect each.

5. Invent three features for a prediction task you know well, and write the sentence each one encodes.
