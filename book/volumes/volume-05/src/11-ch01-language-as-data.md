# What Language Looks Like to a Machine

The complaint came from a warehouse in Leeds. A spell-checking step in an order-entry system had begun flagging every product code that contained the letters "BOLT", because a dictionary of ordinary English does not contain that string, and the nearest word by edit distance was "BOAT". The system was not malfunctioning. It was doing exactly what it had been told: compare each token with a list of known words, and flag the ones that are close to a known word but not equal to it.

The interesting part is the complaint that followed. The warehouse asked for the dictionary to be updated. The engineer, sensibly, asked instead why product codes were being spell-checked at all, and discovered that the pipeline ran every field through the same cleaning function because the function was convenient.

This is the pattern of the first part of this book. Language processing fails less often because a model is weak than because a decision about *what a word is* was made once, by accident, and then applied to everything.

## A String Is Not a Word

At the lowest level, text is a sequence of code points encoded as bytes. UTF-8 uses one byte for ordinary English letters, two for accented Latin characters, three for most other scripts, four for emoji and rarer symbols.

| Text | Code points | Bytes in UTF-8 |
|---|---|---|
| cat | 3 | 3 |
| café | 4 | 5 |
| € | 1 | 3 |
| — | 1 | 3 |

Three consequences follow, and each has produced a real bug in a real system.

Length is not the number of visible characters. A field limited to forty bytes holds thirteen emoji, not forty.

Upper and lower case are not always paired. The German sharp s, the Turkish dotless i, and the Greek final sigma all break the assumption that case conversion is reversible. Turkish in particular has produced a generation of systems that turn a capital I into a dotted i when the correct answer is the dotless form. Emoji, which take four bytes each, make the same point about length.

Slicing by byte can cut a character in half. A truncation at two hundred bytes may land inside a three-byte character, producing invalid text that later stages will reject or, worse, silently corrupt.

None of this is exotic. It is the everyday arithmetic of handling text, and it is the reason production systems agree on an encoding — UTF-8 — at every boundary and validate it on entry.

## Ambiguity Is Not an Edge Case

A word in isolation carries almost no information. "Bank" is a financial institution or a river edge. "Sanction" means to permit and to punish. "Fast" means quick and immobile. "Bolt" is a fastener, a verb for running, and a roll of cloth.

Human readers resolve these instantly using context, and the resolution feels like knowledge of meaning. For a machine, the resolution is a statistical decision over neighbouring words, and it is worth seeing that stated plainly, because it sets the ceiling of everything in this volume.

Consider the two sentences:

> The bank raised its rate.
> The bank was steep and muddy.

A classifier that sees only the word "bank" cannot do better than guess. One that sees "rate" or "muddy" can do very well. The information that disambiguates is *distributional* — it lives in which words appear near which others — and that single observation is the foundation of the modern field.

## Cutting Sentences

Before words, sentences. It sounds trivial until the text contains "Dr. Smith arrived at 4.30 p.m. on Tuesday," which has three apparent sentence ends and one actual one.

Rules of thumb that work reasonably: a full stop is a sentence end if followed by a space and a capital letter; abbreviations are a known list; a decimal point is never a sentence end; a single capital letter followed by a period is usually an initial.

The failure cases matter in production. Academic citations, legal numbering, and chemical names produce sentences that end nowhere and paragraphs that end mid-clause. When a downstream task depends on sentence boundaries — summarisation, or anything that scores per sentence — the boundary errors propagate invisibly, and a model can appear to fail at summarisation when it is failing at splitting.

## Distance Between Strings

One of the oldest and most useful tools treats text as a sequence of characters and asks how far apart two strings are. The **edit distance** is the smallest number of insertions, deletions and substitutions that turn one string into another.

Take "kitten" and "sitting". Substitute k for s at the first position, substitute e for i at the fifth, insert g at the end. Three edits, so the distance is three.

The recurrence is a small table, and it is worth filling once by hand:

> distance[i][j] = min(distance[i-1][j] + 1, distance[i][j-1] + 1, distance[i-1][j-1] + cost)

where cost is zero if the characters match and one if they do not. The table has one more row and column than the strings, filled from the top left, and the answer is in the bottom right corner.

This distance is the engine behind spelling correction, fuzzy matching of names, and the detection of near-duplicate records — the last of which is more valuable than it sounds, because duplicate near-matches are how a text dataset gets contaminated.

## What a Pipeline Looks Like

Four stages, and every system in this volume is some arrangement of them.

| Stage | Question | Typical decisions |
|---|---|---|
| Acquisition | What text do we have, and from where? | Source, licence, time span, language |
| Normalisation | What counts as the same text? | Case, accents, punctuation, numbers, encodings |
| Tokenisation | What are the units? | Words, subwords, characters, sentences |
| Representation | How is a unit turned into numbers? | Counts, vectors, identifiers |

Each decision is a modelling choice with a consequence, and the consequences are not symmetric. Lowercasing makes "Bank" and "bank" identical, which helps topic models and hurts named-entity recognition. Removing punctuation makes "3.5" into "35", which is harmless for sentiment and catastrophic for finance. Stripping stop words removes "not", which reverses the meaning of every sentence that contains it.

The rule that survives every project: decide once, write the decision down, and apply the same function to training text and to production text. A pipeline whose training data was cleaned differently from its live data is measuring one thing and deploying another.

## Working Notes

1. How many bytes does the string "naïve café" occupy in UTF-8? How many characters does a human see?
2. Compute the edit distance between "form" and "farm", and between "form" and "from". Which pair would a spell-checker confuse more readily, and why?
3. A system truncates user input at 500 bytes. Give two inputs where this produces a different result from truncating at 500 characters.
4. "I did not like the film" and "I did like the film" differ by one token. Explain what a stop-word filter does to the second sentence and to a sentiment classifier's accuracy.
5. A colleague proposes lowercasing all text, removing punctuation, and stripping digits before training a classifier that must detect invoice totals. Name two specific failures.
6. List the four pipeline stages for a system that reads customer emails and routes them to a department. Write one decision for each stage.
