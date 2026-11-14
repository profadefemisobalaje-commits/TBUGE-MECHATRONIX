# What Intelligence Means in Machines

> Course 1: Introduction to Artificial Intelligence - Chapter 1 of 10

## Opening

By the end of this chapter you can say what intelligence means in a machine, test that claim with a task and a number, and explain why "AI" keeps changing its meaning.

In 1997, a computer called Deep Blue beat the world chess champion. People said it was a great day for artificial intelligence. Ten years later, the same program running on a free phone app was described as "just a chess engine", not as intelligence at all. Nothing about the program had changed. Only our expectations had. This happens every few years, and it will happen to you too. It is the first thing you need to understand before you write a single line of AI code.

## Big Picture

Intelligence, in this book, is not a mysterious substance inside a head. It is a **behaviour**: the ability to choose actions that reach a goal, in situations you have not seen before. A calculator is fast but it never chooses. It does exactly what it is told. A self-driving car chooses — sometimes badly, but it chooses — and that difference is the whole subject.

When we say a machine is intelligent, we mean three things at once. It can **sense** something about the world. It can **decide** what to do. It can **act**, and then see what happened. Sensing, deciding and acting in a loop, in an uncertain world, is the core of every system in this book, from a robot arm to a language model.

This definition has a useful side effect. It makes intelligence something you can measure. If intelligence is behaviour, then you can build a test, run it, and count. You do not have to argue about whether the machine "really understands". You can ask a much better question: on this task, with this measure, how well does it do compared with a person, and compared with a stupid guess?

## Key Words

- **Intelligence** - the ability to choose actions that reach a goal in unfamiliar situations.
- **Artificial intelligence (AI)** - the study and construction of machines that sense, decide and act.
- **Agent** - anything that senses its world and acts on it. A robot is an agent. So is a spam filter.
- **Narrow AI** - a system that is good at one task and useless outside it.
- **General AI** - a system that can handle any task a person can. No such system exists today.
- **Baseline** - the score a stupid, simple method gets. Every intelligent result must be compared with it.
- **The AI effect** - the habit of calling a solved problem "not really AI" once it works.

## The Explanation

### Step 1 - Intelligence is behaviour you can see

Think of two people. One has memorised the bus timetable and recites it perfectly. The other has never seen the city, has no map, and is dropped in a strange street with a phone that has died. The first person is impressive. The second person finds their way home by asking, remembering landmarks and trying streets. Which one would you call intelligent?

Most people pick the second, because intelligence shows up when the situation is new. That is why the definition stresses *unfamiliar situations*. A system that works only on the exact data it was trained on has not shown intelligence. It has shown memory.

This gives us a practical test with three questions:

1. What can the system sense?
2. What actions can it choose from?
3. In how many *new* situations does it still reach the goal?

A chess engine senses the board and chooses a move. Inside chess it is extraordinary. Outside chess it cannot do anything, because its sensors and actions exist only on a board. That is **narrow AI**, and almost everything you will meet in this book is narrow.

### Step 2 - The same machine, a different name

AI has a strange habit: as soon as a problem is solved, we stop calling it AI.

Optical character recognition — turning a photo of text into typed letters — was a research triumph in the 1980s. Today it happens in your phone's camera app and nobody calls it AI. Route finding was a landmark of the 1960s. Today your maps app does it and you call it "the maps app". Speech recognition was a career's work. Today it is a small button.

This is **the AI effect**. There are two reasons for it. First, once we understand how something works, it stops feeling magical; it becomes engineering. Second, marketing language moves on to whatever is not yet solved, because that is where attention and money are.

The practical lesson: never accept the label "AI" as evidence of anything. Ask what the system senses, what it can do, and how it was tested. A system called "AI-powered" may be three rules in a spreadsheet. A system called "a sorting script" may contain a serious neural network.

### Step 3 - Measure it, or it means nothing

Suppose you build a filter that decides whether an email is spam. You test it on 1,000 emails and it is right 90% of the time. Is that good?

You cannot tell yet, because you do not know the **baseline**. Imagine that only 100 of the 1,000 emails are spam, and 900 are normal. A filter that says "not spam" to everything — a filter with no intelligence at all — is right 900 times out of 1,000. That is also 90%. Your clever filter has learned nothing that a brick could not do.

This is why the book insists on a baseline in every experiment. The baseline is the number a lazy method gets, and it is often shockingly high.

| Method | Correct out of 1,000 | Accuracy |
|---|---|---|
| Say "not spam" always | 900 | 90% |
| Say "spam" always | 100 | 10% |
| Your first filter | 900 | 90% |

Now look at the spam itself, not the whole pile. The filter catches 60 of the 100 spam emails and wrongly blocks 30 normal ones. In the spam group, it is right 60% of the time. In the normal group, it is right (900 − 30)/900 = 96.7% of the time. Those two numbers tell a completely different story from "90% accurate". A filter that misses 40 of every 100 spam emails, and blocks 30 real messages, would annoy most users.

So we never report one number. We report the score, the baseline, and the mistakes by type. Only then does "90%" mean anything.

A useful habit: when someone shows you a result, ask three questions. What is the baseline? What is the worst mistake this system can make? Who paid for the test? The third question is not cynicism. It is how you find out which cases were left out.

## Where It Goes Wrong

**Mistake 1 - Thinking AI means "like a human".** A system can be superhuman at one task and hopeless at everything else. Deep Blue beat a champion and could not tell you what a chair is. *Fix:* describe what the system does, not what it resembles. Say "a chess-playing program", not "a thinking machine".

**Mistake 2 - Trusting a single accuracy number.** As the spam example shows, 90% can mean "does nothing". *Fix:* always compute the baseline first, then split the errors by type.

**Mistake 3 - Confusing automation with intelligence.** A washing machine runs a fixed cycle. It senses almost nothing and chooses nothing. It is automatic, not intelligent. *Fix:* use the three questions — what does it sense, what can it choose, how does it do in new situations?

**Mistake 4 - Believing the field is new.** The questions were asked in the 1950s. Only the computing power and the data are new. *Fix:* read Chapter 2 before making claims about what is unprecedented.

**Mistake 5 - Letting the demo stand in for the product.** A video of a robot walking on a smooth floor says nothing about stairs, rain or mud. *Fix:* ask for the failure rate, on which data, measured by whom.

## Case Note

In 2016, a group of researchers asked a simple question about image classifiers: why did the model say "wolf"? They took a network that appeared to tell huskies from wolves with high accuracy and analysed which parts of each picture pushed the decision. The answer was uncomfortable. The network was not looking at the animal at all. It was looking at snow. Almost every wolf photograph in the dataset had been taken outdoors in winter, so "snow on the ground" predicted "wolf" almost perfectly. Husky photographs, mostly taken indoors or in summer, had no snow.

The model was accurate on the test set, because the test set was drawn from the same photographs with the same accidental shortcut. It would have failed on a wolf photographed in a desert, and it would have failed on a husky standing in snow. Nobody had checked, because the number looked good.

This is the clearest possible illustration of this chapter's definition. The system was not intelligent in any useful sense. It had found a correlation that happened to hold in one collection of pictures, and it would have broken the moment the situation changed, exactly as the definition in the Big Picture section predicts.

The lesson for your own work: whenever a model performs surprisingly well, ask what it could be using that you did not intend. Then design a test where that shortcut is unavailable. If performance collapses, you have found the shortcut, and you have learned more than a hundred more training examples would have taught you.

## Mini-Lab

**You need:** paper, a pen, and 20 short messages (or just the table below).

**Do this:**
1. Write down five "AI" systems you used this week. Next to each, fill three boxes: what it senses, what it chooses, what counts as its goal.
2. Mark each one narrow or general.
3. Imagine a test for the first one. Write the task, the measure, and a stupid baseline that uses no learning at all.
4. Predict the baseline score before you imagine the clever system's score. If your clever system does not clearly beat the baseline, your test is too easy.

**What you should see:** at least one system you thought was intelligent turns out to sense almost nothing, and at least one "boring" system — a maps app, a photo organiser — turns out to be doing serious sensing and choosing.

**Why it matters:** you have just done the first real job of an AI engineer. Not building a model. Deciding what would count as success.

## Recap and Questions

**Three things to remember**

1. Intelligence is behaviour: sensing, deciding and acting to reach a goal in new situations.
2. The AI effect means the label "AI" proves nothing. Look at the sensing, the actions and the testing.
3. A score without a baseline is not a result.

**Check yourself**

1. A program predicts tomorrow's weather correctly 70% of the time. What is the baseline, and why does it matter?
2. Give one system that is automatic but not intelligent, and one that is intelligent but not automatic. Explain the difference in one sentence each.
3. Your robot vacuum cleans 95% of the floor area it covers. Why is that number not the same as "cleans 95% of your home"?

**One thing to try next**

Take the last "AI" advertisement or news story you saw. Write its claim in the three-question form: what does it sense, what does it choose, how was it tested? You will be surprised how often one of the three boxes is empty.
