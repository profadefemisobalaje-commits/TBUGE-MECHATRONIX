# The Chain of Small Probabilities

The autocomplete in a ticketing system had one charming defect. After an agent typed "kind", it offered "regards" with a confidence of 0.94, whatever the sentence. "Kind regards" was the commonest pair in the corpus by a wide margin, and the model was simply reporting the truth about the corpus.

The defect was not statistical. It was that the model had no way to represent "kind of urgent" or "kindly note", because it looked exactly one word back. Everything about a language model's competence, and everything about its silliness, follows from how far back it looks.

## The Assumption

A language model assigns a probability to a sequence of words. Written out honestly, that is

> P(w1, w2, ..., wn) = P(w1) × P(w2 | w1) × P(w3 | w1, w2) × ...

and the conditioning context grows without limit. The **Markov assumption** truncates it: assume the next word depends only on the previous k words. With k = 1, a **bigram** model:

> P(w1 ... wn) ≈ P(w1) × P(w2 | w1) × P(w3 | w2) × ...

This is false. It is also the foundation of a great deal of working technology, and its falseness is worth understanding precisely: the model is not claiming language is a Markov chain; it is claiming that the previous word carries most of the useful short-range information, and that the rest is too sparse to estimate.

## Bigrams by Hand

Two sentences:

> the cat sat on the mat
> the cat ate the fish

Add a boundary marker at the start and end of each, giving 14 tokens including boundaries. Count the pairs:

| Pair | Count |
|---|---|
| the cat | 2 |
| cat sat | 1 |
| cat ate | 1 |
| sat on | 1 |
| on the | 1 |
| the mat | 1 |
| ate the | 1 |
| the fish | 1 |

"The" begins four pairs in total, so conditional probabilities from "the" are:

> P(cat | the) = 2/4 = 0.50
> P(mat | the) = 1/4 = 0.25
> P(fish | the) = 1/4 = 0.25

From "cat", two pairs begin, so each continuation has probability 0.5. The whole sentence "the cat sat on the mat" then has probability

> 1.00 × 0.50 × 0.50 × 1.00 × 1.00 × 0.25 = 0.0625

Every conditional in that product came from a table of eight entries. That is the entire mechanism: a language model is a lookup table with an opinion about what has not been seen.

## Sparsity, Which Is the Real Subject

The table above is small enough to memorise. Now consider the actual numbers.

A corpus of a million tokens contains 40,000 distinct words and about 600,000 distinct bigrams. The number of possible bigrams is 40,000² = 1.6 billion. So the corpus covers about 0.04% of the possible pairs, and the rest have no count at all.

A trigram model is worse: 40,000³ = 6.4 × 10¹³ possibilities, against perhaps 10 million observed trigrams. And the count of counts is brutal — most trigrams that occur, occur once.

| Order | Context used | Distinct n-grams in a million tokens | Coverage of possibilities |
|---|---|---|---|
| 1 (unigram) | none | 40,000 | 0.1% of vocabulary seen |
| 2 (bigram) | one word | 600,000 | 0.04% |
| 3 (trigram) | two words | 8,000,000 | 0.00001% |

The practical effect: an eight-word sentence using ordinary English has a decent chance of containing at least one pair that never appeared in the corpus. Under a raw bigram model, that sentence has probability zero — not small, zero. And because probabilities are multiplied, one zero annihilates the whole product, which is why the next chapter is devoted entirely to the arithmetic of the unseen.

## One More Word, and the Data Doubles

It is tempting to conclude that a trigram model must be better than a bigram model, since it uses more context. In principle it is. In practice the extra context costs data at a rate that surprises people.

The reason is in the counts. A bigram model needs to have seen each pair often enough to estimate a probability; a trigram model needs each triple. For English text, the number of distinct trigrams in a corpus is roughly ten times the number of distinct bigrams, and most of them occur once. To estimate trigram probabilities as well as bigram probabilities were estimated, a corpus needs something like ten times the tokens — and the next order needs ten times more again.

There is a standard way to see the effect, and it is the table of counts by frequency:

| Frequency in corpus | Bigrams | Trigrams |
|---|---|---|
| 1 occurrence | 68% | 86% |
| 2 occurrences | 15% | 8% |
| 3 or more | 17% | 6% |

Two thirds of observed bigrams were seen once; six sevenths of trigrams were. A count of one is not an estimate of anything — it is an anecdote — and the smoothing methods of the next chapter exist precisely to handle this distribution of anecdotes.

The practical consequence for anyone building a system: adding context is not free, and the benefit must be measured on held-out text rather than assumed. On a small domain corpus, a well-smoothed bigram model frequently beats a trigram model, because the trigram has more context and less evidence. This is the same bias-variance trade met in Volume Three, arriving in a new costume.

There is a second, subtler cost. A longer context is more specific to the training text, so it generalises less. The trigram "the pump was" may occur in training only in the context of a particular failure description, and the model will then insist that the phrase is followed by that description. The bigram "pump was" has seen more of the world.

## Generating Text From a Table

A bigram model can be run backwards, as a generator: start with a boundary, sample the next word according to the table, repeat.

On a real corpus the output has a characteristic texture. It is locally plausible — each adjacent pair is a pair that occurs — and globally incoherent, drifting by association. The classic demonstration produces sentences that begin sensibly and end somewhere unrelated, which is exactly what a one-word memory should produce:

> the pump was replaced by the supplier reported that the seal kit

Every pair here is attested. The sentence is nonsense. This is the clearest possible illustration that local statistics are not meaning, and it is why the subject did not stop here.

## Perplexity

To compare models you need a single number, and the standard one is **perplexity**: the inverse probability of the test text, normalised per word.

> perplexity = (1 / P(test text))^(1/N)

where N is the number of words. A model that assigns higher probability to real text has lower perplexity. In words: perplexity is roughly the number of equally likely choices the model is hesitating between at each step.

Two worked values. If a model gives every word in a ten-word sentence a probability of 0.1, then

> P = 0.1^10 = 10^-10
> perplexity = (10^-10)^(-1/10) = 10

The model is, on average, choosing among ten options. If the model instead assigns 0.05 per word, perplexity is 20 — twice as uncertain.

A useful calibration: uniform choice over a 40,000-word vocabulary is a perplexity of 40,000. A decent bigram model on English news text reaches a few hundred. A good modern model reaches the low tens. The distance between those numbers is the distance between a lookup table and a system that has learned something about structure.

Perplexity has two traps. It is only comparable between models with the same vocabulary — a model with a 30,000-token vocabulary and one with a 50,000-token vocabulary are scoring different tasks. And it measures how well a model predicts text, not whether it produces useful text; a model can have excellent perplexity and be useless for the task at hand.

## Exercises

1. Using the bigram table, compute the probability of "the cat ate the fish", then of "the fish ate the cat".
2. Add the sentence "the cat sat on the fish" and recompute P(cat | the) and P(fish | the). How far did two observations move them?
3. A corpus has 25,000 distinct words. How many bigrams and trigrams exist, and what fraction of bigrams would 500,000 tokens contain?
4. A model gives probabilities 0.2, 0.1, 0.05, 0.01, 0.01. Find the perplexity.
5. Why can perplexity not be compared across two tokenisers?
6. Generate six words from the bigram table, taking the most likely continuation each time. Where does it get stuck?
