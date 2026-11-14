# Classifying Text

A classifier that routed support email to the right team reported 97% accuracy in testing. On the live queue it was wrong about one message in five, and the errors had a comic consistency: every message that had been forwarded internally was routed to "IT".

The tag "[EXTERNAL]" that the mail gateway appended to incoming messages had been stripped by the cleaning step, so its absence became the signal for "forwarded internally". The model had found a perfect predictor of the wrong thing, and no amount of tuning would have fixed it, because the predictor was genuinely perfect in the training data.

Text classification is the most-used application of language processing and the one where contamination is easiest. This chapter is about building one that survives contact with production.

## From Text to Features

A classifier needs numbers. Four options, in increasing complexity.

**Bag of words.** Count each vocabulary word in the document. Loses order entirely, and works surprisingly well.

**tf-idf.** Weight each count by how rare the word is across documents, as computed in Chapter Three. The standard baseline for retrieval and classification, and hard to beat on small datasets.

**Averaged embeddings.** Replace each word with its vector and average. Captures similarity between words, loses exact terms.

**Learned representations.** A network reads the text and produces a vector. Best when data is plentiful, and it needs thousands of labelled examples before it beats tf-idf.

A worked tf-idf for one document in a collection of 1,000, where "leak" occurs twice and appears in 50 documents:

> tf = 2 / (number of words in document) — say 2/120 = 0.017
> idf = log(1,000 / 50) = 3.0
> weight = 0.017 × 3.0 = 0.05

And for "the", occurring twenty times and appearing in every document:

> idf = log(1,000 / 1,000) = 0
> weight = 0

The frequent, uninformative word is eliminated by arithmetic rather than by a stop-word list. That is the appeal of the method.

## Naive Bayes, Done by Hand

The oldest classifier is still a serviceable baseline and can be computed with a pencil.

Suppose 100 emails: 40 spam, 60 ordinary. The word "free" appears in 24 spam and 6 ordinary messages.

> P(free | spam) = 24/40 = 0.60
> P(free | ordinary) = 6/60 = 0.10
> P(spam) = 0.40, P(ordinary) = 0.60

Multiply and compare:

> spam: 0.40 × 0.60 = 0.24
> ordinary: 0.60 × 0.10 = 0.06

Normalising gives a posterior of 0.24 / 0.30 = 0.80 for spam on the strength of one word. Add more words and the product extends.

The "naive" in the name is the assumption that words are independent given the class, which is false — "credit" and "card" are not independent — and yet the ranking it produces is often good. What it produces is not a calibrated probability, and treating 0.80 as "80% likely" is a mistake the next section addresses.

Two practical notes. Unseen words must be smoothed, exactly as in Chapter Six, or one unseen term zeroes the product. And the class priors must reflect deployment: a corpus that is half spam will produce a classifier that flags far too much when deployed on a mailbox that is 5% spam.

## The Integrity of the Split

This is where text classification fails, and it fails in ways that are invisible in a notebook.

| Leakage source | How it happens | Effect |
|---|---|---|
| Same thread in train and test | Random split over messages | Validation score inflated |
| Near-duplicate documents | Templated emails, quoted replies | Model memorises templates |
| Sender in both sets | One person's style | Learns the person, not the topic |
| Time | Train on 2023–24, test randomly | Ignores drift between years |
| Label-derived features | ID numbers correlated with class | Learns the annotation order |
| Boilerplate | Signatures, disclaimers, gateway tags | Learns the plumbing |

The last row is the opening story, and it is the most common of all. The defences are mechanical: strip known boilerplate, deduplicate by similarity, split by thread or by sender or by date, and inspect the most predictive features of the fitted model. If the top feature is a tag rather than a topic, the model is measuring the plumbing.

Looking at the top features takes ten minutes and is the single most valuable diagnostic in applied text work.

## Choosing the Metric

Accuracy is a poor summary, for the reasons established in Volume Three, and text makes it worse because class frequencies are usually extreme.

The alternatives:

**Precision and recall** per class, with the operating threshold stated.

**F1**, the harmonic mean, when a single number is demanded and the two error types are equally costly.

**Macro-average** across classes, which weights each class equally and therefore punishes a model that ignores a rare class. **Micro-average** weights by frequency and flatters it.

**Calibration**, which asks whether a predicted 0.8 corresponds to a frequency of 80%. A model can rank well and be badly calibrated, and a threshold chosen on uncalibrated scores will not transfer between datasets.

For a routing system, the relevant question is not accuracy at all. It is: how many messages per day reach the wrong team, and what does that cost in delay? That question requires the confusion matrix and a cost per error, and nothing else.

## Thresholds and the Cost of Being Wrong

A classifier outputs a score; a decision requires a threshold, and the threshold encodes a judgement about relative costs.

For routing, sending a message to the wrong team costs a few hours of delay. Sending it nowhere costs a customer. So the threshold for "confident" should be high, and everything below it should go to a human queue — which is not a failure of the model but a design decision that uses it where it is reliable.

This arrangement — automate the confident cases, queue the rest — is how nearly every deployed text classifier actually behaves, and it has the pleasant property that its performance can be measured directly as the fraction of traffic that avoids the queue and the error rate within it.

## Problems

1. A collection has 2,000 documents and "bracket" appears in 100. Compute its idf, and the weight of a 200-word document containing it twice.
2. Using the Naive Bayes numbers above, compute the posterior if "free" appeared in 12 spam and 12 ordinary messages. What changed, and why?
3. A routing classifier reports 95% accuracy across five classes. Class sizes are 800, 100, 50, 30 and 20. Compute the accuracy of a model that always predicts class one, and explain what that implies.
4. Name three boilerplate features that leak into email classifiers, and how you would detect each.
5. A model has precision 0.9 and recall 0.4 on the "urgent" class. At 600 urgent messages a month, how many are missed, and how many false alarms does it raise?
6. Design a split for 8,000 tickets from three years and four products, deployed next month. State the rule and the reason.
