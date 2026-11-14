# Words as Vectors

A retrieval system was asked for documents about "refunds" and returned nothing useful, although the archive contained four hundred pages on the subject. Every one of them used the word "credit note".

A human archivist would have found them in a minute, because a credit note and a refund are the same transaction described by two names. The system could not, because the two names share no letters, and a keyword search is a test of shared letters.

The fix required a representation in which "refund" and "credit note" are near each other. This chapter is about how such a representation is built, what its distances mean, and where the whole idea quietly fails.

## The Distributional Idea

The assumption is old, and it was stated most compactly by J. R. Firth: you shall know a word by the company it keeps.

If two words appear in similar contexts, they are used similarly, and — for most practical purposes — they mean similar things. "Refund" appears near "request", "customer", "issued", "within fourteen days". So does "credit note". The contexts are nearly the same, so the words should be near each other in whatever space we construct.

The construction is mechanical. For each word, count which other words appear near it across a corpus; treat that vector of counts as the word's representation; then compare vectors by angle.

## A Small Co-occurrence Table

Three words and their counts against three context words, in a tiny corpus:

| Word | customer | days | issued |
|---|---|---|---|
| refund | 20 | 15 | 10 |
| credit | 18 | 14 | 12 |
| valve | 2 | 0 | 1 |

"Refund" and "credit" have similar profiles; "valve" does not. That similarity is what a vector space formalises.

## Cosine Similarity, Worked

Comparing vectors by angle rather than by distance has one great advantage: it ignores length. A word appearing fifty times more often than another will have larger counts everywhere, and angle removes that scale.

> cosine = (a · b) / (|a| × |b|)

Take a = (1, 2, 2) and b = (2, 1, 2).

> dot = 1×2 + 2×1 + 2×2 = 2 + 2 + 4 = 8
> |a| = sqrt(1 + 4 + 4) = 3
> |b| = sqrt(4 + 1 + 4) = 3
> cosine = 8 / 9 = 0.889

An angle of about 27 degrees. In practice, trained word vectors produce cosine values in a narrow band — most pairs sit between 0 and 0.4 — so a value of 0.889 is not "similarity of 89%"; it is "unusually close".

| Cosine | Typical reading |
|---|---|
| 0.85 and above | Near-synonyms or the same entity |
| 0.6 to 0.85 | Same topic or domain |
| 0.4 to 0.6 | Related, not interchangeable |
| Below 0.3 | Uninformative |

These bands are conventions, not measurements, and they shift with the model. They are useful for sanity checks, dangerous as thresholds.

## How the Vectors Are Learned

The hand-built table above is what early systems used, and it works badly: it is enormous, mostly zeros, and dominated by frequent words.

The modern method trains the vectors as a by-product of a prediction task. For each word in a corpus, take its neighbours as a target, and adjust the vector so that it predicts them better. Words that occur in similar company end up with similar vectors because they need to make the same predictions. The vectors are then a few hundred numbers per word — three hundred is conventional — and they are dense rather than sparse.

The arithmetic of analogy falls out of this. Because the training forces consistent directions onto consistent relationships, vector arithmetic approximates meaning arithmetic:

> king − man + woman ≈ queen

It works often enough to be striking and often enough to be wrong that it has generated a decade of overclaiming. The failures are usually in domains where the corpus itself is inconsistent, and they are always about the corpus, never about the geometry.

One practical number: an embedding table for 100,000 words at 300 dimensions, stored as 4-byte numbers, is 120 megabytes. That is why embedding tables are shipped as files, versioned, and why a mismatch between the table used in training and the one used at inference produces predictions that are wrong in a way no error message will reveal.

## Search at Scale

Once everything is a vector, finding similar things is a geometric question: which points are nearest to this one? The naive answer is to compare against all of them, and the arithmetic of that is worth doing because it decides the architecture.

Take 100,000 documents represented as 300-dimensional vectors of 4-byte numbers.

> storage = 100,000 × 300 × 4 bytes = 120 megabytes
> cost per query = 100,000 × 300 = 30 million multiply-additions

Thirty million operations is nothing for a modern processor — a few milliseconds — so a single query against a hundred thousand documents is fine by brute force. At a hundred queries per second it is three billion operations per second, which is no longer nothing, and at a million documents it is ten times worse again.

The standard remedy is an approximate index. Instead of comparing with everything, the index groups vectors into clusters and searches only the nearby ones, or arranges them in a graph that can be walked towards the query. The result is a search that examines a small fraction of the collection and returns almost the same answer.

"Almost" is the part that requires measurement. An approximate index has a **recall**: the fraction of the true nearest neighbours it actually returns. A well-tuned index returns ninety-five per cent of the true top ten, at perhaps a fiftieth of the cost of exhaustive search.

| Index setting | Recall at 10 | Relative speed |
|---|---|---|
| Exhaustive | 100% | 1× |
| High accuracy | 98% | 8× |
| Balanced | 95% | 40× |
| Fast | 80% | 200× |

The last row is a trap that appears in real systems: retrieval gets faster, the answers get slightly worse, and because nothing in the pipeline reports recall, the degradation is invisible until someone notices that the assistant no longer mentions the obvious document.

The measurement that prevents this is small. Take two hundred real queries, compute the exhaustive answer for each, and compare with what the index returns. That is the index's recall, and it belongs in the monitoring dashboard alongside latency.

## What the Distances Do Not Mean

Four cautions, each of which has cost a project.

**Antonyms are close.** "Good" and "bad" appear in nearly identical contexts, and their vectors reflect that. A similarity search for "good" will return "bad" cheerfully.

**Similarity is not substitutability.** "Refund" and "credit note" are near neighbours and cannot be swapped in a sentence. Retrieval benefits; generation suffers.

**Rare words get bad vectors.** A word seen eleven times has eleven contexts, and its vector is noise with a direction. This is the same tail problem as the previous chapter, wearing different clothes.

**A word is not one thing.** Before contextual models, "bank" had a single vector, an average of its financial and riverside uses. Averaging two meanings produces a point between them, which is near neither.

The last point is why modern systems compute a *contextual* representation: the vector for a word depends on the sentence it is in. The word "bank" gets one vector in "raised its rate" and another in "steep and muddy". Mechanically this is the same idea — position in a space determined by company — applied per occurrence rather than per word.

## Where This Is Useful

Three applications, in order of how well they work.

**Retrieval and clustering** are the natural home. Finding documents that discuss the same subject, grouping complaints into themes, deduplicating a corpus — all of these tolerate approximate similarity and benefit enormously from synonym matching.

**Classification features** work well when data is plentiful and classes are coarse. A classifier fed averaged word vectors on ten thousand labelled emails will beat a keyword list comfortably.

**Generation and rewriting** are where the caution belongs. Nearest neighbours are not paraphrases, and a system that replaces words with their nearest neighbours produces text that is grammatically fine and semantically wrong — the failure mode that makes machine translation output read as though it were written by someone who had learned the language from a dictionary.

## Things to Try

Take two hundred sentences from a domain you know, and build the cheapest possible co-occurrence table: for each word, count the words appearing within two positions, keeping only the two hundred most frequent. Compute cosine similarity for a handful of pairs you have opinions about — "leak" and "drip", "refund" and "return", "urgent" and "important". The numbers will be less impressive than the ones in the papers and more informative, because you will know which of them are wrong.

Then find the nearest neighbours of a word that has two meanings in your domain, and see which meaning dominates. That single experiment explains why contextual models exist.
