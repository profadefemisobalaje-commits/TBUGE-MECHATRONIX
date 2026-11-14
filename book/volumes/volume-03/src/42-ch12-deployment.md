# Deployment, Drift and the Long Middle

A model is a snapshot of the world as it was when the data was collected. Deployment puts that snapshot in front of a world that keeps moving. The moment between the end of development and the first month in production is where most of the value of a machine learning project is either captured or lost, and it is the part that courses rarely teach.

This chapter is about the long middle: the years in which a model is running, quietly decaying, and either being maintained or being trusted past its usefulness.

## What Deployment Changes

Three things change the moment a model starts making decisions.

**The population changes.** A model trained on last year's customers meets this year's, and the new ones are different precisely because the model exists. A retention offer changes who stays; a fraud model changes what fraudsters attempt; a screening tool changes who is tested.

**The measurement changes.** In development, labels arrive in a tidy file. In production, labels arrive late, if at all: the failure is confirmed next month, the customer cancels next quarter, the diagnosis comes back from the laboratory. A system that cannot wait for labels must be monitored indirectly.

**The consequences change.** A wrong prediction in a notebook is a wrong number. A wrong prediction in production is a blocked payment, a delayed delivery or an unnecessary inspection, and somebody has to deal with it.

## Getting It Into Service

Two deployment patterns reduce the risk of a bad first month.

A **shadow deployment** runs the new model alongside the old one, without acting on its output, and compares their predictions on live data. It costs computation and nothing else, and it catches mismatches between the training pipeline and the production pipeline before any customer sees them.

A **canary release** sends a small share of traffic to the new model, perhaps 5%, and compares outcomes against the rest. It is the only way to measure the effect of the model on the thing you actually care about, which is rarely the model's accuracy.

Both patterns share a principle: never let a model's first contact with reality be its full workload.

## Three Signals to Watch

A monitoring system needs to watch inputs, outputs and outcomes, because the three fail differently.

**Inputs.** For each feature, track the mean, the spread, the missing rate and the distribution. Compare against the training distribution. A shift in a feature's mean by more than a fraction of its training spread is worth an alert, because it usually means something upstream changed: a sensor replaced, a unit converted, a form redesigned.

**Outputs.** Track the rate of positive predictions, the average score, the distribution of scores. A fraud model that suddenly flags 4% of transactions instead of 0.5% has either found something or broken, and both require a human.

**Outcomes.** When labels arrive, compute the real metrics. This is the only direct measure of performance, and it is always delayed. Until it arrives, the input and output signals are proxies.

Population stability is often summarised with a single number, the **population stability index**, which compares the distribution of a feature in production with its distribution in training. A value below 0.1 is usually unremarkable; above 0.25 is a signal to investigate. The thresholds are conventions, not laws, and the number should be used to prioritise attention rather than to trigger automatic retraining.

## Three Kinds of Drift

The word drift covers three distinct problems, and they need different responses.

**Covariate shift** is a change in the inputs. The relationship between input and output is unchanged, but the inputs are different: a new camera, a different season, a new customer segment. Retraining on recent data usually fixes it.

**Label shift** is a change in the proportion of classes. Fraud rises from 0.2% to 1%. The model may still rank correctly, but any fixed threshold now produces far more alerts, and the threshold must move.

**Concept drift** is a change in the relationship itself. What predicted repayment in 2006 did not predict it in 2009. Retraining on recent data helps only if the new relationship is stable; if the world is changing every month, no model will stay useful for long, and the honest response is to shorten the review cycle.

| Kind | What changes | First symptom | Response |
|---|---|---|---|
| Covariate | Input distribution | Feature drift alerts | Retrain on recent data |
| Label | Class proportions | Alert rate jumps | Recalibrate the threshold |
| Concept | Input–output relation | Accuracy falls with labels | Investigate, retrain, shorten cycles |

## Retraining Without Chaos

A retraining policy is a business process as much as a technical one. It needs three things: a trigger, a gate and a rollback.

The **trigger** is either scheduled, such as quarterly, or conditional, such as an alert on outcome metrics. Scheduled retraining is simple and can waste effort; conditional retraining reacts but can be gamed by whoever sets the threshold.

The **gate** is a comparison on held-out data: the new model must beat the incumbent on the metric that matters, with an allowance for uncertainty. A model that is 0.3 percentage points better on 400 test cases has not been shown to be better at all.

The **rollback** is a stored previous version and a one-command route back to it. Every system that cannot roll back is one bad retraining away from an outage.

Two further practices are worth the effort. Version the data as well as the code, so that a model can be rebuilt exactly. And write a short model card for each release: what it predicts, on what population, with what measured performance, what it must not be used for, and who owns it.

## The Feedback Loop

The most dangerous property of a deployed model is that it changes the data it will be trained on next.

A model that predicts which machines will fail sends inspectors to those machines. The other machines are inspected less, so their failures are recorded later or not at all. The next training set is therefore biased towards the machines the model already flagged, and the model's apparent accuracy improves while its coverage of the fleet quietly narrows.

The same pattern appears in hiring, lending and policing, and it is not a statistical curiosity. It is the system's own success corrupting its evidence.

The defences are deliberate: keep a random sample of cases that the model did not choose, record outcomes for them, and include them in evaluation. A small control group, chosen at random and treated identically, is often the only honest way to know whether a deployed model is helping.

## Alert Fatigue, in Numbers

A model's output is not the end of the system. Someone receives it, and the arithmetic of what they receive determines whether the system survives its first month.

Take a plant performing 2,000 welds a day with a 1.5% defect rate: 30 real defects. The detector catches 85% of them, which is good, and its alerts are right 22% of the time, which is ordinary for a rare event.

| Quantity | Value |
|---|---|
| Welds per day | 2,000 |
| Real defects | 30 |
| Caught | 26 |
| Alerts raised | 118 |
| False alarms | 92 |

Each inspector can properly review 40 alerts per shift. On paper, 118 alerts is three shifts of work, and the plant has one. In practice the queue does something worse than overflow: it teaches people to dismiss.

Within a few weeks the pattern is measurable. Alerts reviewed falls to 60 a day, then 40. The proportion dismissed without inspection climbs past half. Effective recall — the fraction of the 30 defects actually acted on — falls to around 50%, and the model's headline 85% becomes a number that describes nothing anyone does.

There are four repairs, and they are usually applied together.

Raise the threshold, accepting fewer catches in exchange for alerts people believe. Precision of 22% is not a fact of nature; it is a choice of operating point.

Route the cheap cases elsewhere. A low-score part can be inspected later by sampling rather than immediately by a person.

Cap the queue explicitly and report the overflow, so that the system's silence is visible rather than mistaken for safety.

Measure the response, not only the prediction. Log which alerts were reviewed and what the reviewer found. That log is the only honest measure of whether the model is doing anything.

The general lesson is that precision and recall are properties of a model, while workload and trust are properties of a system. A deployment plan that computes only the first pair is planning half a system.

## Problems

1. Design a monitoring plan for a model that predicts equipment failure. Name three input signals, two output signals and the outcome metric, and say how often each is checked.

2. A feature's mean shifts by 0.8 standard deviations. List three possible causes and the check that would distinguish them.

3. Your new model is 1.2 percentage points better on a test set of 300 cases. Compute the standard error of the difference approximately, and decide whether to deploy.

4. Describe the feedback loop for a model that decides which students receive tutoring. How would you collect evidence about the students the model did not choose?

5. Write a model card for a model you have built or used: purpose, population, performance, limitations, owner, review date.
