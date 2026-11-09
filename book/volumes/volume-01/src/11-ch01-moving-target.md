# The Moving Target

On 11 May 1997, in the Equitable Center in Manhattan, a machine called Deep Blue beat Garry Kasparov in the sixth and final game of a match. Kasparov was the reigning world chess champion. Deep Blue was a pair of refrigerator-sized cabinets built by IBM. The match had drawn worldwide attention for two weeks; the prize was more than a million dollars; the front pages treated the result as a turning point in the relationship between people and their tools.

Ten years later, a chess program that could beat almost any human grandmaster ran on a laptop, and grandmasters used it to prepare rather than fearing it. Twenty years later it ran on a phone, silently, inside an app that also told you what time the tide came in. Nothing about the program had become less capable. Quite the opposite: the phone version was stronger than Deep Blue. It had simply stopped being remarkable, and once a thing stops being remarkable, we stop calling it intelligent.

This is the first fact about artificial intelligence, and the one that causes the most confusion. The word does not describe a fixed property that a machine either has or lacks. It describes a boundary that keeps moving. Whatever the field manages to build gets reclassified as ordinary engineering, and the name moves on to whatever is still unsolved. Optical character recognition was a triumph in the 1980s and is now a camera feature. Route finding was a landmark of the 1960s and is now a blue line on a map. Speech recognition took fifty years and is now a button.

If you take nothing else from this chapter, take this: the label tells you almost nothing. If you want to know what a system can do, you have to look at the system.

## Judging by What a Thing Does

Philosophers have argued for centuries about what intelligence is, and the argument is not over. This book takes a different route, on purpose. It treats intelligence as a way of behaving, not as an inner substance.

The definition we will use is plain: **intelligence is the ability to choose actions that reach a goal in situations you have not seen before**. Three pieces of that sentence matter. There is a goal, so there is a difference between success and failure. There is a choice, so the thing is not merely following a script. And there is novelty, because a system that works only on the exact situations it was built for has demonstrated memory, not intelligence.

Test it on three machines. A calculator is fast and never chooses; it does exactly what it is told, and it would do the same thing in any situation. A chess engine chooses, but only among moves on a board, and its world is perfectly known; it is intelligent inside a very small box. A self-driving car chooses among steering and braking actions, in a world that is partly hidden, moving and full of people; it is doing something much more like what a person does, and it is much worse at it than a person is.

The definition also gives you a way to ask useful questions. For any system, ask: what can it sense? What actions can it choose from? What counts as the goal? And how many situations outside its training ground can it handle? Four questions, and you can answer them for a spam filter, a factory arm, a hospital triage tool or a chat assistant.

These are deliberately the same four questions an engineer asks when writing a design specification. That is not an accident. In this book, intelligence is not a mystery to be admired. It is a property of a system, and properties of systems can be specified, built, measured and improved.

## What the Word Hides

There are two temptations when reading about artificial intelligence, and both come from taking the name too seriously.

The first is to imagine that a system which is impressive in one place will be impressive in another. It will not. The chess engine that beat the world champion could not tell a chair from a table. It could not recognise a chessboard in a photograph, or explain its moves to a beginner, or play any other game without being rebuilt. The technical word for this is narrowness. Almost every system you will meet in this book is narrow: excellent inside its task, helpless outside it.

The second temptation is the opposite one: to hear that a system is narrow and conclude that it is trivial. Narrow systems run factories, read postal addresses, screen loans, recommend what you watch next and, increasingly, drive. Narrowness is not the same as weakness. A scalpel is narrow too.

What narrowness does mean is that claims must be tied to tasks. "This system understands language" is not a claim you can test. "This system answers questions about a set of technical manuals with 82% accuracy, and invents an answer rather than saying it does not know in 6% of cases" is a claim you can test, argue with, and decide whether to deploy. The whole discipline of evaluation, which Part Three of this volume takes up, exists to turn the first kind of sentence into the second.

## A Number Without a Baseline

Here is a small piece of arithmetic that will save you from more bad claims than any other single idea in this book.

Suppose you build a filter that decides whether an email is spam. You test it on a thousand messages and it is right 900 times. Ninety per cent. Is that good?

You cannot know, because you do not know what a stupid method would score. Imagine that only 100 of those thousand messages are spam, and 900 are legitimate. A filter that never checks anything, and simply says "not spam" to every message that arrives, is right 900 times out of a thousand. It has the same score as yours, and it contains no intelligence whatsoever. Its author could publish the same headline.

This is why every experiment in this book begins with a **baseline**: the score that a deliberately simple method achieves. The baseline is the bar that intelligence has to clear. In the spam case, the bar is already at 90%, and a filter that merely matches it has earned nothing.

Now look more closely at your filter. It catches 60 of the 100 spam messages and wrongly blocks 30 real ones. Among spam, it is right 60% of the time. Among ordinary mail, it is right 870 / 900, or 96.7%, of the time. Those numbers describe a product people might tolerate for a week before switching filters, because missing forty out of a hundred junk messages and hiding thirty real ones is a bad day at the office.

The single figure of 90% concealed all of it. That is the lesson: a score without a baseline and without a breakdown of its mistakes is not a result. It is a slogan wearing the clothes of a result.

## The Wolf That Was Really Snow

In 2016, a group of researchers at the University of Washington asked a question that more people should ask about machine learning systems: when this model says “wolf”, what is it looking at?

The model in question was a classifier trained to tell photographs of huskies from photographs of wolves, and it appeared to do so very well. The researchers analysed which parts of each image pushed the decision one way or the other. What they found was a small scandal. The model was not looking at the animal. It was looking at snow.

Almost every wolf photograph in the dataset had been taken outdoors, in winter, on snow. Most husky photographs had been taken in homes, parks or summer fields, without snow. So “there is snow on the ground” predicted “wolf” almost perfectly, and the model had learned the shortcut rather than the animal.

On the data it was given, the model was accurate. On a wolf photographed in a desert, or a husky standing in snow, it would have failed, and nobody would have known until it did.

Notice how neatly this fits the definition at the start of the chapter. The system did not choose actions to reach a goal in new situations. It found one correlation that held in one collection of pictures and would have broken the moment the situation changed. That is the difference between a system that scores well and a system that is intelligent in any sense worth the word, and the difference is invisible in a single accuracy number.

The practical habit is easy to state and hard to keep: whenever a model does surprisingly well, ask what it could be using that you did not intend. Then build a test in which that shortcut is unavailable. If the score collapses, you have found the shortcut, and you have learned more than a hundred extra training examples would have taught you.

## What the Definition Costs

Treating intelligence as behaviour has a cost, and it is only fair to name it.

A system can behave intelligently, in the sense used here, without any inner life at all, and a system can have inner states that its behaviour does not reveal. Philosophers have made careers of this gap. John Searle's Chinese room argument, published in 1980, asks you to imagine a person in a room who follows rules for manipulating Chinese characters, producing replies that look fluent to anyone outside, without understanding a word of Chinese. If the room passes the test, has it understood? Searle said no. Others said the room as a whole understands. The argument is not settled, and this book does not settle it.

What the book does is take a practical position. For the purposes of building, testing and regulating machines, behaviour is what we can observe, measure and be responsible for. If a system's outputs can harm someone, the harm is real whether or not anything is happening inside. That is why the definition in this chapter is behavioural: not because the philosophical question is unimportant, but because it is not the question an engineer can answer at the bench.

You will meet this tension again in the volumes on ethics, where the question is not whether a machine understands, but whether the people who built and deployed it can give an account of what it did.

## Problems

1. Write down five systems described as “AI” that you used this week. For each, fill in three columns: what it senses, what it chooses, and what would count as failure. Mark each one narrow or general.

2. For the system you know best, invent a test. Write the task, the measure of success, and a baseline that uses no learning at all. Predict the baseline's score before you predict the clever system's score. If your clever system does not clearly beat the baseline, the test is too easy to be interesting.

3. Here is a table from a small experiment. A classifier was tested on 200 photographs, 40 of which showed a cracked weld. It flagged 50 photographs as cracked. Of those 50, 30 really were.

|  | Flagged | Not flagged |
|---|---|---|
| Actually cracked (40) | 30 | 10 |
| Actually sound (160) | 20 | 140 |

Compute the accuracy, then compute the two numbers that matter: of the flagged photographs, what fraction were cracked, and of the cracked welds, what fraction were found. Write two sentences explaining why a factory manager might reject this system even though it is accurate most of the time.

4. Find a news story that describes a system as intelligent. Rewrite its central claim in the form “on this task, with this measure, it scores X, compared with a baseline of Y”. If you cannot fill in the blanks, say so, and say what you would need to ask the author.
