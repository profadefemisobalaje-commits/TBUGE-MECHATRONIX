# Evaluation, Bias and the Decision to Ship

The assistant passed its pilot. Two hundred questions, ninety-one per cent answered correctly by a manager's reckoning, a demonstration to the board, and a plan to roll it out to every service desk in the group.

The audit that followed asked a different set of questions. Which two hundred questions? They had been written by the project team, from documents the project team had chosen. What was the ninety-one per cent measured against? One reviewer's judgement, recorded in a spreadsheet. What happens when it does not know? It answers anyway. And what happens when the documents change? Nobody had thought about it.

Every answer was defensible individually. Together they described a system that had never been evaluated against the traffic it would actually receive, by anyone who did not want it to succeed.

This chapter is the one that decides whether the previous twelve were worth writing.

## Three Questions

Any claim about a language system should survive three questions, and they can be asked in thirty seconds.

**What exactly was counted?** Accuracy over what unit — sentences, documents, questions, fields? Scored by whom, against what reference, with what rule for partial credit?

**What was held out?** A test set drawn from the same distribution as training, or from the traffic the system will meet? Split by document or by sentence? How many near-duplicates were removed?

**What happens next month?** What changes — vocabulary, products, policies, the upstream pipeline — and what would detect the change before a user does?

A system whose authors can answer all three is not necessarily good. A system whose authors cannot answer them is not evaluated at all.

## Layers of Evidence

Evaluation is not one experiment; it is a stack, and each layer answers something the one below cannot.

| Layer | Question | Cost |
|---|---|---|
| Held-out test set | Does it work on data like the training data? | Low |
| Slice analysis | Does it work for every group and topic? | Low |
| Adversarial set | Does it fail gracefully on hostile input? | Medium |
| Human review of samples | Would a person accept this output? | Medium |
| Shadow deployment | Does it agree with the current process on live traffic? | High |
| Live trial with review | Does it help, and what does it cost to operate? | High |

The first three can be done before any deployment and are routinely skipped. The fourth is where most projects should spend more time than they do, because human judgement on a stratified sample of two hundred outputs reveals failure modes that no aggregate score can express.

The fifth and sixth are the only ones that measure the system in the presence of real traffic, and they are also the only ones that can be wrong in the direction of optimism if the reviewers know which system produced the output.

## Bias, Concretely

Language models inherit whatever is in their text, their labels and their sampling. The word "bias" is used loosely; the mechanisms are specific.

**Corpus bias.** A corpus of formal written English does not represent how people write in a hurry, in dialect, or in a second language.

**Annotation bias.** Labellers from one background apply one set of judgements. If the reviewed slice is labelled by the same three people, the model learns their habits and the evaluation confirms them.

**Sampling bias.** Traffic from one region, one product line, one customer tier. The system is excellent where it was measured and untested elsewhere.

**Objective bias.** A model trained to maximise agreement with past decisions reproduces those decisions, including the ones the organisation has since decided were wrong.

The measurable form of all four is **disaggregation**: compute the metric per group, per topic, per source, and report the worst slice alongside the average.

A worked example, on 5,000 classification decisions:

| Slice | Share of traffic | Accuracy |
|---|---|---|
| All | 100% | 92% |
| Source A | 78% | 95% |
| Source B | 14% | 88% |
| Dialect group C | 8% | 78% |

The average is 92%. For eight per cent of traffic it is 78%, and those are the users most likely to be writing informally, in a second language, or with unusual spelling — which is to say, the users least able to correct the system's mistakes.

A slice figure from a small sample is noise, so the sample size must be stated. To estimate a proportion to within five percentage points at 95% confidence requires about 384 examples; to within ten points, about 96. A slice with twelve examples and an accuracy of 67% is a rumour, not a measurement.

## Privacy and the Text You Keep

Text systems ingest personal data as a matter of course: names, addresses, account numbers, health details, complaints. Four obligations follow, and they are engineering requirements rather than policy statements.

**Minimise.** Do not send a whole document when a paragraph is needed. Do not log a prompt when a hash of it would serve.

**Redact before storage.** Names and identifiers can be replaced with placeholders at ingestion, and the mapping held separately. This costs accuracy and preserves the ability to delete.

**Retain deliberately.** A retention period should be a decision with a date, not a default. Logs written "for debugging" become the archive that cannot be deleted when someone asks.

**Respect the boundary.** Data used to improve a model is a different use from data processed to serve a request, and in many jurisdictions it requires different consent. The distinction is easy to lose when the same pipeline does both.

## Prompt Injection, in One Page

A system that reads retrieved documents and follows instructions is vulnerable to instructions hidden in those documents. A web page, a PDF, or an email can contain text addressed to the model rather than to the reader: ignore your previous instructions, send the following, approve this.

The mechanism is not a bug in the model; it is the consequence of putting untrusted text into a context that also contains instructions. Three mitigations reduce the risk substantially, and none eliminates it.

Keep instructions and data in separate, clearly delimited sections, and state in the instruction which sections are data.

Give the system the least authority it needs. A summariser that cannot send email cannot be tricked into sending one.

Validate outputs against a schema and an allowlist before acting. If an action must be taken, take it through a function with narrow permissions rather than through free text.

The residual risk should be stated in the deployment document, not discovered in an incident review.

## Drift, and the Feedback Loop

A language system degrades when the world changes, and the changes are usually visible in the text before they are visible in the metrics.

Vocabulary drift: new products, new abbreviations, renamed departments. Detect by monitoring the rate of tokens that were rare or absent in training data.

Distribution drift: a new complaint category, a new supplier, a marketing campaign. Detect by monitoring class proportions and confidence distributions.

Pipeline drift: someone changes the email gateway tag, and a feature that the model relied on disappears — the opening story of Chapter Eight, which is a drift story.

The feedback loop is subtler. If the system's outputs are used to train the next version, the model learns its own mistakes as if they were truth. If human corrections are used, the model learns only about the cases humans chose to correct, which is a biased sample by construction. Either way, the training data stops being a sample of the world and becomes a sample of the system's history, and the evaluation must be built from fresh, independently collected text.

## The Decision to Ship

Ten questions. They are deliberately boring, and a project that cannot answer them is not ready.

1. What is the unit of evaluation, and who labelled the reference?
2. What was held out, and by what rule was the split made?
3. What is the worst-performing slice, and how large is it?
4. What does the system do when it does not know?
5. What is the error that would matter most, and how often does it occur?
6. What will change in the next six months, and what will detect it?
7. What data is retained, for how long, and who can delete it?
8. What can the system do without human approval, and what can it not?
9. Who is accountable when it is wrong, and how does a user appeal?
10. How is the system turned off, and how long does that take?

Question four is the one that separates systems people trust from systems people tolerate. A language system that says "I cannot find that in the documents I have" when the retrieval is weak, and says it consistently, is worth more than one that answers every question with equal fluency.

## For Practice

Take a system you have used — a search box, a chat assistant, a spam filter — and answer the ten questions about it. The gaps are the interesting part: which cannot be answered from outside, and what that tells you.

Then write the deployment paragraph for a system you would like to build: what it does, what it is measured on, and what it refuses. If you cannot write it, the system is not understood.
