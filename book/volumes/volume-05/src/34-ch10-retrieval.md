# Search, Retrieval and Answering Questions

An engineer asked the internal assistant how to reset a specific controller. It replied, confidently and at length, with the controller's address, its baud rate and three steps that were almost right.

The retrieval step had returned the manual's table of contents — a page dense with the right words and containing none of the procedure — and the generative step had done what generative steps do: it had produced plausible prose from an outline. The failure was in retrieval, and it looked like a failure of the model.

This chapter is about the half of a question-answering system that decides what the model is allowed to read.

## The Inverted Index

The classical search stack is an inverted index: for each term, a list of documents containing it, with positions. Building one from a corpus of documents is a counting exercise, and the counting is the same counting as Chapter Three.

Retrieval scores documents against a query, and the dominant classical formula is **BM25**, which balances three effects: a term's rarity, its frequency in the document, and the document's length.

> score = idf × [ tf × (k1 + 1) ] / [ tf + k1 × (1 − b + b × doclen / avgdoclen) ]

with idf = ln((N − df + 0.5) / (df + 0.5) + 1), k1 around 1.2 and b around 0.75.

Worked, in a collection of 1,000 documents with an average length of 120 words. The query term appears in 10 documents, so

> idf = ln(990.5 / 10.5 + 1) = ln(95.3) = 4.56

Three candidate documents:

| Document | Term count | Length | Score |
|---|---|---|---|
| A | 3 | 100 | 7.43 |
| B | 1 | 100 | 4.89 |
| C | 3 | 300 | 5.42 |

Document A beats C although both contain the term three times, because C is three times longer and is therefore less about anything in particular. Document B beats nothing and is ranked last. This is the behaviour a person expects from search, derived from counts.

The length normalisation is the part people find surprising, and it is the part that matters most on real corpora: a long document containing a word once is making a passing reference, and a short document containing it once may be about nothing else.

## Measuring Search

Retrieval is measured with the queries you will actually receive, and the measures are simple.

**Precision at k** — of the top k results, how many are relevant. Three relevant in the top five is 0.6.

**Recall at k** — of all relevant documents, how many appear in the top k. With four relevant in the collection, three in the top five is 0.75.

**Mean reciprocal rank** — the average of 1/rank of the first relevant result. Three queries answered at ranks 3, 1 and 8:

> (1/3 + 1/1 + 1/8) / 3 = (0.333 + 1.000 + 0.125) / 3 = 0.486

MRR is the right summary when a user needs one good result, as in an assistant. Precision at k is right when a user will read several, as in research.

The hard part is the query set. A hundred real queries, sampled from logs and labelled for relevance by someone who knows the domain, is worth more than any amount of tuning against invented queries — and the labels are the expensive part.

## Semantic Retrieval, and Why It Is Not a Replacement

Embedding retrieval replaces term matching with vector similarity: embed the query and the documents, and return the nearest documents.

It finds the credit note when you ask for a refund, which keyword search cannot. It also fails in ways that keyword search does not:

It cannot match a part number. "XYZ-40" and "XYZ-41" are nearly identical vectors and completely different components.

It has no notion of exact phrase, so a query for a quoted error message may return anything semantically nearby.

It is opaque. When it returns the wrong document, there is no term to inspect and no score to explain.

The practical answer is **hybrid** retrieval: run both, and combine the rankings. A simple and effective recipe is to take the top fifty from each, merge the lists, and rerank the union with a small model or a hand-weighted score that gives a bonus to exact term matches. The bonus exists because rare exact terms are almost always the user's actual intent, and dense vectors under-weight exactly that.

## A Second Pass: Reranking

Retrieval has two jobs that are hard to do at once: find candidates cheaply, then judge them carefully. Systems usually split the work.

The first stage scores the whole collection with something fast — BM25, or a vector index — and keeps the top fifty. The second stage reads each candidate together with the query and produces a relevance score. That second model sees the pair jointly, so it can notice that the query asks about "reset procedure" and the candidate discusses "resetting", which a bag of words cannot.

The cost is straightforward arithmetic. Fifty candidates of 300 tokens each is 15,000 tokens per query, evaluated by a model that reads query and candidate together — perhaps fifty times the work of scoring the same fifty documents separately. At ten queries a second, that is a substantial machine; at one query a second, it is nothing.

The trade is worth stating plainly, because it decides whether a second stage is affordable at all. If the application tolerates two hundred milliseconds per query, a reranker costing a hundred and fifty of those milliseconds is reasonable. If the interface must respond within fifty milliseconds, it is not, and the improvement in ordering has to come from a better first stage instead.

| Stage | Job | Cost | Failure if skipped |
|---|---|---|---|
| Filter | Remove obviously irrelevant | Low | Wasted work downstream |
| Retrieve | Get 50 candidates | Low | Recall cannot be recovered |
| Rerank | Order them well | Medium | Good documents ranked 20th |
| Read | Generate an answer | High | Wrong answer from right documents |

The table explains a common misdiagnosis. When an assistant gives a poor answer, the instinct is to improve the generator. But the generator can only work with what it is shown, and if the right passage is at rank 30, no amount of model quality will recover it. Check the retrieval first: does the correct passage appear in the top k at all? If it does not, the answer is in the index, the chunks or the query, and never in the language model.

A useful diagnostic, and it takes an afternoon: take a hundred real questions, record the rank of the first genuinely relevant passage, and plot the distribution. If half the questions have their answer in the top three, the retrieval is sound and the problem is downstream. If the median rank is fifteen, the system is being asked to answer from the wrong half of the manual.

## Chunking, Which Decides Everything

A long document cannot be embedded as a whole, so it is split into chunks. The arithmetic is trivial and the consequences are not.

A 60,000-word manual, chunked at 300 words with 50 words of overlap:

> chunk count = (60,000 − 50) / (300 − 50) = 240

Each chunk is retrieved independently, so a system that returns five chunks is showing the model 1,500 words out of 60,000 — two and a half per cent of the manual. If the answer spans a chunk boundary, or if the relevant chunk ranks sixth, the model never sees it.

| Chunking choice | Effect |
|---|---|
| Too small | Loses context; answers refer to missing steps |
| Too large | Retrieval becomes coarse; many irrelevant words |
| No overlap | Answers cut mid-sentence at boundaries |
| Overlap 10–20% | Standard compromise |
| Split by section | Best, when the document has structure |

The last row is the one that pays. Documents written by human beings have headings, and a chunk that follows a heading boundary contains a coherent thought. Chunking by fixed length throws that structure away and then spends effort recovering it.

## What Actually Fails

A question-answering system built on retrieval fails in five characteristic ways, and diagnosing which one is happening is most of the engineering.

| Failure | Symptom | Fix |
|---|---|---|
| Retrieval miss | Answer ignores the obvious document | Better chunks, hybrid search, more k |
| Stale index | Answer cites a superseded version | Rebuild on change, show dates |
| Chunk boundary | Answer stops mid-procedure | Overlap, section-aware splitting |
| Conflicting sources | Answer averages two policies | Rank by authority, show both |
| No answer exists | Confident invention | Refuse when retrieval is weak |

The fourth row is the one nobody anticipates: a corpus containing two versions of a policy, retrieved together, produces an answer that is a blend of both. The repair is not a better model but a better corpus — a versioned index with the obsolete document removed, and the removal treated as part of the deployment.

The fifth row is a design decision that must be made explicitly. A system that answers only when retrieval produces a strong match, and otherwise says it does not know, will be trusted. A system that always answers will eventually answer wrongly about something important, and the trust will not return.

## Things to Try

Build the smallest possible search engine: ten text files, an inverted index of words to file names, and a scorer that counts matching words and divides by document length. Then run ten queries you care about and record where the right document appears.

The exercise takes an hour and teaches three things permanently: that length normalisation matters, that the words you thought were distinctive ("the", "system") are not, and that the query you wrote is rarely the query the index needs.

## Problems

1. Compute the idf for a term appearing in 3 documents of a 500-document collection. Is it more or less informative than a term in 30 documents?
2. A document of 200 words contains a term 4 times, in a collection with an average length of 100 and idf 3.0. Compute its BM25 score with k1 = 1.2 and b = 0.75.
3. Three queries are answered at ranks 1, 4 and 10. Compute MRR.
4. A manual of 120,000 words is chunked at 200 words with 40 overlap. How many chunks? How many words does a system returning k = 8 show the model?
5. Explain why an embedding search fails on part numbers, and describe a fix that does not abandon embeddings.
6. A corpus contains a policy from 2023 and its replacement from 2025. Describe three mechanisms that prevent the old one influencing answers.
