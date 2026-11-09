# Trees, Forests, and the Art of Asking Questions

A maintenance engineer's diagnosis sounds like a tree. If the vibration is above 4 mm/s, look at the bearing. If the bearing is fine, check the alignment. If the alignment is fine and the temperature is above 60 °C, call the supplier. That structure — a sequence of yes-or-no questions, each chosen because it separates the cases well — is exactly what a decision tree learns.

Trees are the most useful family of models for tabular data, and they are the easiest to explain to somebody who does not work in machine learning. That combination, rather than any theoretical elegance, is why they dominate practical work on spreadsheets.

## Splits and Impurity

A tree is built by choosing, at each step, the question that best separates the classes.

"Best" is measured by **impurity**: how mixed the group is. A group that is all one class has zero impurity. A group split evenly between two classes has maximum impurity for two classes, 0.5 by the Gini measure, or 1 bit by entropy.

Take ten welds, five cracked and five sound. The Gini impurity of the whole set is 1 − (0.5² + 0.5²) = 0.5.

Now try a split on vibration, above or below 3 mm/s. Suppose the low group has six welds, one cracked and five sound, and the high group has four, all cracked.

- The low group's impurity is 1 − ((1/6)² + (5/6)²) = 0.278.
- The high group's impurity is zero, because it is pure.
- The weighted impurity after the split is (6/10)(0.278) + (4/10)(0) = 0.167.

The impurity fell from 0.5 to 0.167, a reduction of 0.333.

Now try a split on temperature instead, above or below 50 °C. Suppose each side has five welds, with two cracked on one side and three on the other. Each side's impurity is 0.48, and the weighted impurity is 0.48. The reduction is 0.02 — almost nothing.

The tree chooses vibration, and the arithmetic says why. It then repeats the procedure inside each branch, choosing the best remaining question, until the groups are pure or a stopping rule applies.

| Split | Left group | Right group | Weighted impurity | Reduction |
|---|---|---|---|---|
| Vibration > 3 | 1 of 6 | 4 of 4 | 0.167 | 0.333 |
| Temperature > 50 | 2 of 5 | 3 of 5 | 0.480 | 0.020 |

Entropy gives the same ordering by a different route. The whole set has one bit of uncertainty. After the vibration split, the low group carries 0.65 bits and the high group carries none, giving a weighted 0.39 and an information gain of 0.61 bits. Either measure works; both are greedy, and both look only one split ahead.

## The Tree That Grows Too Far

Left alone, a tree will keep splitting until every training example sits in a leaf of its own. The training error goes to zero and the model becomes a very elaborate way of memorising the table.

Three stopping rules keep it honest, and each has a cost.

**Maximum depth** caps the number of questions. A depth of three to six is often enough for tabular data and produces a diagram a human can read.

**Minimum samples per leaf** stops a split that would leave fewer than, say, five examples in a leaf. It prevents the tree from building a rule around one unusual case.

**Pruning** grows the tree and then removes branches that do not improve validation performance. It is more expensive and usually better.

The failure mode of an overgrown tree is easy to describe and easy to miss: it predicts the training set perfectly, and its performance on new data collapses. The failure mode of an over-pruned tree is the opposite: it is stable, readable and too coarse to capture real structure. The validation set, again, is the only instrument that tells you where you are.

## Why Forests Beat Trees

A single tree is unstable. Move ten rows in the dataset and the first split may change, which changes everything below it. That instability is a source of error, and it can be reduced by averaging.

A **random forest** builds hundreds of trees, each on a different random sample of the data, drawn with replacement; at each split, each tree is allowed to consider only a random subset of the features. The predictions are then averaged, or voted on.

The reason it works is worth stating precisely. Individual trees make errors, and those errors are partly independent, because the trees see different samples and different feature subsets. Averaging many partly independent errors reduces the variance of the average without increasing its bias much. The result is a model that is much more accurate than any of its members and much more stable than a single tree.

The costs are the usual ones. A forest of five hundred trees is five hundred times more expensive to build and to run, it is no longer readable as a diagram, and its predictions are harder to explain. In exchange it is often several points more accurate, which on a defect rate of 3% can be the difference between useful and decorative.

| Model | Training cost | Prediction cost | Readable | Typical accuracy on tabular data |
|---|---|---|---|---|
| Single tree, depth 4 | Low | Very low | Yes | Moderate |
| Single tree, unlimited | Low | Low | No, too large | Poor on new data |
| Random forest, 300 trees | High | High | No | Good |
| Boosted trees | High | Moderate | No | Usually best |

**Gradient boosting**, the other dominant ensemble, builds trees one at a time, each correcting the errors of the previous ones. On tabular data it is usually the most accurate of the classical methods, at the cost of more careful tuning and a greater tendency to overfit if the number of trees is not controlled.

## Feature Importance, and Its Lies

Trees offer a tempting number: **importance**, usually computed from how much each feature reduced impurity across the forest. It is easy to produce and easy to misread.

Impurity-based importance is biased towards features with many distinct values, such as continuous measurements or identifiers. A customer ID will often appear important because it can split the data many ways, not because it predicts anything.

**Permutation importance** is more honest: shuffle one column, measure how much the model's error increases, and repeat. If shuffling a feature destroys performance, it mattered. If it changes nothing, the feature was noise.

Neither measure tells you about causation, and both describe the model rather than the world. A feature can be important because it is a proxy for something else, and a feature can be unimportant because a correlated feature has taken its place.

## Problems

1. Build the first split for a dataset of eight examples with four positives and four negatives. Compute the Gini impurity before and after a split that gives (4 positive, 0 negative) and (0 positive, 4 negative). What is the reduction?

2. Using the same dataset, construct a split that gives (2, 2) and (2, 2). Compute the reduction. Explain why a greedy tree would never choose it, even though it might lead to a better tree overall.

3. Explain in your own words why averaging many unstable models can produce a stable one. What has to be true of their errors?

4. A random forest reports that customer ID is the most important feature. What has probably happened, and what would you do?

5. Draw a three-level decision tree for deciding whether to carry an umbrella, using at most three questions. Then explain what the tree cannot represent.
