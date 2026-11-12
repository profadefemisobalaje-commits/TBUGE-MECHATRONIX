# Cleaning, Splitting and Counting

A sentiment model was trained on twenty thousand customer emails and performed beautifully in testing. In production it developed a curious habit: any message ending with a formal sign-off was scored as negative, however cheerful the body.

The cause took an afternoon to find. The most predictive phrase in the entire training set was not a phrase about the product at all. It was the boilerplate signature that the company's own complaint-handling team appended to every message it sent, and the training data had been assembled from threads in which those appended messages were included. The model had learned, with perfect statistical justification, that this signature predicted dissatisfaction — because in that dataset, it did.

This chapter is about the decisions that come before any model: what to keep, what to cut, and what a token is. They are unglamorous and they determine more of the outcome than the choice of algorithm.

## Cleaning Is a Claim About Meaning

Every cleaning step asserts that two different strings mean the same thing. That assertion is sometimes true, and the cases where it is false are where the bugs live.

**Lowercasing** asserts that case is irrelevant. True for topic modelling, false for names ("Apple" the company, "apple" the fruit), for German nouns, and for any text where shouting is a signal.

**Removing punctuation** asserts that it carries no information. False for "3.5", for "U.S.", for "don't", and for emoticons.

**Removing stop words** asserts that frequent words are empty. False for negation, for questions ("what", "why"), and for anything where the distinction between "the report" and "a report" matters.

**Stemming** asserts that "running", "runs" and "ran" are one thing. True for retrieval, false for grammar-sensitive tasks, and always approximate — the classic stemmer output "gener" for "general", "generous" and "generation".

**Removing HTML and boilerplate** asserts that markup is not content. Almost always true, and almost always done incompletely, which is how the opening story happened.

| Decision | Helps | Hurts |
|---|---|---|
| Lowercase | Vocabulary size, recall | Names, emphasis, German |
| Strip punctuation | Simplicity | Decimals, abbreviations, contractions |
| Remove stop words | Speed, topic clarity | Negation, questions, style |
| Stem or lemmatise | Grouping variants | Precision, rare terms |
| Strip digits | Noise reduction | Quantities, dates, codes |

The general principle: clean for a task, not for a corpus. If you cannot say which errors the cleaning prevents and which it introduces, it is a habit rather than a decision.

## Where Whitespace Fails

Splitting on spaces gets you a long way in English and then stops.

> "I don't think it's working" becomes: I | don't | think | it's | working

That is five tokens, and "don't" carries a negation that is invisible to a model that only sees the string. Splitting contractions gives "do" and "n't", which makes the negation explicit. Whether that is better depends on the task, and either choice must be applied consistently.

Other cases where spaces are the wrong boundary:

Hyphenated compounds ("state-of-the-art") — one token or five?

Numbers with units ("12mm", "12 mm", "12.0 mm") — three forms of one fact.

URLs and file paths — full of punctuation that a naive splitter shreds.

Languages without spaces — Chinese and Japanese require segmentation of their own, and a whitespace splitter returns one enormous token per sentence.

Social media text — hashtags, mentions, repeated letters for emphasis.

## Subwords, and the Vocabulary Problem

The tension is simple. A word-level vocabulary must include every word the system will ever meet, and English has an unbounded supply: product names, surnames, compounds, typos, and the plurals and tenses of all of them. A vocabulary of a million words still misses something every day. An unknown word must be mapped to a single placeholder, and that placeholder means nothing.

The modern answer is to stop treating words as atoms and learn **subword** units: pieces of words that recur often enough to be worth having.

The standard algorithm is byte-pair encoding, which is a counting procedure and can be run by hand on a toy corpus.

Start with these words and their frequencies: low (5), lower (2), newest (6), widest (3). Split each into characters, then count adjacent pairs across the whole corpus.

| Pair | Count |
|---|---|
| e s | 9 |
| s t | 9 |
| w e | 8 |
| e w | 6 |
| n e | 6 |

The most frequent pair is "es" (the tie with "st" is broken arbitrarily). Merge it everywhere it occurs: "newest" becomes n e w es t, "widest" becomes w i d es t, and the pair counts are recomputed. Repeat. After a few dozen merges on a real corpus, common word-pieces have appeared: "ing", "tion", "pre", "est".

The result is a vocabulary of thirty thousand to fifty thousand pieces that can encode any string whatsoever, because the fallback is characters. Unknown words disappear as a category; an unfamiliar product name becomes two or three familiar fragments.

The cost is that token counts inflate. English text averages roughly one and a third tokens per word, so a thousand-word document becomes about 1,300 tokens. Since nearly every modern language system bills, or times, or limits by token, that inflation is not academic:

| Document | Words | Tokens (approx.) | Effect |
|---|---|---|---|
| Email | 250 | 330 | Fits easily |
| Report | 4,000 | 5,300 | Approaches context limits |
| Manual | 60,000 | 80,000 | Must be chunked |

There is a second cost that is easier to miss. Tokenisation depends on the tokeniser's training corpus, so two systems with different tokenisers cannot compare token counts, and a per-token price is not a per-word price.

## Tokens and Types

Two counts, and confusing them is a classic error.

The **token count** is the number of running instances: "the cat sat on the mat" has six tokens.

The **type count** is the number of distinct forms: "the", "cat", "sat", "on", "mat" — five types, because "the" appears twice.

A useful corpus statistic: a million tokens of English news text contains roughly forty thousand types, and about half of those types occur exactly once. That long tail of singletons is the central difficulty of the subject, and the next chapter is about what it does to any model built on counting.

## Numbers, Dates and Units

Nothing in ordinary tokenisation handles quantities well, and quantities are where text processing meets consequences.

"1,200" tokenises as "1", ",", "200". "12.5 mm" becomes "12", ".", "5", "mm". "£1.2m" becomes a currency symbol, a decimal and a letter. None of these is wrong at the level of tokens, and all of them are wrong at the level of meaning: the value is distributed across pieces, and any downstream task that reads single tokens has lost it.

The repair is a normalisation step that recognises quantities as units and rewrites them in a canonical form before tokenisation:

| Input | Canonical | Note |
|---|---|---|
| 1,200 | 1200 | Thousands separator removed |
| 1.200,50 | 1200.50 | European convention |
| £1.2m | 1200000 GBP | Multiplier expanded |
| 12.5mm | 12.5 mm | Space inserted for splitting |
| 3 May 2025 | 2025-05-03 | Ambiguity removed |

Two warnings about this table.

The European convention is a genuine hazard. "1.200" is one thousand two hundred in Germany and one point two in Britain, and a pipeline that guesses wrongly is off by a factor of a thousand. Guess from the document, not from the number: if other figures in the same document use a comma as a decimal separator, that is the convention.

Date normalisation can invert day and month. "03/05/2024" is the third of May in Britain and the fifth of March in the United States, and there is no way to tell from the string. Systems that must handle both should refuse to normalise ambiguous dates silently, and should keep the original text alongside the parsed value so that a human can check it.

The reason this belongs in a chapter about tokenisation rather than in a chapter about numbers is that the decision has to be made before tokens exist. Once "1,200" has become three tokens, the information that it was a single quantity is gone, and the model must rediscover it from context — which, for numbers, it does badly.

## A Worked Count

Take this fragment, three sentences, and count it.

> The pump failed again. The pump was replaced. The new pump failed.

Tokens: 6 + 4 + 4 = 14. Types: the, pump, failed, again, was, replaced, new = 7.

"pump" occurs 3 times, "the" 3 times, "failed" twice. The two most frequent words account for 6 of 14 tokens, or 43%. That proportion is absurd for three sentences and roughly right for a corpus: frequency is concentrated, and it is concentrated in words that carry little content.

## Exercises

1. Tokenise this sentence by whitespace and then by a rule that splits contractions: "It's not the same, is it?" How many tokens in each case?
2. A corpus contains 500,000 tokens and 31,000 types. What is the ratio of types to tokens, and what does a low ratio suggest about the text?
3. Compute the two most frequent adjacent character pairs in: "testing", "tester", "resting", "rested", weighting each word once.
4. A model's context window holds 8,000 tokens. How many words of ordinary English does that correspond to, at 1.3 tokens per word? How does the answer change for a language with longer words?
5. A pipeline removes stop words before classification. Construct a two-sentence example where this changes the label, and one where it does not.
6. An email dataset includes quoted replies from previous messages. Describe two ways this contaminates a sentiment model and how you would detect it.
