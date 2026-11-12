# Smoothing, and the Cost of the Unseen

A support chatbot was built on a trigram model over four years of transcripts. It answered routine questions well. Then a new product line launched, and the very first message about it — "where is the clamp for the new bracket" — produced no reply at all, because the trigram "the clamp for" had never occurred in the old transcripts and its probability was zero.

The system did not say "I don't know". A model that multiplies probabilities has no way to say anything once a factor is zero. The reply was empty, and the operator assumed the bot was broken, which in a sense it was.

Every language model that has ever been built is, at bottom, a scheme for assigning a small but nonzero probability to text it has never seen. This chapter is that scheme.

## The Zero Problem

A bigram model estimates

> P(word | previous) = count(previous, word) / count(previous)

If the pair has never occurred, the numerator is zero. The denominator may be large — "the" might occur 60,000 times — and the estimate is still zero, because a single unseen continuation makes the whole probability collapse.

The problem is not the missing pair. It is that the estimate treats "never observed" as "impossible", and for language that is obviously wrong. English does not run out of sentences.

## Add-One, With Numbers

The simplest repair is to pretend every possible pair was seen one extra time.

> P(word | previous) = [count(previous, word) + 1] / [count(previous) + V]

where V is the vocabulary size. Take the corpus from the previous chapter, with V = 8 (the, cat, sat, on, mat, ate, fish, and the boundary).

Unsmoothed: P(cat | the) = 2/4 = 0.50.

Smoothed: (2 + 1) / (4 + 8) = 3/12 = 0.25.

Every unseen pair now has probability 1/12 = 0.083, which is the point — nothing is impossible any more. But note what happened to the pairs that were genuinely common: their probability fell by half. Add-one takes mass from the observed and gives it to the unobserved, and it does so without regard to how much room there is.

The consequence is easy to see in the vocabulary size. With V = 40,000 and a context seen 4 times, the smoothed estimate is (2+1)/(4+40,000) = 0.000075, against an unsmoothed 0.50. The model has been destroyed to rescue one unseen pair. This is why add-one is a teaching device and not a production method: for large vocabularies it gives away almost all the mass.

The general repair is **add-k**, with k much less than one — 0.01 or 0.001 — or better, a method that gives mass to unseen events in proportion to how many *distinct* continuations a context has, rather than uniformly.

| Method | Unseen probability | Behaviour |
|---|---|---|
| None | zero | Fails on any novel text |
| Add-one | 1/(count + V) | Simple, over-smooths badly |
| Add-k | k/(count + kV) | Tunable, still uniform |
| Good-Turing | proportional to singletons | Principled, unstable at scale |
| Kneser-Ney | from continuation counts | Best classical option |
| Interpolation | mixture of orders | Simple and effective |

## Interpolation, Which Is What People Actually Do

Instead of choosing one order, mix them.

> P(word | previous two) = lambda × P3(word | previous two) + (1 - lambda) × P2(word | previous)

Worked, with lambda = 0.7. Suppose the trigram "clamp for the" has count 3 out of 5 occurrences of "clamp for", and the bigram "for the" has count 40 out of 900 occurrences of "for".

> P3 = 3/5 = 0.60
> P2 = 40/900 = 0.044
> P = 0.7 × 0.60 + 0.3 × 0.044 = 0.42 + 0.013 = 0.433

The high-order model dominates when it has evidence, and the low-order model holds the floor. Where the trigram is unseen, the estimate falls back to the bigram, which is the behaviour the chatbot needed.

The weights can be fitted on held-out text, and doing so is a five-line exercise that outperforms any amount of intuition. The principle is worth stating: the more data a context has, the more the model should trust the specific context; the less it has, the more it should trust the general one.

## Evaluating: Held-Out Text, Not Sentences

A language model is evaluated on text it has not seen, and the split must be by document, not by sentence. Two reasons.

Sentences from the same document share vocabulary, topic and often phrasing, so a random sentence split leaks. A model that has seen the rest of a manual will predict the next page of that manual far better than it predicts a page from a different manual.

The quantity reported is usually perplexity on the held-out set, and the comparison must hold two things fixed: the tokenisation and the vocabulary. Change either and the number is meaningless.

A worked comparison, on the same 10,000-word held-out text:

| Model | Perplexity | Reading |
|---|---|---|
| Uniform over 20,000 words | 20,000 | No information |
| Unigram | 900 | Frequency only |
| Bigram, no smoothing | infinite | Contains a zero |
| Bigram, interpolated | 320 | Useful |
| Trigram, interpolated | 240 | Better |

Note the third row. A model that looks excellent on its training text scores infinitely badly on held-out text the moment it meets one unseen pair, and this is the single most important fact in the chapter. A model evaluated on the data it was trained on is not being evaluated at all.

## Why This Still Matters

It is tempting to treat all of this as history now that models are trained by gradient descent on enormous corpora. It is not history, for three reasons.

The mechanisms are the same. A neural language model also assigns probability to the next token given a context; it simply represents the context as a vector rather than a lookup, and therefore generalises to unseen contexts instead of failing. The reason modern models handle "the clamp for" is that they are not counting that exact trigram — they are computing from a representation that shares structure with everything similar.

The evaluation is the same. Perplexity, held-out text, splits by document: the discipline carries over unchanged.

The failure is the same. A model meeting text from a new domain degrades, and the degradation is invisible unless the held-out set is genuinely new. The chatbot in the opening was not defeated by its smoothing method. It was defeated by a corpus that stopped before the product launched.

## Working Notes

1. With V = 12 and a context seen 6 times, compute the add-one probability for a word seen twice, and for a word never seen.
2. A trigram model gives 0.4 for the observed trigram, and the interpolating bigram gives 0.05. With the weight at 0.6, what is the mixed probability? What happens at 1.0?
3. Explain why add-one smoothing is unacceptable for a 40,000-word vocabulary, with one calculation.
4. A model scores perplexity 180 on held-out news and 610 on held-out legal contracts. What does the difference tell you, and what would you do before deploying it on contracts?
5. Design a train/validation/test split for a corpus of 5,000 emails spanning three years, where the system will be deployed next year. State the rule, not the ratio.
6. Give one sentence of text that a bigram model would score as impossible and a trigram model would score as probable, and explain why the reverse can also happen.
