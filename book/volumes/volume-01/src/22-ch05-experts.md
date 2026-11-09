# What the Experts Knew

Ask a hospital receptionist how they decide where to send a patient and they will give you a list. Chest pain goes to the emergency team, immediately, no discussion. Fever with a cough goes to the respiratory clinic. A sprained ankle at nine in the evening goes to minor injuries, and a sprained ankle at nine in the morning goes to the patient's own doctor. Nobody calls this list artificial intelligence. It is a set of rules, written down by people who know the place, and it works.

The first great commercial wave of artificial intelligence was built on exactly this observation. If a specialist's knowledge can be written as rules, a machine can follow the rules faster, more consistently and without forgetting the awkward case at the end of a long shift. The idea produced systems that genuinely helped, systems that cost millions, and a collapse that took a decade to recover from. All three are worth understanding, because the rule is not dead. It is running the interlock that stops a robot arm when a human enters the cage.

## Two Kinds of Knowing

There is a distinction that runs through this whole book, and it is worth naming plainly.

Some knowledge is *declarative*: it can be written down as statements that are true or false. A patient with a fever above 38 °C and a cough should be tested for influenza. The door must not open while the robot is moving. A tax return filed after the deadline attracts a penalty.

Other knowledge is *procedural* or *statistical*: it lives in examples, in the way an experienced radiographer's eye moves across a scan, in the judgement that a sound is a fault and not a vibration. It is very hard to write down, and very easy to demonstrate a thousand times.

Rule-based systems are built for the first kind. Learning systems are built for the second. Most real problems contain both, which is why the argument between the two approaches has always been less interesting than the engineering that combines them.

## A Very Small Language

A rule-based system has two parts: a **knowledge base**, which holds facts and rules, and an **inference engine**, which applies the rules to the facts and produces new facts.

A fact is a short statement with a name and some arguments:

```
fever(patient12).
cough(patient12).
age(patient12, 34).
```

A rule has a conclusion on the left, an arrow, and conditions on the right:

```
urgent(X) :- fever(X), cough(X), age(X, A), A > 60.
```

Read the arrow as “if”. If X has a fever, and X has a cough, and X is older than 60, then X is urgent. The letter X is a variable that stands for any patient. This notation is old, small, and still used, because it is compact enough for a person to read and precise enough for a machine to execute.

Now add a second rule:

```
respiratory(X) :- fever(X), cough(X).
```

Every patient who matches the urgent rule also matches this one. That overlap is not a mistake; it is the normal state of a knowledge base, and it forces a decision that no amount of code can make for you: when two rules apply, which one wins?

A defensible policy is that specific rules beat general ones, so a patient who matches the urgent rule goes to emergency even though they also match the respiratory rule. Write that policy down. A system whose behaviour depends on the order in which rules happen to sit in memory is a system nobody can explain, and you will be asked to explain it.

## Running the Chain

There are two ways to make a knowledge base do work, and the difference is practical rather than philosophical.

**Forward chaining** starts with what is known and pushes. Take a patient with a fever, a cough, and an age of 34. The engine tests the respiratory rule: all conditions hold, so it adds the fact that the patient is respiratory. It tests the urgent rule: the age condition fails, so nothing is added. Two rules checked, one fact derived, and the answer is the respiratory clinic.

Forward chaining is data-driven, and it suits monitoring, where facts keep arriving and you want the conclusions kept up to date. An alarm system, a stock control system, a robot's safety supervisor: all of these want to be told what is true now and to work out what follows.

**Backward chaining** starts with a question and works back. The question is “is patient 12 urgent?” The engine looks for a rule whose conclusion is urgency. It finds the one above, and sets three sub-goals: fever, cough, age over 60. Fever is known, cough is known, the age condition fails, and the answer is no, with the exact path that produced it.

Backward chaining is goal-driven, and it suits diagnosis and configuration, where there are many rules and few questions. It does not care about anything unrelated to the question, which can save an enormous amount of work.

| | Forward chaining | Backward chaining |
|---|---|---|
| Starts from | Known facts | The question |
| Style | Data-driven | Goal-driven |
| Good when | Facts arrive continuously | Few questions, many rules |
| Typical use | Monitoring, alarms, supervision | Diagnosis, configuration |

## Where the Money Went

The commercial story of the 1980s is worth telling in numbers, because the numbers explain the collapse better than any account of hype.

XCON, the configuration system we met earlier, grew from a few hundred rules to several thousand as the product line expanded. Each new machine needed new components, each component needed constraints on how it could be combined, and each constraint interacted with constraints written years before by engineers who had since left the company. Testing became a branch of its own. The system never became wrong; it became expensive to keep right, and that is the same thing to a business.

MYCIN, the medical adviser, illustrates a different cost. Its knowledge was excellent, and it was never adopted, because adoption depended on typing, hardware, liability and the willingness of busy clinicians to change what they did at three in the morning. The technical work was finished. The system was not.

The general name for the first problem is the **knowledge acquisition bottleneck**. Getting knowledge out of an expert's head and into rules is slow, expensive and iterative, and experts are famously bad at describing what they know. Ask a skilled driver how they hold a lane in wind and they will produce a description that is both incomplete and slightly wrong. Ask them to do it, and they will do it perfectly. This gap between what people can say and what people can do is the reason learning from examples eventually displaced rules for perception and control.

## The Rules That Never Left

It would be a mistake to read this as the defeat of rule-based reasoning. Rules run the parts of the world where certainty is required, and they will keep running them.

Consider the interlock on a robot cell. When a light curtain is broken, power to the motors is cut. There is no probability in this, no training set, no confidence score. The rule is short, the behaviour is total, and it can be tested exhaustively. The same is true of aircraft checklists, railway signalling, payment authorisations above a limit, and the tax rules that compute a bill. In each case, a human must be able to read the logic, argue about it, and prove it was followed.

Rules have three properties that learning systems find hard to match: they are auditable, deterministic and testable case by case. A regulator can read a rule. A court can ask whether it was applied. A test suite can cover every branch. Those properties are worth a great deal in the places where being wrong is expensive, and no accuracy figure substitutes for them.

The modern pattern is therefore a stack rather than a choice. A rule layer handles what must never happen and what must be provable. A learned layer handles the fuzzy perception that tells the rule layer what it is looking at. A planner sits between them, deciding what to do next. When you debug a robot that behaves oddly, the fault is often at the seam between two of these layers, not inside either one.

## Living With Brittleness

Rules have a characteristic failure, and it is worth learning to see it, because it appears in every system that uses thresholds.

The rule above says that a patient of 61 with a fever and a cough is urgent. What about 60 years and 11 months? The rule is silent. What about a temperature of 37.9 °C when the threshold is 38.0? Silent again. Real knowledge does not have sharp edges, and rules do. The result is a cliff in behaviour: nothing happens, nothing happens, and then everything happens at once.

Four defences are worth knowing.

Model the unknown explicitly. If a sensor fails and reports nothing, a naive engine treats “unknown” as “false” and silently concludes that the condition is not met. Give unknown its own state, and decide what the system should do when it cannot tell.

Add hysteresis, as the thermostat did, so that a value hovering at the threshold does not cause the system to chatter between two actions.

Use defaults, but mark them. “Assume the floor is dry unless the humidity sensor says otherwise” is a reasonable default. It becomes dangerous when nobody remembers that it is an assumption.

And where the boundaries are genuinely gradual, consider a system that reasons in degrees rather than in yes and no. That is the subject of fuzzy logic, which gets its own volume later in the programme. The short version: instead of asking whether the temperature is above 38 °C, ask how strongly it belongs to the category “high”, and let several rules contribute in proportion. It is a small change to the machinery and a large change to how gracefully the system behaves near the edges.

## Exercises

1. A laptop will not switch on. You know that the charger is plugged in, the charger light is off, the battery was flat yesterday, the wall socket works with another device, and the cable is new. Write six facts and five rules that could lead to a diagnosis.

2. Run forward chaining by hand on your knowledge base, numbering each fact as it is derived. Then ask “is the charger faulty?” and run backward chaining. Count how many facts you had to touch in each case.

3. Add a rule that contradicts an existing one. Decide which should win, write the policy down, and explain in two sentences why the other choice would be worse.

4. Write the three rules you would put in a robot that shares a corridor with people, choosing only rules whose violation would be unacceptable. Then notice how much of the robot's behaviour those three rules leave undecided.
