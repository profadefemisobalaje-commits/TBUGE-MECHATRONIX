# Limits, Risks and the Road Ahead

> Course 1: Introduction to Artificial Intelligence - Chapter 10 of 10

## Opening

By the end of this chapter you can name the real limits of today's AI, describe the risks that matter, and plan the next four years of your own study with a clear map.

In 2016, a self-driving car failed to see a white lorry crossing a brightly lit road, and the driver, who was not watching, was killed. The sensors worked. The software worked, in the sense that it ran without error. The system had never been shown that combination of a white object against a bright sky at that angle, and it had no fallback for not knowing. That gap — between a system that performs well on average and a system that is trustworthy at the edge — is where the whole field now lives. This chapter is about that gap, and about how the next 47 courses close it.

## Big Picture

Today's AI is powerful, narrow and fragile in specific, predictable ways. It is powerful because scale plus learning works: given enough examples, machines find patterns people cannot write down. It is narrow because those patterns do not transfer outside the data. It is fragile because it fails on inputs unlike anything it has seen, and it fails confidently.

The risks follow directly. A system that fails confidently is dangerous where failure is expensive: medicine, driving, weapons, hiring, policing. A system trained on the past carries the past's biases. A system that optimises a measure will find the cheapest way to satisfy the measure, including ways nobody intended.

None of this is a reason to stop. It is a reason to build with three habits: know the limits, measure at the edges, and keep a human able to see and stop what is happening.

## Key Words

- **Brittleness** - failing badly on inputs slightly different from training data.
- **Distribution shift** - the live world drifting away from the training data.
- **Bias** - a systematic error that disadvantages a group or a situation.
- **Causality** - knowing that one thing makes another happen, not just that they occur together.
- **Alignment** - making a system pursue what its designers actually intended.
- **Accountability** - a named person or organisation responsible for a system's effects.
- **Edge case** - a rare input at the boundary of normal operation.

## The Explanation

### Step 1 - Know what the methods cannot do

Four limits are worth memorising, because you will meet them in every course.

**Limit 1: pattern is not cause.** A model that sees ice-cream sales rise with drowning deaths has found a real pattern and the wrong story. The cause is summer. Models trained on correlation will happily recommend an action that does nothing, or makes things worse.

**Limit 2: the training data is the world, as far as the model knows.** Change the camera, the accent, the dialect, the lighting, the demographic, and performance can fall off a cliff. The model has no way to notice that it is now outside its experience.

**Limit 3: no common sense.** A language model can write a perfect recipe and suggest putting the pan in the fridge to cool the sauce. Large amounts of text do not automatically produce an understanding of physics, time or embarrassment.

**Limit 4: confidence is not calibrated.** A network's 0.99 output is a number produced by arithmetic. Unless you have measured calibration on held-out data, it tells you nothing about the chance of being right.

For each limit, there is an engineering response: use causal experiments where decisions matter, test on shifted data, add rule-based checks for physical impossibilities, and calibrate confidence before anyone acts on it.

### Step 2 - Name the risks in the language of consequences

Risks are easier to handle when they are specific. Consider four categories.

**Safety.** A robot that misjudges a person's position can injure them. The response is a safety layer that does not depend on the learned model: physical bumpers, force limits, speed reduction near people, and an emergency stop that always works.

**Fairness.** A hiring model trained on ten years of decisions by people who favoured one group will reproduce that favour, with the added authority of mathematics. The response is to measure outcomes by group, to ask whether the label is even the right thing to predict, and to keep a human decision-maker accountable.

**Privacy.** Cameras in public and private spaces, microphones in homes, and records that never expire. The response is to collect less, keep it for less time, and be explicit with the people affected.

**Power.** The concentration of capability in a few organisations, and the use of automated systems to make decisions about people who cannot contest them. The response is governance: audit, appeal, transparency and law. You will meet all of this again in Courses 15, 38 and 40.

A useful discipline: for each risk, write the harm, who bears it, and who can prevent it. If the answer to the third question is "nobody", the design is not ready.

### Step 3 - Plan your own path through the next 47 courses

You now know what intelligence means in a machine, where the idea came from, how an agent is structured, how it searches, reasons, learns from data and handles uncertainty, how it sees and hears, and how systems succeed or fail in the real world.

The rest of the book builds the machine, piece by piece:

- **Courses 2–6** give you the physical body, the learning tools, the eyes, the language and the control loop.
- **Courses 7–12** give you the engineering skills: algorithms, signals, embedded code, interaction design, neural networks, graphics.
- **Courses 13–18** connect machines to the world and to each other, and start the ethical conversation properly.
- **Courses 19–24** make robots move, learn, reason with degrees of truth, and compute their own geometry.
- **Courses 25–30** add immersive interfaces, physical-digital systems, teams of robots, software architecture, cognition and biology.
- **Courses 31–36** turn all of it into dependable industrial and social systems.
- **Courses 37–42** push into advanced practice: evolution, ethics as design, learning on real hardware, manipulation, perception.
- **Courses 43–48** finish with navigation, planning, simulation, design and your own capstone project.

A study plan that works: read one chapter in the morning, do the mini-lab in the afternoon, and answer the three questions aloud a week later. Do not read three chapters in one day and none for a month. The book is built for steady repetition, and so is your memory.

## Where It Goes Wrong

**Mistake 1 - Assuming a good average means a safe edge.** *Fix:* test the odd cases on purpose, and report worst-case performance beside the average.

**Mistake 2 - Treating the model as the whole system.** *Fix:* draw the chain from Chapter 9 and give every link an owner.

**Mistake 3 - Believing a confident output.** *Fix:* calibrate the confidence, and never let a single number authorise an irreversible action.

**Mistake 4 - Skipping the ethics because "we are only engineers".** *Fix:* write the harm list. You are the last person who can still change the design cheaply.

**Mistake 5 - Learning tools without learning judgement.** A student who can call a deep learning library but cannot frame a problem will build the wrong thing faster. *Fix:* practise framing, measuring and questioning, which is what this course has been about.

## Case Note

In 2018, a woman in Arizona was struck and killed by a self-driving test vehicle. Investigations found that the software had detected an object but had repeatedly changed its classification — vehicle, other, bicycle — and its predicted path, and the system's design did not give it a way to treat "an unknown object in the road" as a reason to slow down. The safety driver was looking away.

The technical lesson is precise: uncertainty about *what* an object is must not stop the system from acting on *where* it is. A good design slows for anything solid on the road, whatever its label, because the cost of being wrong is not symmetrical.

The wider lesson is about culture. The system had a safety driver because someone had judged the technology not yet ready. That judgement was right, and the safeguard failed because a human was asked to stay vigilant for hours with nothing to do. Vigilance is not a safety system. Engineering is.

## Mini-Lab

**You need:** paper, a pen, and one willing person.

**Do this:**
1. Choose an AI system you use weekly.
2. Write its four limits: where it confuses pattern with cause, where its data is narrow, where it lacks common sense, where its confidence may be uncalibrated.
3. Write one harm it could cause, who bears that harm, and who could prevent it.
4. Design one check that does not depend on the model — a rule, a second sensor, or a human review.
5. Explain the check to your willing person in 60 seconds. Ask them to repeat it back.

**What you should see:** the check is easy to design once the harm is named, and hard to explain if it is vague. Clarity is the test.

**Why it matters:** this is the habit that separates an engineer people trust from one they do not.

## Recap and Questions

**Three things to remember**

1. Today's AI is powerful on average, narrow by design, and fragile at the edges — and it fails confidently.
2. Confidence must be calibrated, and any irreversible action needs a check that does not depend on the model alone.
3. Ethics is design work. The cheapest moment to prevent harm is before the system exists.

**Check yourself**

1. Why is "the model was 99% accurate" not a defence after an accident?
2. What is the difference between a pattern and a cause, and why does it matter for decisions?
3. Name one thing you personally will not build, and the reason in one sentence.

**One thing to try next**

Write a one-page "limits and risks" note for the project you would most like to build. Keep it. In four years, when you build that project for your capstone, read it first.
