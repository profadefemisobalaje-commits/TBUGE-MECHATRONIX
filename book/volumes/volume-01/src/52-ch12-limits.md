# What Machines Still Cannot Do

In March 2018, a self-driving test vehicle operated by Uber struck and killed a woman walking a bicycle across a road in Tempe, Arizona. The vehicle was travelling at about 70 km/h in a 65 km/h zone. Its sensors detected the pedestrian several seconds before impact. The software classified the object repeatedly, changing its mind between vehicle, bicycle and other, and its predictions of the object's path moved back and forth. The system's design did not treat “an unknown object in the road” as a reason to slow down. The safety driver was looking away from the road, and the vehicle braked less than a second before impact.

The technical facts of that night are the clearest illustration available of what these systems can and cannot do. The perception worked: something was there, and it was seen. The classification was uncertain, and the system had no policy for acting on uncertainty about *what* a thing is, when the important fact was *where* it is. A human driver who could not identify an object in the road would slow down. The machine had not been taught that hesitation is a form of intelligence.

This chapter is about the specific limits that produce failures like that one, and about the risks that follow when such systems are deployed at scale.

## Pattern Is Not Cause

A model trained on history learns associations. Ice-cream sales rise with drowning deaths; both rise with summer. The association is real, and the causal story is missing a variable.

Associations are enough when you only need to predict. They are not enough when you need to act, because actions change the world in ways the data has never seen. A hospital that learns “patients with this test ordered have worse outcomes” and then orders the test more often will change the population, and the model will be measuring its own effect.

The formal tools for this belong to a later volume, and the instinct belongs here. Before acting on a model's recommendation, ask what would happen if you intervened. If you cannot answer, you have a prediction, not a plan. The cheapest version of the question is the one a good manager asks: “and then what?”

## The World Moves Underneath

Every model is trained on a sample of the world and deployed into a world that keeps changing. The gap has a name, distribution shift, and three common forms.

**Covariate shift.** The inputs change but the relationship does not. A camera's colour balance drifts as the lamp ages; the mapping from image to defect is unchanged, but the images are not.

**Label shift.** The proportions change. A fraud model trained when fraud was one transaction in a thousand meets a season when it is one in fifty.

**Concept drift.** The relationship itself changes. What counted as a good credit risk in 2005 was not a good credit risk in 2009, because the economy had changed and the model had not.

The Tempe crash had an element of all three. Night, unusual lighting, a pedestrian pushing a bicycle rather than walking, and a location with a history of jaywalking. None of these were exotic. They were simply absent, or rare, in the data the system had been tuned on.

The engineering response is not to demand that the world stop moving. It is to measure the inputs as well as the outputs, to keep a labelled sample from each month, and to design the system so that unusual inputs provoke caution rather than confidence. That last one is a design decision, and it is the one that was missing in Tempe.

## Common Sense and Its Absence

Ask a language model for a recipe and it will produce something plausible, well organised and grammatically flawless. Ask it to explain how to cool a sauce quickly and it may suggest putting the pan in the refrigerator, which would warm the fridge, cool the sauce slowly, and possibly warp the pan.

The model has read an enormous quantity of text about cooking. What it does not have is a model of heat, or of what a pan weighs, or of why the fridge door has a shelf that will not take a heavy object. Those facts are rarely written down, because everybody knows them. Text contains what people bothered to say, and people do not bother to say the obvious.

This is the reason a system can be fluent about a subject and wrong about its physics. Fluency is learned from the surface of language; physical intuition is learned from doing things in a world with consequences. Until a system has either, its confident prose should be read as a proposal, not a report.

The practical consequence for engineering is to keep the physical checks separate. A robot that plans a path through a wall should be stopped by a collision checker, not by a better language model. A system that suggests a temperature should have a rule that no temperature above the boiling point of the fluid is acceptable. Rules catch what learning cannot see.

## The Price of the Answer

There is a cost side to all of this that rarely appears in technical papers and always appears in an electricity bill.

Training a large model consumes a great deal of energy. Estimates for the largest models run to hundreds of megawatt-hours for a single training run, before any use at all. Inference — answering a query — costs much less per query, but is paid billions of times. A system that is 2% more accurate and twice as expensive may be a worse product, and a system that cannot run on the device in the customer's hand may be no product at all.

There is a human cost as well. Supervised learning needs labels, and labels are made by people. Some of that work is skilled. Some of it is poorly paid, repetitive, and psychologically damaging: the people who review harmful content so that a model can learn to filter it are exposed to the material that the filter exists to hide.

These costs are not arguments against the technology. They are arguments for counting them. A design that ignores them will be optimised for the metric that was counted and will quietly export the rest.

## Who Answers for It

In 2018, a large technology company abandoned an internal recruiting tool that had been trained on a decade of hiring decisions. The system had learned to favour candidates whose applications resembled those of people who had previously been hired, and because the industry had hired mostly men for technical roles, the tool penalised résumés that contained the word “women's” — as in “women's chess club”. The company said the tool was never used to make final decisions. It was still a system that had learned the past and would have reproduced it with the authority of arithmetic.

Bias of this kind is not a bug in the mathematics. It is the mathematics doing exactly what it was asked: find the pattern in the data. If the data encode a history of exclusion, the pattern is exclusion.

The response has to be structural. Measure outcomes by group, not just in aggregate. Ask whether the label you are predicting is the thing you actually want. Keep a human decision-maker who is accountable for the result. And make the system contestable: a person affected by a decision should be able to ask how it was made and get an answer that is not a shrug.

Accountability is the thread that ties this volume's technical chapters to the ethical ones that follow. A system that decides something about a person is a system that somebody must be able to explain. If nobody can, the system is not ready, however good its score.

## Problems

1. For each of the three forms of distribution shift, invent an example from a system you have used, and say what measurement would reveal it first.

2. The Tempe system changed its classification of the pedestrian several times and had no policy for acting on that uncertainty. Write the policy you would have specified, in three sentences, and say what it would have cost in normal operation.

3. Ask a language model, or a person pretending to be one, for instructions that involve a physical process you understand well — cooking, plumbing, lifting. Find one step that is plausible in prose and wrong in the world. Explain why the training data would not contain the correction.

4. Estimate the energy cost of your own use of an online service for a week, using published figures where you can find them, and stating your assumptions. Then decide whether the service is worth it to you.

5. Write one sentence describing a decision you would not delegate to a machine, and one sentence explaining why. Keep both. In four years, read them again.
