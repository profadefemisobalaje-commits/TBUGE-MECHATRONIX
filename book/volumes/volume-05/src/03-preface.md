# Preface

Language is the easiest domain in artificial intelligence to demonstrate and the hardest to evaluate. A system that produces three fluent paragraphs looks finished; a system that classifies ten thousand support tickets looks dull. The fluent one may be wrong in ways nobody can measure, and the dull one may be right in ways that pay for themselves in a month.

This volume is written from the dull end. It spends its first hundred pages counting words, because the counting is where the difficulty hides: how text is cut into pieces, how often words repeat, how much of a language is a small number of very common tokens and an enormous tail of rare ones. It builds a language model small enough to compute with a pencil, so that the idea of a probability over sentences stops being abstract. Only then does it turn to vectors, networks, translation and speech.

The later chapters are about the part of the subject that is currently changing fastest and therefore dates fastest. The methods will be superseded. What will not be superseded is the discipline of asking what a score measures, on which text, split how, and compared with what baseline. That discipline is the actual content of the volume, and it is why the chapters on evaluation come before the chapter that tells you whether to ship.

## What you need

A text file, a terminal, and arithmetic. No calculus, no linear algebra beyond a dot product, no framework. Where a model appears — a bigram table, a classifier, a network — it is described in the smallest version that still shows the mechanism, and the numbers are small enough to check by hand.

## What you will not find

Benchmarks quoted without their conditions. A single "accuracy" for a whole language. Claims about what a model understands. These are not omissions of modesty; they are the specific things this field gets wrong most often, and a book that repeated them would be teaching the mistakes.

## A note on the examples

The text used in the worked examples is invented, short, and deliberately unremarkable. That is the point: a corpus of eight sentences is enough to show that an unseen bigram has probability zero, and a reader can verify every number on the page. Real corpora make the arithmetic expensive and the lesson no clearer.

## The promise

By the last chapter you should be able to take a piece of text, a task, and a claim about performance, and answer three questions without hesitation: what exactly was counted, what was held out, and what would happen on the text that arrives next month.
