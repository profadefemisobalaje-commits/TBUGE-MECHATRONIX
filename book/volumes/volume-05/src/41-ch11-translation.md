# Translation and the Problem of Equivalence

A translated warning label read, in the target language, "the guard may be removed while the machine is running". The source said "the guard must not be removed while the machine is running". One word had been dropped, the sentence remained grammatical, and the label was now an instruction to do something dangerous.

The translation system had been evaluated on a general corpus and had scored well. Nothing in that score distinguished an error that misplaced a comma from an error that inverted a safety instruction.

Translation is the clearest case in this volume of a task where the metric and the purpose are not the same thing.

## There Is No Single Right Answer

Begin with a sentence and three published translations of it. All three are correct. They differ in rhythm, in the order of clauses, and in whether an idiom is preserved or replaced.

> The engine will not start if the fuel cap is loose.

A faithful version keeps the conditional at the end; a natural version reverses it; a terse version becomes two sentences. A machine that produces any of them has succeeded, and a metric that compares against one reference will mark two of them wrong.

This is the **equivalence problem**, and it is not a technicality. Translation is not a substitution cipher between languages; it is the production of a text that does the same job in a different culture of writing. Word order differs, articles appear and disappear, polite forms carry information that English marks with modals, and compound nouns unpack into phrases.

| Source phenomenon | What happens in translation |
|---|---|
| German verb-final clauses | Reordering across the whole sentence |
| Japanese topic markers | Subject supplied or dropped |
| English phrasal verbs | Single verbs in Romance languages |
| Measure words | Required in some languages, absent in others |
| Decimal comma | 1.5 becomes 1,5 — and a machine may "correct" it |

The last row is not a curiosity. A number converted between conventions without care changes a specification by a factor of ten, and no grammar check will notice.

## Alignment: The Old Machinery

Before neural methods, translation was assembled from statistics over aligned text: sentence pairs from bilingual documents, aligned at the word level by counting co-occurrence, then phrases extracted and reordered by a model of movement.

The word alignment step is the same distributional idea as Chapter Four, applied across languages: the English word "pump" co-occurs with the German "Pumpe" far more often than chance, in sentences that are translations of one another. A handful of such correspondences, extracted from millions of sentence pairs, is enough to translate.

Two consequences survive into modern systems. Terminology is learned from data, so a domain with distinctive vocabulary — medical, legal, industrial — needs its own parallel text or an explicit glossary. And word order differences are the hardest part, which is why reordering was the central problem of the field for two decades.

## Encoder, Decoder, Attention

The modern arrangement is conceptually simple, and it reuses the machinery of the previous part.

An **encoder** reads the source sentence and produces a sequence of vectors, one per token, each informed by its neighbours through attention. A **decoder** generates the target sentence one token at a time, attending to the encoder's vectors as it goes. At each step it decides which source words matter — which is exactly the alignment problem, learned rather than counted.

Nothing in this description involves understanding. The system has learned a function from source sentences to target sentences, and the function is good because the training data was enormous.

## Measuring Translation: BLEU, and Its Arithmetic

The conventional automatic measure compares the system's output with one or more human references, counting overlapping word sequences.

Take a candidate of five words and a reference that shares four of its words and two of its word pairs.

> 1-gram precision = 4/5 = 0.80
> 2-gram precision = 2/4 = 0.50

BLEU combines the precisions geometrically, with a brevity penalty for outputs shorter than the reference. With equal lengths by assumption:

> BLEU-2 = sqrt(0.80 × 0.50) = 0.632

A score of 0.632 on a two-gram BLEU is respectable; four-gram BLEU scores are lower and are the usual published figures.

The measure has known properties, and they explain a great deal of published confusion.

It rewards word overlap, so a valid paraphrase scores badly. Two human translators often score lower against each other than a machine does against one of them.

It is sensitive to tokenisation. Change how punctuation or compounds are split and the score moves several points without any change in quality.

It does not distinguish error types. Dropping "not" and misspelling a name cost the same order of magnitude as changing a preposition.

| Score movement | Likely cause |
|---|---|
| 3 points down after a tokeniser change | Measurement artefact |
| 5 points up on in-domain test set | Domain match, not general improvement |
| 1 point up, human reviewers prefer new output | Real but small |
| No change, users complain more | Metric not measuring what users see |

## What Must Be Measured Instead

For any translation that will be acted upon, the useful measurements are categorical and human.

**Adequacy** — does the translation convey the same information? A reviewer marks each sentence as correct, partly correct, or wrong.

**Fluency** — is it grammatical in the target language? Independent of adequacy, and sometimes in tension with it.

**Critical error rate** — the fraction of sentences containing an error that changes meaning, inverts a negation, alters a number or unit, or corrupts a name. This is the number that matters for instructions and labels, and it is the number that BLEU does not report.

A worked example from a hundred-sentence sample:

| Category | Sentences |
|---|---|
| Fully correct | 71 |
| Minor error, meaning intact | 17 |
| Meaning changed | 9 |
| Negation or number corrupted | 3 |

A BLEU score of 45 would be reported as strong. The critical error rate is 12%, and for a safety label it is disqualifying. Both numbers are true, and only one of them is about the application.

## The Practical Arrangement

Three rules cover most industrial translation work.

**Glossary first.** Product names, part numbers, units and regulated terms are not translated by statistics; they are fixed by a glossary applied before and after the model. This is cheap and prevents the most embarrassing errors.

**Numbers and negations checked by rule.** A post-translation check that confirms every number, unit and negation in the source appears in the target catches the errors that matter most and costs almost nothing. It is not a model; it is a matching procedure.

**Human review proportional to consequence.** A marketing page can ship with machine output and a light edit. A warning label cannot. The decision is about consequence, not about the quality of the system.

## Problems

1. A candidate translation has 20 words; 15 of its words appear in the reference and 8 of its bigrams do. Compute 1-gram and 2-gram precision, and BLEU-2 assuming no brevity penalty.
2. Explain why two professional translators' outputs might score BLEU 30 against each other, and what that implies about a machine scoring 40.
3. Give three examples of source text where a single dropped word changes the meaning dangerously.
4. A sample of 200 translated sentences contains 14 with changed meaning, 4 of which invert a negation. What is the critical error rate, and what would you recommend for a technical manual?
5. Describe a rule-based post-check that catches decimal-comma errors, and state one case it would miss.
6. A supplier offers a translation system scoring BLEU 52 on news and 31 on your maintenance manuals. Which number governs the decision, and what would you test next?
