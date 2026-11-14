# Knowledge, Rules and Reasoning

> Course 1: Introduction to Artificial Intelligence - Chapter 5 of 10

## Opening

By the end of this chapter you can write facts and rules in a form a computer can use, trace a chain of reasoning forwards and backwards, and say where rule-based systems break.

A hospital receptionist follows a short list of rules. If a patient has chest pain, call the emergency team immediately. If a patient has a fever and a cough, send them to the respiratory clinic. If neither applies, book a normal appointment. Nobody calls that list "artificial intelligence", yet it is exactly the kind of knowledge that powered the first great commercial wave of AI. Expert systems in the 1980s held thousands of such rules and gave advice on infections, insurance and factory faults. Learning why they worked, and why they stopped, is the fastest way to understand what knowledge actually is.

## Big Picture

A rule-based system has two parts. The **knowledge base** holds facts and rules, written in a form the machine can read. The **inference engine** applies the rules to the facts and produces new facts, over and over, until it reaches a conclusion or runs out of things to do.

The appeal is honesty. Every conclusion can be traced back to the exact rules that produced it, which is why expert systems were trusted in medicine and banking. The weakness is equally clear: the system knows only what someone wrote down. It has no common sense, no ability to notice that a rule does not apply today, and no way to say "I am not sure". Rule-based reasoning gives certainty, and certainty is exactly what the messy real world rarely offers.

## Key Words

- **Knowledge base** - the store of facts and rules.
- **Fact** - a statement known to be true, such as "patient 12 has a fever".
- **Rule** - an if-then statement linking conditions to conclusions.
- **Inference** - the process of deriving new facts from old ones.
- **Forward chaining** - start from the facts and apply rules until nothing new appears.
- **Backward chaining** - start from the question and work back to the facts that would prove it.
- **Conflict resolution** - the rule for deciding which of several applicable rules fires first.

## The Explanation

### Step 1 - Write facts and rules so a machine can check them

A fact is a short statement with a name and arguments:

```
fever(patient12).
cough(patient12).
age(patient12, 34).
```

A rule has a head (the conclusion) and a body (the conditions):

```
urgent(X) :- fever(X), cough(X), age(X, A), A > 60.
```

Read the arrow as "if". If X has a fever, and X has a cough, and X is older than 60, then X is urgent. The variable X stands for any patient. This notation is called a **logic program**, and it is old, small and still useful.

Now add a second rule:

```
respiratory(X) :- fever(X), cough(X).
```

Notice the overlap: every patient who matches the urgent rule also matches the respiratory rule. That is not a bug. It is the normal state of a knowledge base, and it is why you need a policy for conflicts.

The third piece is the **conflict resolution** rule. A simple and defensible policy: specific rules beat general rules, so a patient who matches the urgent rule is sent to emergency even though they also match the respiratory rule. Write that policy down, because a system whose behaviour depends on the order in which rules happen to be stored is a system nobody can explain.

### Step 2 - Reason forwards or backwards

**Forward chaining** starts with what you know and pushes until nothing new can be derived. It is **data-driven**: new information arrives, and you ask what follows.

Take a patient with fever, cough and age 34. Apply the respiratory rule: respiratory(patient12) is now true. Apply the urgent rule: the age condition fails, so nothing. Conclusion: respiratory clinic, not emergency. Two rules checked, one fact added, done.

**Backward chaining** starts with a question and works back. The question is "is patient 12 urgent?" The engine looks for a rule whose head is `urgent(X)`. It finds the one above and sets three sub-goals: fever, cough, age over 60. Fever: true. Cough: true. Age over 60: false because the patient is 34. The answer is no, and the engine can show the exact path that produced it.

Backward chaining is efficient when there are many rules and few questions, because it ignores everything unrelated to the question. Forward chaining is efficient when facts keep arriving and you want to keep conclusions up to date, which is the normal situation in monitoring.

| | Forward chaining | Backward chaining |
|---|---|---|
| Starts from | Known facts | The question |
| Style | Data-driven | Goal-driven |
| Good when | Facts arrive continuously | Few questions, many rules |
| Typical use | Monitoring an alarm system | Diagnosis, configuration |

### Step 3 - Accept the wall: certainty is not enough

The rule above says a 61-year-old with fever and cough is urgent. Fine. Now change one word: what if the patient is 60 years and 11 months? The rule is silent. What if the fever is 37.9 °C and the rule says 38.0? Silent again. Real knowledge does not have sharp edges, and rules do.

Three walls stop rule-based systems:

1. **The knowledge acquisition wall.** Each rule needs an expert to state it, argue for it, and test it. A system with 4,000 rules has millions of possible interactions, and nobody can read them all.
2. **The common-sense wall.** The system does not know that a person cannot be in two places, that water is wet, or that a patient who is asleep cannot answer questions. Everything must be written down.
3. **The uncertainty wall.** Rules are true or false. The world is usually "probably". Pushing probability through rules is possible, but it quickly becomes heavy — which is why Chapter 7 and Course 21 exist.

Modern systems answer these walls with combinations. A rule layer handles the parts that must be auditable, such as "never open the door while the robot is moving". A learned model handles the parts that are fuzzy, such as "is that a person or a coat stand". The engineer's job is to decide which part of the problem belongs to which layer.

## Where It Goes Wrong

**Mistake 1 - Rules that overlap with no priority.** Two rules both apply and the system behaves differently on different runs. *Fix:* write an explicit conflict-resolution policy and test it with overlapping cases.

**Mistake 2 - No defaults.** The system has nothing to say when a value is missing, so it silently treats "unknown" as "false". *Fix:* model unknown as its own state and decide what the system should do.

**Mistake 3 - Sharp thresholds on smooth quantities.** A temperature rule that triggers at exactly 38.000 °C produces a cliff in behaviour. *Fix:* use hysteresis or fuzzy rules (Course 21).

**Mistake 4 - A knowledge base that nobody maintains.** Rules written in 1995 describe a hospital in 1995. *Fix:* give the knowledge base an owner, a review date and a test set of cases that must still pass.

**Mistake 5 - Explaining the trace instead of the reason.** A system that prints forty rule firings has not explained itself. *Fix:* store a natural-language reason with each rule and show the three or four that mattered.

## Case Note

In the 1980s, the computer company Digital Equipment Corporation used an expert system called XCON to configure its VAX computers. A customer order might specify dozens of components, and the components had to fit together physically, electrically and in software. Human specialists took hours and sometimes made expensive mistakes. XCON took minutes and, by the company's own estimate, saved tens of millions of dollars a year.

For a while, XCON was the flagship of a whole industry. Then the trouble started. Each new product line needed new rules. Each rule interacted with rules written years earlier by people who had left. The knowledge base grew into the thousands of rules, and every change risked breaking a configuration nobody had tested. Maintaining it became a specialist job in itself, and the system slowly became a liability rather than an asset.

The system never became wrong. It became expensive to keep right, which in business is the same thing.

There are three lessons here, and they are the reason this chapter treats maintenance as a first-class problem. First, knowledge has a shelf life; products change and rules rot. Second, the interactions between rules grow much faster than the number of rules, so a large knowledge base is a large testing problem. Third, the people who understand the rules must stay involved, because a knowledge base with no owner is a rumour with a database.

Modern systems have the same shape, whether the knowledge is in rules or in weights. Someone must own it, test it, and retire it. Ask any vendor of an "AI solution" who that person will be in your organisation. If the answer is vague, you have found the real cost.

## Mini-Lab

**You need:** paper and a pen, or any text editor.

**Do this:**
1. Write six facts about a broken laptop: it does not turn on, the charger is plugged in, the charger light is off, the battery was flat yesterday, the socket works, the cable is new.
2. Write five rules that could lead to a diagnosis, using the if-then form.
3. Run forward chaining by hand. Number each fact as it is derived.
4. Now ask "is the charger faulty?" and run backward chaining. Count how many facts you had to touch.
5. Deliberately add a rule that contradicts another. Decide which should win, and write down why.

**What you should see:** backward chaining touches fewer facts, forward chaining produces a fuller picture, and the contradiction forces you to make a policy decision that no amount of code can make for you.

**Why it matters:** this is the exact structure of every safety rule in robotics. "If a person is within 0.5 m, stop." You have now built and traced one.

## Recap and Questions

**Three things to remember**

1. A knowledge base is facts plus rules; inference is what turns one into the other.
2. Forward chaining is data-driven, backward chaining is goal-driven, and the choice depends on how the question arrives.
3. Rules give certainty and traceability, and they break on common sense, maintenance and uncertainty.

**Check yourself**

1. A rule says "if battery below 10%, return to dock". The battery sensor fails and reports nothing. What does a naive system do, and what should it do?
2. Give one task in a hospital where a rule is the right tool and one where it is the wrong tool.
3. Why does a 4,000-rule system become hard to test even if every rule is individually correct?

**One thing to try next**

Write the three rules you would put in a robot that shares a corridor with people, choosing only rules whose violation would be unacceptable. Then notice how much of the rest of the behaviour those rules do not cover.
