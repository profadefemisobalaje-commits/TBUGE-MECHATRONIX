# Glossary

**Accuracy** — the fraction of predictions that are correct. Meaningless without a baseline.

**Active learning** — labelling only the examples the model is least certain about, to reduce labelling cost.

**AUC** — the area under the ROC curve; the probability that a randomly chosen positive is ranked above a randomly chosen negative.

**Baseline** — the score of a trivial method, such as the mean or the majority class.

**Bias (statistical)** — error caused by a model too simple to represent the truth.

**Bias–variance trade** — the balance between error from oversimplification and error from sensitivity to the training sample.

**Brier score** — the mean squared difference between predicted probability and outcome; lower is better.

**Calibration** — agreement between predicted probabilities and observed frequencies.

**Class imbalance** — a dataset in which one class is much rarer than another.

**Confusion matrix** — a table of predicted against actual classes.

**Concept drift** — a change in the relationship between inputs and outputs.

**Covariate shift** — a change in the distribution of inputs, with the relationship unchanged.

**Cross-entropy** — the loss used for classification, equal to minus the logarithm of the probability assigned to the true class.

**Cross-validation** — repeatedly splitting the data into training and held-out parts so that every case is tested once.

**Curse of dimensionality** — the loss of meaning of distance, and the growth in data requirements, as the number of features rises.

**Decision tree** — a model that splits data by a sequence of yes-or-no questions.

**Discriminative model** — a model that predicts the target directly, rather than modelling the data's distribution.

**Ensemble** — a model built by combining several models.

**Feature** — a measurable input variable used by a model.

**Feature importance** — a measure of how much a feature contributes to a model's predictions.

**F1 score** — the harmonic mean of precision and recall.

**Gini impurity** — a measure of class mixing in a group, used to choose splits in trees.

**Gradient boosting** — an ensemble built by adding trees that correct previous errors.

**Hyperparameter** — a setting chosen before training, such as tree depth or regularisation strength.

**Imputation** — filling missing values with a substitute.

**Inductive bias** — the assumptions a model makes that let it generalise from finite data.

**Label** — the known answer for a training example.

**Label shift** — a change in the proportion of classes in the population.

**Lasso** — regression with a penalty on the absolute size of coefficients, which can set some to zero.

**Leakage** — information in training that will not be available at prediction time.

**Logistic regression** — a linear model passed through the logistic function to produce probabilities.

**Loss** — the single number a model minimises during training.

**Overfitting** — fitting the training sample so closely that new data suffers.

**Pipeline** — the ordered set of transformations and the model, fitted and applied as one unit.

**Precision** — of the cases predicted positive, the fraction that are correct.

**Precision–recall curve** — precision plotted against recall across thresholds; preferred for rare positives.

**Random forest** — an ensemble of decision trees trained on random samples and feature subsets.

**Recall** — of the actual positives, the fraction that were found.

**Regression** — predicting a numeric value.

**Regularisation** — a penalty on model complexity used to reduce variance.

**Residual** — the difference between prediction and truth for one example.

**ROC curve** — true positive rate against false positive rate across thresholds.

**Stratified split** — a split that preserves class proportions in each part.

**Supervised learning** — learning from examples with known answers.

**Target encoding** — replacing a category with the average outcome for that category.

**Underfitting** — a model too simple to capture the pattern.

**Unsupervised learning** — finding structure in data without labels.

**Validation set** — data used to make modelling decisions, never for final reporting.

**Variance** — error caused by sensitivity to the particular training sample.
