# Data: Where It Comes From and What It Costs

A team builds a system that finds cracks in welds. They collect twelve thousand images from one factory, train a model, and reach 98% accuracy. The model is installed on a second production line in another country, where the lighting is different, the camera is a different model, and the welds are made by a different process. Accuracy falls to 61%, and nobody can explain why, because nobody wrote down where the twelve thousand images came from.

Data is the largest cost, the largest source of failure, and the part of machine learning that is least often taught. This chapter is about getting it, understanding what it represents, and being honest about what it does not.

## Four Sources, Four Biases

Data arrives in four ways, and each carries its own distortion.

**Sensors and logs** record what happened. They are cheap, plentiful and mercilessly honest about one thing only: the conditions under which they were installed. A temperature dataset from a factory in one climate is a dataset about that climate.

**Human labelling** attaches answers to examples. It is expensive, inconsistent and indispensable for supervised learning. Two experts often disagree, and the disagreement is itself information: a task where experts agree only 85% of the time cannot support a model judged against a single label.

**Transactions** record decisions that people made: loans approved, candidates hired, claims paid. They are convenient and deeply biased, because they record the outcome of a process that was already selective. A model trained on approved loans learns what the approvers liked, not who would have repaid.

**Purchase** buys you a dataset someone else collected for a different purpose. It is fast and it is usually a poor fit, because the collection decisions were driven by someone else's problem.

The common thread is that a dataset is a record of how it was collected, and the model learns the collection as faithfully as it learns the phenomenon.

## Coverage, and the Sample Is Not the World

The assumption underneath every model is that the future resembles the sample. When that assumption fails, everything else is decoration.

Four kinds of coverage failure matter most.

**Population coverage.** A hospital's model is trained on its own patients. Another hospital serves a different population with different age structure, different languages and different referral patterns. The model's accuracy there is an open question, and the honest answer is "we do not know until we measure".

**Condition coverage.** Photographs taken in daylight; readings taken in summer; transactions from a stable economy. The conditions absent from the data are the conditions in which the model will eventually be asked to work.

**Time coverage.** A model trained on five years of history contains the past's relationships. When a competitor enters, a regulation changes or a pandemic arrives, the relationship moves and the model does not.

**Rare-event coverage.** Fraud, machine failure and serious medical events are rare by definition. A dataset with forty examples of the thing you care about cannot support a model with a hundred parameters, whatever the total row count says.

A useful habit is to write a short **dataset description** before modelling: who or what is in it, where it came from, when, under what conditions, and what is deliberately missing. Google's "Datasheets for Datasets" paper formalised this, and a page of it prevents most surprises.

## Labels Cost More Than You Think

Labelling is usually the dominant cost, and the arithmetic is sobering.

Suppose a weld image takes a trained inspector twenty seconds to label: open, zoom, decide, enter. One thousand images take 20,000 seconds, which is five and a half hours of uninterrupted work. In practice, with context switching and quality checks, plan for eight. For a model that needs twenty thousand labelled examples, that is four months of one person's time, before any review.

The cost changes the design. It pushes teams towards:

**Active learning**, where the model chooses the examples it is least sure about and a human labels only those, which can cut the labelling requirement by a factor of three or four;

**Weak supervision**, where cheaper signals — a maintenance record that says "replaced bearing" — stand in for expensive labels, at the cost of noise;

**Synthetic data**, generated from a simulation or a model, which is cheap and only as good as the simulation's fidelity.

Each of these trades label cost for some other risk, and naming the trade is part of the engineering.

## Cleaning, and the Errors That Survive

Real tables are dirty in predictable ways.

**Missing values** are rarely random. A sensor that fails when hot produces missing readings precisely when the machine is under stress, so deleting those rows deletes the hard cases and flatters the model. Decide explicitly: delete, impute with a median, or add a "was missing" indicator.

**Duplicates** appear when the same record is entered twice or the same image is stored under two names. They inflate the apparent dataset size and, worse, can put the same example in training and test. De-duplicate before splitting.

**Unit and scale errors** are the quiet killer. A temperature column with ninety-nine values in Celsius and one in Fahrenheit; a distance in millimetres among distances in metres. A single such row can dominate a squared-error loss and distort a model without producing an error message. Plot every column before you trust it.

**Outliers** are either errors or the most interesting rows in the table. Deciding which is a domain question, not a statistical one: a pump vibrating at ten times the fleet average is either a broken sensor or a machine about to fail, and only someone who knows pumps can tell you.

## Splitting Is a Design Decision

The train–validation–test split is usually taught as a random 70/20/10. That is one choice among several, and often the wrong one.

| Split | Use when | Why |
|---|---|---|
| Random | Examples are independent and exchangeable | Standard baseline |
| Grouped | Several rows belong to one person, machine or image | Prevents the model learning the group |
| Temporal | The model will predict the future | Mimics deployment, prevents time leakage |
| Stratified | Classes are imbalanced | Keeps the rare class represented in each part |
| By site | The model will be used in another location | Measures transfer honestly |

A medical dataset with several X-rays per patient must be split by patient. A demand model must be split by date, with all training data before all test data. A model destined for another factory should be tested on that factory, or on held-out sites if the data exists.

None of these splits is more sophisticated than the others. Each answers a different question about the world the model will meet, and the right question is the one the deployment will ask.

## Problems

1. You have a dataset of 50,000 support tickets labelled by category, collected over three years. Name three coverage failures you would expect and the effect each would have.

2. Estimate the labelling cost for 8,000 images at 15 seconds each, with a 20% overhead for quality review. How would the number change if active learning cut the requirement by 60%?

3. A colleague deletes all rows with missing sensor values, reducing the dataset from 20,000 to 14,000 rows and improving accuracy from 81% to 88%. Explain what has probably happened and what you would check.

4. You must split a dataset of loan applications from 2015 to 2024. Describe the split you would use if the model is to be deployed next year, and why a random split would mislead you.

5. Write a one-page description of a dataset you can access, real or invented: who is in it, where it came from, and what is missing.
