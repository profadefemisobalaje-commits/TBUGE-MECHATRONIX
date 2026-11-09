# When Machine Learning Is the Wrong Tool

A team is asked to build a model that decides whether a payment should be blocked. The rule that governs the decision is written in regulation, and it must be applied identically to every customer, in a fixed order, with a reason recorded. Nobody wants a model for that. They want the rule, implemented carefully, with an audit trail.

Knowing when not to use machine learning is a mark of competence, and it is rarely taught because the enthusiasm of the field runs the other way. This chapter is a set of questions to ask before the first line of code.

## Four Questions

**Is the pattern real and stable?** If the relationship between inputs and outcomes changes faster than the model can be retrained, learning is a treadmill. Some domains are stable — the physics of a bearing, the optics of a lens — and some are not, such as fashion, fraud and markets. Ask how long the relationship has held and what would break it.

**Is there enough data, of the right kind?** Enough means enough examples of the thing you are predicting, not enough rows in total. Forty machines and six failures is not a dataset for a flexible model; it is a dataset for a rule written by the person who maintains the machines.

**Does the decision tolerate being wrong in a measurable way?** A model that is 85% accurate is useful when the cost of mistakes is small and recoverable, and unacceptable when a single mistake is fatal and irreversible.

**Can the decision be explained to the person it affects?** In credit, employment, insurance and medicine, laws increasingly require a reason. A model can sometimes supply one, but a rule always can.

If any of these answers is uncomfortable, the simpler alternative is usually better, and it is always cheaper.

## The Alternative Toolkit

Machine learning is one tool among several, and the others are often better.

**Rules** are the right choice when the knowledge is documented, the decision must be auditable, or the cost of an error is extreme. A safety interlock, a tax computation, a clinical protocol. Rules are cheap to run, easy to test exhaustively and easy to change.

**Lookup tables and thresholds** handle a surprising share of industrial decisions. A part is rejected if its measurement is outside a tolerance set by engineering, and the tolerance is derived from the function of the part, not from a dataset.

**Optimisation** is the right tool when the question is "what is the best allocation" rather than "what will happen". Scheduling, routing and packing are optimisation problems, and a model that predicts demand feeds the optimiser rather than replacing it.

**Simulation** answers "what happens if" when no data exists for the situation, as it often does not for a machine that has never failed.

**Statistical process control** detects that something has changed in a process, using a handful of numbers and a chart, and it does so with a transparency that a model cannot match.

**A person** is the right answer when the decision requires judgement, context or accountability that cannot be delegated. The useful question is not whether to automate the whole decision, but which part of it to automate.

| Situation | Better tool than ML |
|---|---|
| Decision must be audited line by line | Rules |
| Only a few dozen examples exist | Rules or expert judgement |
| Question is how to allocate a fixed resource | Optimisation |
| Situation has never occurred | Simulation |
| Need to know a process has shifted | Control charts |
| Decision carries legal accountability | Human, with ML as advice |

## The Case of the Tiny Dataset

There is a recurring fantasy that a clever model can extract a pattern from almost no data. Sometimes, with strong prior knowledge and a very small model, something can be learned. Usually what happens is that the model memorises the examples and the team mistakes this for insight.

A useful test: hold out two examples out of ten and see whether the model predicts them. It usually does, and the result is meaningless, because the model saw eight and was fitted until it agreed with them.

With tiny data, the honest approaches are: use a model with two or three parameters, such as a threshold or a line; use domain knowledge to constrain the model; collect more data before modelling; or accept that the decision is a judgement call and support it with a transparent calculation rather than a fitted model.

## The Case of Causation

A model trained on observational data learns associations. When the decision changes the world, the association may not survive the change.

A hospital observes that patients who receive a particular test have worse outcomes, and concludes that the test is harmful. In fact, doctors order the test for patients they are worried about, so the test is a marker of severity rather than a cause. A model that recommends reducing the test would be confidently wrong, and the harm would fall on the patients the doctors were right to worry about.

The question to ask before acting on any model is: if I intervened and changed this input, would the outcome change, and in which direction? Without an experiment or a causal model, the honest answer is often "we do not know", and a decision that changes people's lives should not be built on an unknown.

## Model Plus Rule

The most common industrial arrangement is not a model instead of a rule. It is a model and a rule, each doing the part it is good at.

Consider a weld inspection cell. A vision model scores each image for porosity. A geometric check measures bead width and flags anything outside a tolerance that the process engineer can justify from first principles. Neither is a substitute for the other: the model sees texture the rule cannot express, and the rule sees a physical limit the model has never been taught to respect.

The combination has a shape worth naming: the model proposes, the rule constrains.

| Configuration | Recall | Precision |
|---|---|---|
| Rule alone | 60% | 48% |
| Model alone | 88% | 30% |
| Model, then rule as veto | 80% | 55% |

The third row costs eight points of recall and gains twenty-five points of precision, which is usually the better trade, because the veto removes exactly the class of error people find least forgivable: confident nonsense about a part that is visibly wrong by measurement.

Three design details make the pattern work.

The rule must be independently justified. If the geometric tolerance was itself tuned against the same labels, the combination is one model wearing two hats, and the agreement between them is meaningless.

The veto must be logged. Every case where the rule overrides a high model score is a case where the model was wrong about something checkable, and a run of them is the earliest signal of drift available.

The arrangement must fail safe. If the camera fails, the rule must still run, and the line must stop rather than pass parts on the strength of a missing score.

The same pattern appears far from factories. A language model proposes a reply and a rule blocks it if it contains an account number. A credit model scores an applicant and a policy declines anyone with a recent default. In every case the rule is doing work the model cannot do reliably — enforcing a commitment that is not in the training data — and the model is doing work the rule cannot express.

## A Closing Checklist

Before building, answer these six questions in writing. They take twenty minutes and save months.

What decision will this model change, and who makes that decision today?

What is the target, in one sentence, with a horizon and a unit?

What would I know at prediction time, and does the data contain any of it by accident?

How many examples of the outcome do I have, and is that enough for the model I intend to use?

What does each kind of mistake cost, and what threshold follows?

If this model works perfectly, how would the world change, and who would notice it was wrong?

If any answer is "we will work that out later", the project is not ready. The later is where the budget goes.

## Problems

1. For each decision, choose between machine learning, a rule, optimisation, simulation, or a human: rejecting a part outside tolerance; deciding a delivery route; approving a mortgage; predicting demand for a new product; deciding whether a machine needs maintenance; deciding whether a patient needs surgery. Justify each in one sentence.

2. You have 60 labelled examples and 12 features. Write the argument you would make to a manager who wants a gradient-boosted model, and the alternative you would propose.

3. Construct a plausible example, from a domain you know, where a model's input is caused by the outcome rather than causing it. Explain how the mistake would show up in deployment.

4. Write the six-question checklist for a project you would like to do, answering each honestly. If you cannot answer one, say what you would need to find out.
