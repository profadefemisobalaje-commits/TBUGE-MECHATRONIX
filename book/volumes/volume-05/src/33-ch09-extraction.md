# Extraction: Names, Relations and Structure

An accounts payable team automated invoice entry. The system extracted six fields per invoice — supplier, invoice number, date, purchase order, net total, tax — and reported 94% accuracy across all fields. The business case assumed the six per cent would be caught in review.

Nobody had done the multiplication. If each field is right 94% of the time and errors are independent, the chance that all six fields of an invoice are correct is 0.94^6 = 0.69. Nearly a third of invoices needed correction, not six per cent, and the review queue was designed for a tenth of that volume.

The arithmetic of extraction is the arithmetic of conjunctions: accuracy per field multiplies, and review capacity does not.

## The Shape of the Task

Extraction turns unstructured text into fields. Three sub-tasks, which are usually confused with one another.

**Finding spans.** Locating a piece of text: the supplier name, the date, the amount.

**Classifying spans.** Deciding what each piece is: this string is an organisation, that one is a location.

**Assembling records.** Combining spans into a structure that satisfies a schema, with relations between them: this total belongs to this purchase order.

The standard notation for the first two is a tagging scheme, and it is worth doing once by hand.

> Send 40 boxes to Acme Ltd in Leeds on 3 May

| Token | Tag | Meaning |
|---|---|---|
| Send | O | outside any entity |
| 40 | B-QTY | begins a quantity |
| boxes | B-PROD | begins a product |
| to | O | |
| Acme | B-ORG | begins an organisation |
| Ltd | I-ORG | continues it |
| in | O | |
| Leeds | B-LOC | begins a location |
| on | O | |
| 3 | B-DATE | begins a date |
| May | I-DATE | continues it |

The B and I prefixes exist to handle multi-token entities; without them, "Acme" and "Ltd" would be two unrelated organisations. A model trained on this scheme learns to predict a tag per token, and the tags are then grouped back into spans.

## Rules First, and Honestly

A large fraction of extraction is better done with rules, and refusing to use them is a common affectation.

Invoice numbers have a pattern. Dates have a small number of formats. Part codes often begin with a fixed prefix. A regular expression finds these perfectly, costs nothing to run, and can be read by an auditor — which matters, because extraction usually feeds a financial or safety process.

Rules have two weaknesses, and they are worth naming precisely.

They break on variation. "3 May", "3rd May", "May 3", "03/05/2024" and "2024-05-03" are one fact. A rule set that handles all five is a small program, and the day a supplier writes "03.05.24" it fails.

They cannot generalise to unanticipated strings. A supplier name has no pattern; it is whatever the supplier calls itself.

The workable arrangement is a hybrid: rules where the format is standardised and legally constrained, models where the text is free, and a validation layer that checks the assembled record for internal consistency.

## Measuring Extraction Properly

Entity extraction is scored by span overlap, and the arithmetic has a trap.

Suppose the system produced 100 predicted entities, of which 80 match a gold entity exactly. The gold data contains 95 entities.

> precision = 80 / 100 = 0.80
> recall = 80 / 95 = 0.84
> F1 = 2 × 0.80 × 0.84 / (0.80 + 0.84) = 0.82

The trap is what counts as a match. "Acme Ltd" against "Acme Limited" is a partial match; a strict scorer counts it as an error, a lenient one as correct, and the difference between the two can be twenty points of F1. The scoring rule must be written down before the numbers are quoted, and it must match how the output will be used: if the field is written into an accounting system, an abbreviation difference is a real error.

A second trap: token-level accuracy flatters. A sentence with eleven tokens and one entity has eight "O" tags, so a system that predicts "O" everywhere scores well on tokens and zero on entities. Entities are the unit of measure.

## Confidence, and the Human in the Loop

A model that predicts a field can also predict how sure it is, and the usefulness of that number depends entirely on whether it is calibrated.

Calibration is measured by binning. Take every field the system extracted, group them by predicted confidence, and compute the actual accuracy in each group.

| Confidence band | Fields | Correct | Actual accuracy |
|---|---|---|---|
| 0.95–1.00 | 4,200 | 4,116 | 98.0% |
| 0.80–0.95 | 1,600 | 1,408 | 88.0% |
| 0.50–0.80 | 300 | 219 | 73.0% |
| below 0.50 | 100 | 41 | 41.0% |

A well-calibrated model has actual accuracy close to predicted confidence in every band. Here the top band is better than advertised and the middle band is worse, which is common: models are under-confident when they are right and over-confident when they are wrong.

The value of the table is that it converts a threshold into a staffing decision. If the review team can handle 1,500 fields a day, the policy "review everything below 0.95" produces about 2,000 — too many — while "review everything below 0.80" produces 400, and the expected error rate among the unreviewed is the accuracy in the top band, which is 2%.

That last number is the one that must be quoted to the business, and it must be quoted with its sample size. A band containing 4,200 fields gives an accuracy estimate with a margin of about one percentage point; a band containing a hundred gives a margin of ten, and a policy built on it is built on noise.

Two disciplines make this work in practice.

Recalibrate after every model change. Confidence scores are not comparable across versions, and a threshold carried over from the previous model may review nothing or everything.

Log the review outcome, not only the decision. The only way to know whether the top band is really 98% next quarter is to sample it and check, which is the same argument as the capability study in the previous volume.

## Relations, Which Are Harder

Fields in isolation are easy; the relations between them are where invoices are lost.

| Relation | Example | Failure mode |
|---|---|---|
| total belongs to invoice | one total, several line items | picks the subtotal |
| invoice references order | "against PO 4471" | misses the reference |
| supplier issues invoice | letterhead, signature block | confuses buyer and seller |
| tax applies to net | two amounts, one rate | assigns the wrong rate |

These are usually extracted as triples — subject, relation, object — and then checked against a schema. The checks are where most of the reliability comes from, and they are cheap:

Does the total equal net plus tax?

Does the tax rate correspond to a plausible jurisdiction?

Is the invoice date later than the order date?

Does the purchase order exist?

Each check catches a class of error that no amount of model improvement would catch, because the error is visible only in the relationship between fields, not in any single field.

## The Review Queue Is a Design, Not a Failure

Given per-field accuracy, the volume of work is a calculation, and it should be done before the system is built.

Ten thousand invoices, six fields, 94% per field:

> field errors = 10,000 × 6 × 0.06 = 3,600
> invoices needing any correction = 10,000 × (1 − 0.69) = 3,100

If a reviewer can correct an invoice in ninety seconds, that is seventy-seven hours of work a month — roughly half a person. The case may still be excellent: it may replace a hundred and fifty hours of manual entry. But the number must be computed, and the review capacity designed around it, or the queue becomes the system's reputation.

| Policy | Effect |
|---|---|
| Review everything | Accuracy never improves; cost unchanged |
| Review low-confidence only | Needs calibrated confidence |
| Review by risk | High-value invoices always, rest sampled |
| Sample audit | Detects drift, does not correct errors |

The third and fourth rows are usually combined in practice: a rule that high-value invoices are always checked, plus a random sample of the rest to measure the error rate over time. The sample is what tells you whether the model is still working in month six.

## Exercises

1. A system has 96% accuracy per field and extracts four fields. What fraction of records is fully correct? How does that change at 99% per field?
2. Tag the sentence "Deliver 12 valves to Beta Engineering in Ibadan before 9 June" using B and I prefixes.
3. Precision is 0.75 and recall 0.60. Compute F1. If recall rises to 0.70 at the same precision, what is the new F1?
4. Write four validation checks for an invoice record that a regex alone could not provide.
5. A reviewer handles forty invoices an hour and there are 6,000 invoices a month. How many reviewer hours are needed if 30% require correction?
6. A supplier starts writing dates as "12.vi.24". Explain what happens to a rule-based extractor, to a model-based one, and to a hybrid, and say which you would rather operate.
