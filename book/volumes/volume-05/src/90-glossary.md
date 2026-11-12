# Glossary

**Accuracy** — the fraction of decisions that are correct. Uninformative when classes are unbalanced.

**Add-one smoothing** — adding one to every count so that unseen events have nonzero probability. Simple and badly biased for large vocabularies.

**Alignment** — the correspondence between words or phrases in a source text and its translation.

**Attention** — a mechanism that weights earlier positions in a context according to their relevance to the current one.

**Bag of words** — a representation that counts words and discards their order.

**Bigram** — a pair of adjacent tokens; a bigram model conditions each word on the previous one.

**BLEU** — an automatic translation score based on overlapping word sequences, with a penalty for short output.

**BM25** — a ranking formula balancing term rarity, term frequency and document length.

**Calibration** — the property that predicted probabilities match observed frequencies.

**Chunking** — splitting long documents into passages small enough to embed or retrieve.

**Collocation** — a pair of words that co-occur more often than chance, such as "strong tea".

**Context window** — the number of tokens a model can attend to at once.

**Cosine similarity** — the cosine of the angle between two vectors; a scale-free measure of similarity.

**Coverage** — the share of running text accounted for by a given vocabulary size.

**Distributional hypothesis** — the idea that words used in similar contexts have similar meanings.

**Edit distance** — the smallest number of insertions, deletions and substitutions that turn one string into another.

**Embedding** — a dense vector representation of a token, document or query.

**Entity** — a span of text referring to a name, place, date, quantity or similar.

**F1** — the harmonic mean of precision and recall.

**Hallucination** — fluent output that asserts something false, typically a plausible continuation rather than a retrieved fact.

**Heaps' law** — the sublinear growth of vocabulary size with corpus size.

**Idf** — inverse document frequency; a weight that reduces the importance of terms appearing in many documents.

**Inverted index** — a mapping from terms to the documents containing them.

**Language model** — a probability distribution over sequences of tokens.

**Leakage** — information from the test set reaching the model, inflating measured performance.

**Lemma** — the dictionary form of a word, to which its inflections are related.

**Macro-average** — averaging a metric across classes with equal weight, so rare classes count as much as common ones.

**Mean reciprocal rank** — the average of one over the rank of the first relevant result.

**Mel scale** — a frequency scale approximating human pitch perception, used in speech features.

**Micro-average** — averaging a metric weighted by the number of examples in each class.

**MRR** — see mean reciprocal rank.

**N-gram** — a sequence of n consecutive tokens.

**Naive Bayes** — a classifier that assumes features are independent given the class.

**Normalisation** — the decisions that make different strings count as the same text.

**Perplexity** — the inverse probability of held-out text, normalised per token; roughly the number of choices the model is hesitating between.

**Pointwise mutual information** — the log ratio of a pair's joint probability to the product of its individual probabilities.

**Precision** — the fraction of positive decisions that are correct.

**Prompt injection** — instructions hidden in text the system reads, intended to redirect its behaviour.

**Recall** — the fraction of real positives that are found.

**Retrieval** — selecting documents or passages relevant to a query.

**Sampling (decoding)** — choosing the next token from a distribution, controlled by temperature and related settings.

**Sentence segmentation** — dividing text into sentences, complicated by abbreviations and decimals.

**Smoothing** — redistributing probability mass so that unseen events are not impossible.

**Stemming** — reducing words to a crude common root by removing affixes.

**Stop word** — a very frequent word, often removed before modelling and often carrying negation.

**Subword tokenisation** — splitting text into frequent pieces rather than whole words, so that any string can be encoded.

**Temperature** — a divisor applied to log-probabilities before sampling; low values sharpen, high values flatten.

**tf-idf** — term frequency weighted by inverse document frequency.

**Token** — the unit a model consumes: a word, subword or character.

**Type** — a distinct word form, as opposed to a token instance.

**Word error rate** — the fraction of reference words that are substituted, deleted or inserted by a recogniser.

**Zipf's law** — the inverse relation between a word's frequency and its rank.
