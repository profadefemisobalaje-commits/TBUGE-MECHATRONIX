# The Shape of a Learning Problem

Two tasks sit next to each other in the same company. The first is deciding whether an incoming email is spam. The second is computing the monthly payroll. Both are done by software; both involve many rules; only one of them should be learned from data.

The difference is not difficulty. Payroll is complicated and tedious, and it is written down in law and in contracts. Every rule can be stated, checked and audited by an accountant. Spam has no such document. Nobody can write the rule that separates a legitimate marketing email from a fraudulent one, because the difference depends on context, language, sender history and a thousand small signals that people recognise but cannot articulate.

That gap — between knowledge that can be written down and knowledge that can only be demonstrated — is where machine learning lives. Everything in this volume follows from taking it seriously.

## Three Kinds of Learning

Learning problems come in three shapes, and the shape decides what you can measure.

In **supervised learning** you have examples with answers. A photograph labelled "cat", a transaction labelled "fraud", a house with a known price. The task is to produce the answer for a new example. If the answer is a category, the task is **classification**. If it is a number, the task is **regression**.

In **unsupervised learning** you have examples without answers. The task is to find structure: groups of similar customers, unusual sensor readings, a smaller set of numbers that captures most of the variation in a table. There is no right answer to compare against, which makes evaluation much harder and makes this the part of the field most often overclaimed.

In **reinforcement learning** you have neither answers nor a fixed dataset. An agent acts, the world responds, and a reward arrives. The task is to learn a policy that collects rewards over time. That is the subject of its own volume, and it is mentioned here only so that the three shapes can be seen together.

| Shape | You have | You produce | Typical task |
|---|---|---|---|
| Supervised, classification | Examples with categories | A category | Spam, defects, diagnosis |
| Supervised, regression | Examples with numbers | A number | Demand, temperature, price |
| Unsupervised | Examples only | Structure | Segments, anomalies, compression |
| Reinforcement | Actions and rewards | A policy | Control, games, routing |

## A Model Is a Guessing Machine With Dials

Strip away the vocabulary and a model is a function with adjustable numbers in it.

A straight line has two dials: a slope and an intercept. A decision tree has a set of questions and thresholds. A neural network has millions of dials. Learning is the process of turning the dials until the function's outputs match the answers you have, as closely as possible, on the examples you have.

The set of functions a model can represent is called its **hypothesis space**, and choosing it is the most consequential decision in the project, because it decides what the model can ever learn.

A straight line can represent a relationship that rises steadily. It cannot represent a relationship that rises, falls and rises again, or one that depends on the interaction of two inputs. A tree can represent sharp thresholds and interactions. It struggles to represent a smooth curve. A neural network can represent almost anything, which is precisely why it can also memorise noise.

The preference for one kind of function over another is called **inductive bias**, and it is not a defect. It is the reason learning works at all. If a model had no bias, every function consistent with the data would be equally acceptable, including the absurd ones, and no amount of data would single out the sensible one. Choosing a bias that matches the world is the craft.

## The Bet at the Centre of It

Here is the uncomfortable heart of the subject. You fit the model to the examples you have, and then you use it on examples you do not have.

The fit is measurable and the future is not. Everything that follows — splitting, validation, regularisation, monitoring — exists to manage that gap and to keep it honest.

Two failures lie on either side.

If the model is too simple for the pattern, it will be wrong on the training data and wrong on new data. It has **underfit**. A straight line through a curve is underfit: it misses the shape and no amount of extra data will fix the choice of a line.

If the model is too flexible, it will fit the training data beautifully and be wrong on new data, because it has learned the particular noise of the sample rather than the pattern underneath. It has **overfit**. This failure is more insidious because the training number looks excellent.

The skill is to sit between the two, and the only instrument that tells you where you are is a set of data the model has never seen. That is why the discipline in Part Three exists.

## Framing: Three Questions Before Any Code

Most failed projects were framed badly rather than modelled badly. Three questions, asked in order, prevent most of it.

**What exactly am I predicting?** "Predict failure" is not a task. "Estimate the probability that this pump will fail within the next 30 days" is. The first has no unit, no horizon and no way to be scored. The second does.

**What will I know at the moment of prediction?** Every column in the table must be available then. A model that uses the repair date to predict repairs is a model that has read the future, and it will score beautifully and deploy uselessly.

**What does a mistake cost?** A missed failure and a false alarm are not the same. Once the costs are written down, the choice of threshold, metric and even model follows from them.

| Vague framing | Usable framing |
|---|---|
| Predict machine failure | Probability of failure within 30 days, from vibration and temperature, for machines under 5 years old |
| Improve customer retention | Probability that a customer cancels within 60 days, from usage and support history |
| Detect anomalies in production | Flag parts whose surface image differs from the reference population, reviewed by an inspector within 4 hours |

The same underlying problem can be framed several ways, and each framing produces a different dataset and a different metric.

Predicting a pump's failure can be **classification** — will it fail in the next month, yes or no? It can be **regression** — how many days until it fails? Or it can be **unsupervised** — is this vibration pattern unusual compared with the fleet? The classification framing needs labelled failures, of which there may be only four in a year. The regression framing needs even more precise labels. The unsupervised framing needs no labels at all, and it will find every unusual pump, including the ones that are unusual because they are new.

None of those is wrong. They answer slightly different questions, and the choice depends on what data exists and what a decision will be made with the answer.

## What Machine Learning Is Not

Two expectations are worth removing before the methods arrive.

It is not a way to avoid understanding the problem. A model can find a pattern in a table without anybody knowing why the pattern exists, and that is fine until the pattern changes, at which point nobody can repair it. The teams that do this well keep a human explanation beside the statistical one.

It is not automatically better than a rule. A rule written by a domain expert is auditable, explainable and free to run. Machine learning earns its place when the pattern is real, large and too complex to write down, and when there is data to prove it. Chapter 13 takes this seriously, and it is one of the most useful chapters in the volume.

## How Much Data Is Enough?

This is the question every project asks first, and the honest answer is a curve rather than a number.

A **learning curve** plots performance against the number of training examples. In most projects it rises steeply for a while, then flattens. The flat part is the signal: adding data there buys almost nothing, and the remaining error is a mixture of irreducible noise and model bias. The steep part is where data is worth collecting, and where a small investment pays.

Two rules of thumb are useful as starting points, not as laws.

For a linear model with a modest number of features, ten to twenty examples per parameter is a common minimum. A model with five coefficients wants at least fifty to a hundred examples, and more if the data is noisy.

For classification, what matters is the number of examples of the rarer class. A dataset with 10,000 rows and 40 positives is a dataset of 40 examples for the purpose of learning what a positive looks like. Flexible models need several hundred positives before their advantage over a simple model shows up.

There is a third consideration that no rule of thumb captures: the number of *distinct situations* the model must handle. A welding dataset from one fixture may need a few hundred images. The same model, applied to twenty fixtures, needs examples from all twenty, because the variation between fixtures is the thing that will break it.

The practical procedure is cheap. Fit your candidate model on 10%, 25%, 50% and 100% of the training data, plot validation performance, and look at the shape. If the curve is still climbing at 100%, collect more data. If it has flattened, collect better features, or accept the floor and move on to deployment.

| Training fraction | Validation score | Interpretation |
|---|---|---|
| 10% | 0.61 | Steep learning |
| 25% | 0.72 | Still climbing |
| 50% | 0.79 | Approaching the plateau |
| 100% | 0.81 | Flattening; data is no longer the constraint |

## Problems

1. For each task, say whether it is classification, regression, unsupervised or not a learning problem at all, and why: sorting mail by postcode; predicting tomorrow's electricity demand; grouping customers by behaviour; deciding whether a photographed weld has a crack; computing interest on a loan; detecting an unusual heartbeat in a patient's recording.

2. Rewrite these three wishes as usable framings with a target, a horizon and a measure: "use AI to reduce downtime", "make our hiring fairer", "predict which students will fail".

3. A model has two dials and is fitted to six points that lie almost on a straight line with a little scatter. Describe what happens if the model has two dials, and what happens if it has six.

4. Name one decision in your own life where you use a rule, and one where you use judgement learned from experience. What makes the first rule-shaped and the second example-shaped?
