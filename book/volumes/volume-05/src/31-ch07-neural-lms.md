# Context Windows and Learned Predictions

The summariser produced its first hundred outputs and the reviewer noticed a pattern: eight of them opened with the same sentence, and it was the first sentence of the document. The system had learned, from its training data, that summaries usually begin at the beginning. It was not summarising. It was copying the opening line and continuing in a plausible style.

This chapter is about the machinery behind such systems, described as plainly as the machinery allows: how a model uses a window of surrounding text, why that window has a size, and what the size costs.

## From Lookup Table to Representation

The bigram model of Chapter Five looked up a count. A learned model instead computes a vector for the whole context, and then computes a probability over the vocabulary from that vector.

The difference in behaviour is exactly what the counting theory predicts. A lookup table fails on an unseen context because there is no entry. A representation does not have entries; it has a function, and the function produces a sensible answer for contexts it has never met, because similar contexts map to nearby vectors.

So "the clamp for the new bracket" can be handled even if never seen, provided the model has learned what "clamp" and "bracket" do in sentences. That is generalisation, and it is bought with computation rather than with counts.

## Attention, in One Paragraph

The mechanism that made this practical in long contexts is attention, and the idea is smaller than the name.

For each position in the text, the model decides which earlier positions matter for predicting what comes next, and it does so by comparing a vector for the current position with a vector for each earlier one. The comparisons are turned into weights that sum to one, and the model reads a weighted mixture of the earlier positions.

A worked set of weights for one position, over four earlier tokens:

> token 1: 0.05   token 2: 0.15   token 3: 0.50   token 4: 0.30

The sum is 1.00, and the model's "view" of the past at this position is 50% token 3, 30% token 4, and almost nothing else. In a real model there are many such attention heads and many layers, so the picture is a stack of these mixtures, but the arithmetic of any single one is that sum.

Two consequences follow. The window can be long, because attention does not require the context to be represented by a fixed-size state. And the cost grows with the square of the window length, because every position compares with every earlier position — which is why context length is expensive and why "just use a bigger window" is a budget decision, not a technical one.

## What Fits in a Window

Context windows are quoted in tokens. Converting to something human:

| Window | Ordinary English words | What it holds |
|---|---|---|
| 2,000 tokens | about 1,500 | Two long emails |
| 8,000 tokens | about 6,000 | A short report |
| 32,000 tokens | about 24,000 | A chapter of a book |
| 128,000 tokens | about 98,000 | A small manual |

The conversion is approximate, and it differs by language and by tokeniser, which is the point made in Chapter Two: a window is a token budget, and the same window holds fewer words in German than in English.

The practical issue with windows is not what fits but what gets *used*. Information at the far end of a long window is often attended to weakly, and a system that puts the crucial instruction at the start of a very long prompt is hoping rather than designing. Put the instruction where it will be read: near the end, or repeated.

## Temperature, and Why Outputs Vary

A model produces a probability for every token in its vocabulary. To generate text you sample from that distribution, and how you sample changes the character of the output.

**Temperature** divides the log-probabilities before the distribution is renormalised. Below one, the distribution sharpens; above one, it flattens.

Take a distribution over three candidate tokens: 0.6, 0.3, 0.1.

| Temperature | Resulting distribution |
|---|---|
| 0.5 | 0.78, 0.20, 0.02 |
| 1.0 | 0.60, 0.30, 0.10 |
| 1.5 | 0.52, 0.33, 0.16 |

At temperature 0.5 the model almost always takes the most likely token: consistent, repetitive, and occasionally stuck. At 1.5 it takes the third option one time in six: varied, and more prone to drifting off the point. There is no correct setting, only a setting appropriate to the task — extraction wants low, brainstorming wants higher.

Greedy decoding, which always takes the most likely token, is the limit of temperature zero, and it produces text that loops: the same clause, then the same clause again, because the model's own output has become its context.

## What Such Models Are and Are Not

They are next-token predictors trained on a very large amount of text. Everything they do follows from that: fluency, because fluent text is what predicts well; factual errors in the shape of confident prose, because a plausible continuation is not a verified one; and a tendency to agree with the premise of a question, because agreement is the common continuation.

The word for the third failure is sycophancy, and the word for the second is hallucination. Neither is a bug in the usual sense. A model that generates a citation for a paper that does not exist is doing precisely what it was trained to do — producing the token sequence that looks most like a citation — and the repair is external: retrieve the source, check it, and refuse when it is absent.

That is why this volume puts retrieval and evaluation after this chapter rather than before. A generative model without a retrieval step and an evaluation step is a demonstration. With them, it is a system.

## Cost, Which Is Real

Three quantities determine whether a language model can run in a given application.

**Tokens in and out.** A 2,000-word prompt is about 2,600 tokens; a 300-word answer about 400. Multiply by requests per day, and the bill follows.

**Latency.** Generation is sequential: each token requires a full pass through the model. At twenty tokens per second, a 400-token answer takes twenty seconds, and no amount of parallel hardware changes the sequence — it only makes each step faster. Streaming the output hides the delay without reducing it.

**Memory for context.** The intermediate state for each token in the window must be kept while generating, so a longer window costs memory as well as time. This is why long conversations degrade or become expensive, and why summarising the conversation periodically is a standard engineering move.

| Use | Constraint | Consequence |
|---|---|---|
| Chat assistant | Latency, 1–3 s to first token | Stream, keep answers short |
| Batch classification | Throughput | Batch requests, avoid generation |
| Document question answering | Window, retrieval | Chunk, retrieve, cite |
| Real-time control | Latency under 100 ms | Do not use a generative model |

## Exercises

1. A prompt contains 1,800 words. Estimate the token count, and say whether it fits a 2,000-token window.
2. A distribution is 0.5, 0.3, 0.15, 0.05. Compute the temperature-0.7 version approximately, and describe the change in behaviour.
3. Explain, in three sentences, why a model can produce a fluent and entirely false paragraph.
4. A system must answer 5,000 questions a day with a 400-token answer each. At twenty tokens per second, how much generation time is that in total, and does it need more than one machine?
5. Why does attention cost grow with the square of the window, and what practical consequence does that have for a 100,000-token prompt?
6. Design a prompt layout for a question-answering system where the instruction, the retrieved documents and the question must all be present. Where does each go, and why?
