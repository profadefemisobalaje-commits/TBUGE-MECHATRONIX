# A Short History of Thinking Machines

> Course 1: Introduction to Artificial Intelligence - Chapter 2 of 10

## Opening

By the end of this chapter you can place any AI system on a timeline, name the idea it depends on, and explain why the field has repeatedly promised too much and delivered in narrow pieces.

In the summer of 1956, a small group of researchers met at Dartmouth College in the United States and wrote a proposal with a remarkable claim: that every feature of intelligence could, in principle, be described so precisely that a machine could simulate it. They expected the work to take a generation. Seventy years later, the work is still going, and the argument about how close we are has not settled. Knowing that story is not decoration. The same three ideas have been fighting for attention since the 1950s, and the argument you hear today is the same argument, with faster computers.

## Big Picture

The history of AI is a repeating loop of four steps: a big promise, real success on narrow problems, a wall where the method runs out of power, and a pivot to a new idea. Three main ideas have taken turns at the front: **rules**, **learning**, and **scale**. Rules say: write down what an expert knows and let the machine follow the rules. Learning says: give the machine examples and let it find the pattern. Scale says: make the network and the data enormous and let the pattern find itself.

Each idea worked brilliantly inside its limits and failed outside them. Each time a wave broke, journalists wrote that AI was finished. Each time, the field quietly kept the useful parts and moved on. Today's systems are not a replacement for the old ideas; they are rules, learning and scale stacked on top of each other. When you debug a modern robot, you will usually find all three in the same program.

## Key Words

- **Turing test** - a test of machine intelligence by conversation, proposed by Alan Turing in 1950.
- **Symbolic AI** - AI built on written rules and symbols, dominant from the 1950s to the 1980s.
- **Expert system** - a program holding a specialist's rules, used in medicine and industry in the 1970s and 1980s.
- **AI winter** - a period of lost funding and lost interest after a wave of promises failed.
- **Connectionism** - the idea that intelligence comes from many simple connected units, the root of neural networks.
- **Deep learning** - neural networks with many layers, trained on large data, dominant since about 2012.

## The Explanation

### Step 1 - The dream and the test (1936-1956)

The story starts with mathematics, not machines. In 1936, Alan Turing described a machine that could compute anything computable by following simple steps on a tape. That gave people a precise meaning for "a procedure a machine can carry out". Once you have that, the question "can a machine think?" stops being poetry and becomes engineering.

Turing's 1950 paper, *Computing Machinery and Intelligence*, did something clever. Instead of defining thinking, he replaced the question with an experiment. Put a person, a machine and a judge in separate rooms. Let the judge type questions to both. If the judge cannot reliably tell which is which, said Turing, we have no good reason to deny the machine intelligence.

That move — replace a hard philosophical question with a testable one — is the pattern of the whole field. It is also the source of endless argument, because a machine can pass the test by being good at conversation without understanding anything, which is roughly what happened seventy years later.

In 1956 the Dartmouth workshop gave the field its name: artificial intelligence. The proposal was confident, the results were thin, and the field was born anyway.

### Step 2 - The rule years, and the first winter (1956-1993)

The first generation believed that intelligence was manipulation of symbols. If you can write down what a doctor knows, you can build a program that diagnoses. This produced real, useful systems: MYCIN advised on bacterial infections in the 1970s and sometimes matched human specialists. Companies built **expert systems** for insurance, mining and factory planning, and for a while the market was enormous.

There were two problems. First, the rules were expensive. A single expert system needed hundreds of rules, each one argued over by specialists, and the rules interacted in ways nobody predicted. Second, the systems had no common sense. A medical system could reason about infections but not notice that a patient was pregnant unless someone had written a rule for it.

The technical blow came earlier. In 1969, Marvin Minsky and Seymour Papert published *Perceptrons*, a careful analysis showing that a simple single-layer network could not compute even the logical function "exclusive or" — a case where the answer is yes if either input is yes, but not both. The result was read, unfairly but widely, as proof that the connectionist approach was dead. Funding for neural networks collapsed; rule-based work continued.

The commercial collapse came in the late 1980s. Expert systems ran on expensive special computers, and when ordinary desktop machines caught up, the economics vanished overnight. Around 1987 the market for those machines crashed. This period is now called the first **AI winter**.

The lesson people took away was "AI overpromises". The lesson the field actually learned was subtler: a method can be correct and still be too expensive to scale.

### Step 3 - The learning years and the deep years (1986-today)

While the rule-based wave was freezing, a different idea was warming up. In 1986, a group of researchers popularised a practical method for training multi-layer neural networks called **backpropagation**. You will meet it properly in Course 11. Its importance here is historical: it removed the objection of 1969. Networks could now learn things a single layer could not represent.

The 1990s shifted attention from hand-written rules to statistics. Instead of asking an expert what the rules are, collect data and estimate the probabilities. This was less glamorous and far more reliable, and it worked in speech, in handwriting, and in credit scoring. In 1997, Deep Blue beat Garry Kasparov at chess using fast search and hand-tuned evaluation, not learning — a triumph of the rules-and-search tradition at the very moment the statistical tradition was taking over.

Then came **scale**. In 2009 researchers released ImageNet, a dataset of over a million labelled photographs. In 2012, a deep network called AlexNet won the ImageNet competition by a large margin, using graphics processors built for video games to train a network with millions of parameters. The pattern was set: bigger networks, more data, more computing power. In 2016, AlphaGo beat a top human player at Go, a game everyone had said was years away. In 2017, a paper called *Attention Is All You Need* introduced the **transformer**, an architecture that handles sequences in parallel. In 2022, chat models built on transformers reached the public and made the argument about AI a household topic.

Notice what did not happen: the old ideas did not die. Chess engines still search. Rule systems still run factories and aircraft. Learning sits on top of both. The history is not a series of replacements. It is a series of additions.

| Period | Dominant idea | Typical success | Typical failure |
|---|---|---|---|
| 1956-1975 | Symbols and search | Puzzles, games, simple proofs | Real-world messiness |
| 1975-1987 | Expert rules | Medicine, configuration, planning | Cost, brittleness, common sense |
| 1987-2012 | Statistical learning | Speech, handwriting, recommendation | Needs labelled data |
| 2012-today | Deep learning at scale | Vision, language, games | Data hunger, opacity, cost |

## Where It Goes Wrong

**Mistake 1 - "AI is brand new".** The ideas are old. *Fix:* date the idea, not the product. A chat model is a 2017 architecture trained on decades-old learning theory.

**Mistake 2 - Reading a winter as a death.** Winters were funding winters, not idea winters. *Fix:* ask what survived each winter. Backpropagation survived the 1970s and won in the 2010s.

**Mistake 3 - Treating a benchmark win as a capability.** Winning a game is not general skill. *Fix:* ask what the benchmark leaves out. A Go program does not know that stones are physical objects.

**Mistake 4 - Believing the current wave cannot fail.** Every wave looked permanent from inside. *Fix:* name the wall. For deep learning, the walls are data, energy, reliability and trust.

**Mistake 5 - Repeating the promise cycle in your own project.** "We will have a general robot in six months" is the Dartmouth proposal again. *Fix:* promise a task, a measure and a date. Then test the measure.

## Case Note

MYCIN was a rule-based system built at Stanford in the 1970s to advise doctors on bacterial infections of the blood. It asked questions, weighed evidence, and recommended an antibiotic. In blind evaluations it performed about as well as human specialists, and better than some junior doctors. It had roughly 600 rules, each argued over by clinicians, and it could explain its reasoning by listing the rules it had used.

It was never used routinely in hospitals.

The reasons were not about accuracy. Doctors did not want to type answers to long lists of questions while a patient waited. The system ran on specialised hardware that most hospitals did not own. Nobody was sure who would be legally responsible if its advice caused harm. And the knowledge base would have needed constant maintenance by experts who had other jobs.

Every one of those obstacles is still with us, in a new form. Today's systems are faster and easier to talk to, but integration, liability, maintenance and trust decide adoption exactly as they did in 1976. This is why Course 1 keeps insisting that a model is not a system, and why Chapter 9 spends its whole length on the chain around the model.

The historical lesson is worth stating plainly: the field has repeatedly produced technology that worked in the laboratory and failed in the world. The failures were rarely mathematical. They were about the human and organisational ground the system had to stand on.

## Mini-Lab

**You need:** paper, a pen, and a ruler.

**Do this:**
1. Draw a horizontal line and mark the years 1940, 1960, 1980, 2000, 2020.
2. Place these on the line: Turing's paper (1950), Dartmouth (1956), the perceptron book (1969), MYCIN (1970s), the expert-system crash (1987), backpropagation (1986), Deep Blue (1997), ImageNet (2009), AlexNet (2012), AlphaGo (2016), transformers (2017), public chat models (2022).
3. Above the line, write the dominant idea at each point: rules, learning, or scale.
4. Below the line, write one wall that the dominant idea hit.

**What you should see:** the walls come roughly every fifteen to twenty years, and each new wave starts by fixing the wall of the last one.

**Why it matters:** you can now predict the shape of the next argument. When someone says a new method will solve everything, ask which wall it removes, and which wall it creates.

## Recap and Questions

**Three things to remember**

1. The field moves in a loop: promise, narrow success, wall, pivot.
2. Rules, learning and scale are additions, not replacements. Modern systems stack all three.
3. Winters were about funding and cost, not about ideas being wrong.

**Check yourself**

1. Why did the 1969 result on perceptrons damage neural network research so much, given that it was a narrow mathematical point?
2. What did the expert-system crash of 1987 teach the field about hardware?
3. Name one thing today's large models cannot do that a rule-based expert system could do in 1980.

**One thing to try next**

Find a news article about AI from five years ago and one from this month. Compare the promises. Write one sentence describing the wall that the older article did not see coming.
