# Uncertainty and Probability

> Course 1: Introduction to Artificial Intelligence - Chapter 7 of 10

## Opening

By the end of this chapter you can reason with uncertain evidence, update a belief when new information arrives, and explain why a 99% accurate test can still be wrong most of the time it fires.

A robot in a warehouse is told there is a box ahead. Its distance sensor says 1.2 m. The sensor is good, but not perfect: sometimes it reads short when the floor is shiny. Does the robot stop? A rule cannot answer, because the sensor has not given a fact. It has given evidence. Almost everything a robot receives is evidence, not fact, and the mathematics for turning evidence into belief is probability. This chapter gives you the one formula you will use for the next forty courses.

## Big Picture

Probability is a way of writing down how strongly you believe something. Belief starts from what you already knew — the **prior** — and is updated by new evidence using **Bayes' rule**. The update is not a guess; it is arithmetic.

The key insight is that evidence is only meaningful compared with how often it happens by chance. A smoke alarm that goes off during cooking is not strong evidence of fire, because it goes off during cooking often. A smoke alarm that goes off at 3 a.m. in a hotel is strong evidence, because that is rare. Bayes' rule is simply the discipline of comparing those two rates. Once you have it, you will spot bad reasoning in newspapers, medical leaflets and AI marketing for the rest of your life.

## Key Words

- **Uncertainty** - the state of not knowing something for certain.
- **Probability** - a number from 0 to 1 saying how likely an event is; 0 is impossible, 1 is certain.
- **Prior** - the belief before seeing new evidence.
- **Likelihood** - how probable the evidence is if the hypothesis is true.
- **Posterior** - the updated belief after seeing evidence.
- **Base rate** - how common the condition is in the population.
- **Bayes' rule** - the formula for turning a prior and a likelihood into a posterior.

## The Explanation

### Step 1 - Treat sensor readings as evidence

Start with the simplest possible statement: the sensor is right 90% of the time. That gives two numbers that engineers call the **sensitivity** and the **false positive rate**, and they are not the same thing.

- If a box is there, the sensor says "box" 90% of the time. (Sensitivity 0.9)
- If no box is there, the sensor says "box" anyway 10% of the time. (False positive rate 0.1)

Now the critical question that everyone forgets: how often is there actually a box? In a busy aisle, maybe 1 in 10 readings has a real box. This is the **base rate**, and without it the other two numbers mean nothing.

Suppose 1,000 readings: 100 real boxes, 900 empty stretches. The sensor catches 90 of the boxes. It also raises 10% × 900 = 90 false alarms. So when the sensor says "box", there are 90 true and 90 false — a 50% chance. A "90% accurate sensor" has produced a reading that is right half the time.

That is not a paradox. It is arithmetic, and it is why robots use several sensors instead of trusting one.

### Step 2 - Update belief with Bayes' rule

Bayes' rule in words: the belief after the evidence is proportional to the belief before it, multiplied by how well the evidence fits.

```
P(box | reading) = P(reading | box) × P(box) / P(reading)
```

Fill in the numbers above. P(reading | box) = 0.9. P(box) = 0.1. The total probability of a "box" reading is the true ones plus the false ones: 0.9 × 0.1 + 0.1 × 0.9 = 0.09 + 0.09 = 0.18.

So P(box | reading) = 0.09 / 0.18 = 0.5.

The belief went from 0.1 before the reading to 0.5 after it. That is a big jump, and it is still not enough to stop a forklift. This is exactly right: one sensor moved the belief, and did not settle the question.

Now add a second, independent sensor with the same rates. Run Bayes again with 0.5 as the new prior:

P(box | second reading) = (0.9 × 0.5) / (0.9 × 0.5 + 0.1 × 0.5) = 0.45 / 0.5 = 0.9.

Two readings, each 90% reliable on its own, produce a 90% belief. Three would take it above 97%. This is **sensor fusion**, and the arithmetic you just did by hand is the core of Course 14.

### Step 3 - Choose actions under uncertainty, not certainties

A robot never gets to act on perfect knowledge. It gets to act on a belief, and the right action depends on the cost of being wrong.

Suppose the robot can stop (cost: 2 seconds of delay) or continue (cost: a collision, which is unacceptable). With a 0.5 belief, continuing is reckless. With a 0.97 belief, stopping wastes time. Somewhere between, there is a threshold, and that threshold is set by the consequences, not by the probability alone.

You can compute a simple version. Let the delay cost be 2 units and a collision cost 1,000 units. Continuing has expected cost 1,000 × (1 − p). Stopping has expected cost 2. Continue only when 1,000 × (1 − p) < 2, that is, when p > 0.998. A 99.8% belief is needed before moving, which sounds extreme and is exactly why robots slow down near people rather than trusting a single reading.

This one calculation explains a design habit you will see everywhere in robotics: safety systems lower the robot's speed and increase its sensing when uncertainty rises. They do not argue with the probability. They change the physics.

## Where It Goes Wrong

**Mistake 1 - Ignoring the base rate.** "The test is 99% accurate" sounds decisive until you learn the condition affects 1 in 10,000 people. *Fix:* always ask how common the thing is before believing a positive result.

**Mistake 2 - Treating dependent evidence as independent.** Two cameras on the same bracket, both blinded by the same sun, are not two independent readings. *Fix:* ask what could fool both at once.

**Mistake 3 - Reporting a probability without a decision rule.** "There is a 30% chance of a person" is not an instruction. *Fix:* pair every probability with the action threshold it triggers.

**Mistake 4 - Confusing "probable" with "frequent".** A single event, such as this specific bridge failing, has no long-run frequency. Probability here is a degree of belief, and that is fine, as long as you say so.

**Mistake 5 - Overconfidence from a model.** A neural network that outputs 0.99 is not necessarily right 99 times in 100. *Fix:* measure calibration on held-out data before trusting a confidence number.

## Case Note

In the early hours of 29 March 2019, a Boeing 737 MAX crashed shortly after take-off, killing all 157 people on board. It was the second crash of the type in five months. Investigators found that a software system had been repeatedly pushing the aircraft's nose down, driven by a single angle-of-attack sensor feeding it incorrect data. The system had no independent cross-check of that sensor, and the pilots had not been told it existed.

The engineering lesson is not "software is dangerous". It is narrower and more useful: a decision built on one noisy measurement, with no second source and no way for a human to see the disagreement, will eventually act on a false reading. Bayes' rule tells you the fix in advance. Two independent readings take a 50% belief to 90%. A third takes it to 97%. The cost of the extra sensor is small next to the cost of a wrong decision.

Whenever you design a system that acts on evidence, ask three questions. How reliable is each source? Are the sources independent? Can a human see what the system believes and why? The first two are arithmetic. The third is design, and it is the one that saves lives.

## Mini-Lab

**You need:** paper, a pen, and a calculator.

**Do this:**
1. A factory alarm has sensitivity 0.95 and a false positive rate of 0.05. A fault occurs in 2% of production runs.
2. Imagine 10,000 runs. How many have a fault? How many true alarms? How many false alarms?
3. Compute P(fault | alarm) with Bayes' rule.
4. Now improve the sensor so the false positive rate drops to 0.01. Recompute.
5. Decide: above what belief would you stop the line, if stopping costs 1,000 units and a missed fault costs 50,000?

**What you should see:** the base rate matters as much as the sensor quality, and halving the false alarm rate changes the answer more than improving sensitivity would.

**Why it matters:** this is the arithmetic behind every alarm, every safety interlock and every "the AI is 99% confident" claim you will meet.

## Recap and Questions

**Three things to remember**

1. Sensors give evidence, not facts. Belief = prior updated by likelihood.
2. The base rate decides whether a positive result is impressive or ordinary.
3. Independent evidence multiplies belief; dependent evidence does not. Actions follow costs, not probabilities alone.

**Check yourself**

1. A test is 99% sensitive with a 1% false positive rate. One person in 1,000 has the condition. Roughly what is P(condition | positive)?
2. Why are two cameras on the same bracket weaker evidence than two cameras at opposite ends of the robot?
3. Your robot is 60% sure a doorway is clear. What else do you need before deciding to pass through it?

**One thing to try next**

Take any screening test you have read about — a medical test, a spam filter, a fraud check — and find its sensitivity, its false positive rate and the base rate. If any of the three is missing, you now know the claim cannot be judged.
