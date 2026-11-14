# AI Systems in the Real World

> Course 1: Introduction to Artificial Intelligence - Chapter 9 of 10

## Opening

By the end of this chapter you can describe the whole life of an AI system — from problem framing to retirement — and name the parts that fail after the model has been trained.

A team builds a defect detector for a factory. The model is excellent: it finds 97% of faulty parts in testing. Six months after launch, the line manager asks for it to be switched off. The camera housing had slowly filled with dust, the lighting was replaced with a different colour temperature, and the model was quietly flagging one part in five as defective, so operators were overriding it constantly, and eventually they stopped looking. The model was never the problem. Everything around the model was. Most AI projects that fail, fail here: not in the maths, but in the space between the maths and the world.

## Big Picture

A working AI system is a chain, and the model is one link. The chain runs: a real problem worth solving, data that represents the world the system will meet, a model trained and tested honestly, an integration that delivers decisions in time, monitoring that notices when the world drifts, and people who know when to override the machine.

Every link has a cost, a failure mode and an owner. The most common mistake in student projects, and in industry, is to spend 90% of the effort on the model and 10% on the chain. The ratio that works is closer to the reverse. This chapter gives you the vocabulary to plan the whole chain, so that your project does not become the defect detector that got switched off.

## Key Words

- **Problem framing** - turning a vague wish into a task with an input, an output and a measure.
- **Data drift** - the real-world data slowly changing away from the training data.
- **Latency** - the time from input to decision.
- **Error budget** - the mistakes a system is allowed to make, by type.
- **Integration** - connecting the model to sensors, actuators, software and people.
- **Monitoring** - watching a live system for drift, errors and silent failure.
- **Human in the loop** - a person who can review or override a decision.

## The Explanation

### Step 1 - Frame the problem before choosing the model

A wish is not a task. "Use AI to improve quality" cannot be built, tested or priced. A framed problem can:

> Detect scratches longer than 2 mm on the painted surface of part X, with a camera at the end of the paint line, and raise an alarm within 200 ms of the part passing the camera. Miss no scratch longer than 5 mm. Accept up to two false alarms per thousand parts.

Notice what the framing added: the object, the defect definition, the sensor, the time limit, the error budget and the acceptable false alarm rate. Every one of those is a decision that changes the design. Without them, you cannot tell success from failure.

Write the framing on one page, and get the person who owns the line to sign it. This single act prevents most later disputes. If a requirement cannot be measured, it is not a requirement, it is a hope.

### Step 2 - Build the chain, not just the model

The model is trained on labelled images. The chain around it has five more parts.

**Sensing.** Is the camera fixed, or does it vibrate? Is lighting controlled? A model trained under one lamp and deployed under another is a model trained on the wrong problem.

**Pre-processing.** Cropping, resizing, colour correction. Every one of these must be identical at training time and at run time. A mismatch here is one of the most common silent failures in deployed vision.

**Inference.** How long does one prediction take? If it is 300 ms and the requirement is 200 ms, the model is unusable no matter how accurate. Measure on the real hardware, not a laptop with a graphics card.

**Decision.** The model outputs a probability. Something must turn that into an action, using a threshold chosen from the error budget. A probability of 0.4 means nothing until someone decides what 0.4 triggers.

**Feedback.** How do operators report a mistake? That report is the only way the system improves, and the only way anyone learns that the world has changed.

| Link | Typical failure | Cheap check |
|---|---|---|
| Sensing | Lighting change, dust | Reference part photographed hourly |
| Pre-processing | Resize mismatch | Log the exact input tensor size |
| Inference | Too slow on real hardware | Time 1,000 predictions on the target |
| Decision | Threshold set for accuracy, not cost | Recompute with the real cost ratio |
| Feedback | No way to report a miss | One button, counted weekly |

### Step 3 - Plan for the day after launch

A model's accuracy is measured on data from the past. The future is different. Paint colours change, a new supplier sends parts with a different surface, the camera ages, the season changes the light through the window.

**Data drift** is the slow divergence of live data from training data. You cannot see it in the model, because the model will keep producing confident answers. You see it in the distribution of inputs, in the rate of alarms, and in operator complaints.

The practical defences are unglamorous:

- Log a sample of every input and every output. Without logs, there is nothing to investigate.
- Track the alarm rate weekly. A sudden doubling is a signal, even if accuracy has not been measured yet.
- Keep a small, freshly labelled set from each month, and score the model on it. This is the only honest measure of current performance.
- Set a review date and a retirement plan. Every model has a useful life, and pretending otherwise is how systems rot.

The factory detector had no logs, no weekly alarm-rate chart and no owner. Each of those would have caught the problem within a week.

## Where It Goes Wrong

**Mistake 1 - Optimising the model and ignoring the deadline.** A 99% accurate model that answers in 2 s is worse than a 94% model that answers in 20 ms when the line moves. *Fix:* put latency in the requirements, then measure it on target hardware.

**Mistake 2 - Training on clean data, deploying in a dirty world.** *Fix:* include the ugly cases in the training set — dust, glare, motion blur, partial occlusion.

**Mistake 3 - No baseline in production.** Nobody knows what the system replaced, so nobody can tell whether it helps. *Fix:* measure the old process for two weeks before switching.

**Mistake 4 - Automating a bad process.** A model that speeds up a broken workflow makes the breakage faster. *Fix:* fix the process first; automate second.

**Mistake 5 - No human override.** An operator who cannot correct the machine will eventually unplug it. *Fix:* design the override first, and count how often it is used.

## Case Note

Hospitals in several countries have deployed sepsis-alert systems that watch patient records and warn clinicians when a patient may be developing sepsis, a fast-moving and often fatal condition. Some of these systems reduced deaths; others were ignored and became background noise.

The difference was rarely the model. Where the alert arrived inside the workflow — on the screen the nurse was already looking at, with a suggested next step — it changed behaviour. Where it arrived as a separate dashboard, or fired so often that clinicians learned to dismiss it, it changed nothing.

The lesson generalises to every robot and every AI product. A prediction is not a decision, and a decision is not an action. Between the model and the outcome sit attention, trust, timing and workload. If you ignore those, you have built a very accurate system that nobody uses. Ask early: who receives this output, at what moment, and what will they do differently because of it?

## Mini-Lab

**You need:** paper and a pen, and one person to interview if possible.

**Do this:**
1. Pick a task in your school, home or workplace that someone does by hand and might be automated.
2. Write the one-page framing: input, output, measure, time limit, error budget, who signs off.
3. Draw the six links of the chain and write the biggest failure risk for each.
4. Estimate the latency allowed. Then think of three ways the world could drift away from your training data.
5. Ask one person who would use the system what they would do differently because of it. If they cannot answer, stop and reframe.

**What you should see:** the framing takes longer than expected, and the answers change the design. That is the point.

**Why it matters:** this is the difference between a coursework demo and a system that survives contact with reality.

## Recap and Questions

**Three things to remember**

1. A system is a chain: problem, data, model, integration, monitoring, people. The model is one link.
2. Frame the problem with a measure, a time limit and an error budget before choosing any method.
3. Drift is normal. Log, monitor and refresh, or the system will quietly fail.

**Check yourself**

1. Your detector finds 99% of defects in the lab and 80% on the line. Name three likely causes.
2. Why is an error budget more useful than a single accuracy target?
3. What would you log on day one, and why would you regret not logging it?

**One thing to try next**

Write the one-page framing for a robot you would like to build. Then show it to someone who is not an engineer. If they can tell you what the robot will and will not do, the framing is good enough to start.
