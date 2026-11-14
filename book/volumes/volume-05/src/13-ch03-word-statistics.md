# The Statistics of Words

The classifier worked on everything except the one thing it was built for. It routed emails to six departments with an accuracy of 91%, and it failed, consistently, on messages about a single component: the model XYZ-40 seal kit.

The reason was visible in a frequency table. Across two years of email, "seal" appeared 4,100 times, "kit" 2,900, "leak" 1,700 — and "XYZ-40" appeared eleven times. Eleven examples cannot teach a model anything, and the model had done the only sensible thing available to it: it had learned that the rare token was noise and ignored it.

This chapter is about the shape of that distribution. It is the same shape in every language, in every corpus, and it explains a large fraction of the failures in applied language processing.

## A Frequency Table Worth Memorising

Take a corpus of one million tokens of ordinary English and rank the words by frequency. The counts fall roughly as the reciprocal of the rank:

| Rank | Approximate count | Share of tokens |
|---|---|---|
| 1 | 60,000 | 6% |
| 2 | 30,000 | 3% |
| 5 | 12,000 | 1.2% |
| 10 | 6,000 | 0.6% |
| 100 | 600 | 0.06% |
| 1,000 | 60 | 0.006% |

This is **Zipf's law**, and it says that a word's frequency is inversely proportional to its rank. It is not an exact law — the very top is flatter than the formula predicts, and the far tail is steeper — but it is close enough to be used for planning.

Two consequences, both of which decide projects.

The first is coverage. A small number of words accounts for most of the running text:

| Vocabulary size | Share of tokens covered |
|---|---|
| Top 10 words | about 25% |
| Top 100 words | about 50% |
| Top 1,000 words | about 70% |
| Top 10,000 words | about 90% |

So a system that handles the ten thousand most common words is missing one token in ten, and the missing tenth contains almost all the information. "The pump was replaced" is mostly common words; "pump" is not in the first hundred, and the thing that distinguishes a failure report from a delivery query is nearly always in the tail.

The second consequence is about vocabulary growth. As a corpus grows, the number of distinct types grows too, but sublinearly. The empirical relation is **Heaps' law**:

> types = k × tokens^0.5 (approximately, with the exponent usually between 0.4 and 0.6)

Doubling the corpus multiplies the vocabulary by about 1.4. Which means: no corpus is ever complete, and there is always a next word you have never seen. Every model in the rest of this book has to have an answer for that word, and the answers are not equivalent.

## What Frequency Does Not Tell You

Frequency is not importance. "The" is the most frequent token in English and conveys almost nothing; a part number occurring eleven times may be the entire point.

Frequency also does not identify phrases. "New York" is a unit of meaning, and so is "strong tea", and neither is discoverable from the counts of the individual words. What identifies them is that the words co-occur far more often than chance would predict.

That comparison has a standard measure, the **pointwise mutual information**:

> PMI(a, b) = log2 [ P(a, b) / (P(a) × P(b)) ]

Worked, on the million-token corpus. Suppose "strong" occurs 2,000 times, "tea" 1,000 times, and the pair "strong tea" occurs 30 times as an adjacent pair.

> P(strong, tea) = 30 / 1,000,000 = 0.00003
> P(strong) × P(tea) = 0.002 × 0.001 = 0.000002
> ratio = 15
> PMI = log2 15 ≈ 3.9

A PMI near zero means the words appear together as often as independent chance predicts — which is what happens with "the" and almost anything, because "the" is everywhere. A high PMI means genuine association, and the list of high-PMI pairs in any corpus is a surprisingly good dictionary of the domain's terminology.

The measure has a known pathology: it over-rewards rare pairs. A pair of words that occur together twice and never apart gets an enormous PMI. Practical implementations therefore require a minimum count, and often use a variant that discounts rare events.

| Pair | Count | PMI | Reading |
|---|---|---|---|
| strong tea | 30 | 3.9 | Real collocation |
| of the | 21,000 | near 0 | Grammar, not meaning |
| XYZ-40 seal | 9 | high | Domain term, few examples |
| good bad | 40 | low | Antonyms, rarely adjacent |

## The Rare Class Is the Task

Put the two facts together — coverage concentrated in common words, and the informative words in the tail — and the practical difficulty of applied language processing is stated: **the thing you must detect is almost always rare**.

A defect description, a fraud signal, a rare diagnosis, an unusual product complaint: all of them live in the tail, where counts are small and models are uncertain. This is why the previous volume spent so long on class imbalance, and why the numbers look the same here.

The responses are also the same, and they are worth listing because they are the ones that work.

Get more examples of the rare thing. Nothing else substitutes.

Represent words as pieces rather than atoms, so that a rare word shares fragments with common ones.

Use context, not the word alone. "XYZ-40" is rare, but "leak", "seal" and "replaced" are not, and a model that reads windows rather than words can use them.

Choose metrics that do not reward ignoring the rare class, which is to say anything except accuracy.

## A Counting Exercise, Done Fully

Four short documents, and a question: which word is most characteristic of this little collection?

> d1: pump seal leak
> d2: pump seal replaced
> d3: pump noisy
> d4: valve leak

Tokens: 11. Types: pump, seal, leak, replaced, noisy, valve. Counts: pump 3, seal 2, leak 2, replaced 1, noisy 1, valve 1.

Frequency says "pump". But "pump" appears in three of four documents, and "leak" in two — so a document-level measure would rank pump first and leak second.

Now compute a document-frequency-weighted score: multiply the count of a word in a document by the inverse of how many documents contain that word. "leak" has document frequency 2, so its weight is higher than "pump"'s document frequency of 3. This is the intuition behind tf-idf, and it is the reason a search engine does not simply return documents containing the most common term.

The arithmetic for "leak" in d1: term frequency 1, inverse document frequency log(4/2) = 0.69, score 0.69. For "pump" in d1: term frequency 1, log(4/3) = 0.29, score 0.29. The rarer word wins, which is the correct answer for retrieval, and it is a purely statistical result — no understanding of pumps or leaks was required.

## Problems

1. In a two-million-token corpus, rank 1 occurs 110,000 times. Using Zipf's law, estimate the count at ranks 2, 10 and 500.
2. A corpus of 200,000 tokens has 18,000 types. If it is doubled, estimate the number of types using Heaps' law with an exponent of 0.5.
3. Compute PMI for a pair occurring 50 times, where each word occurs 5,000 times, in a corpus of 2,000,000 tokens. Is it a collocation?
4. Explain, with the coverage table, why a keyword list of 200 words can classify some support tickets well and fail on others.
5. A domain has 900,000 tokens and a product name that appears 14 times. Propose three ways to make a classifier sensitive to it.
6. Two corpora, one of news and one of legal contracts, have the same number of tokens. Which has more types, and why? What does that imply for a shared vocabulary?
