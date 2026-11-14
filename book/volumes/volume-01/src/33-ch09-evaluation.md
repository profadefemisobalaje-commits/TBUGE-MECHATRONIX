# How Wrong Is It, Really?

There is a particular kind of meeting that anyone who has worked on these systems will recognise. A team presents a model. The accuracy is 94%. The room is pleased. Somebody asks how it was measured, and the answer is a dataset that the team has been looking at for six months.

The number is real. It is also, in a sense that will become clear, a measurement of the team rather than of the model. This chapter is about the difference, and about the habits that keep a result honest after the novelty has worn off and the system is running at three in the morning with nobody watching.

## Three Sets, Not Two

The basic rule from the learning chapter is that you judge a model on data it has never seen. In practice that rule needs one more split, because development involves choices.

Divide the data into three parts.

**Training** data is what the model learns from. **Validation** data is what you use while deciding between models, tuning thresholds and trying features. **Test** data is opened once, at the end, to report a number you can defend.

The reason for the middle set is that every time you look at a score and adjust something in response, you leak a little information from that score into the model. Do it fifty times and the validation set has become training data by another name. Keep a set that you have never looked at, and the final number means something.

For small datasets, three-way splits waste data. A technique called **cross-validation** helps: divide the data into, say, five parts, train five times with a different part held out each time, and average the results. Every case gets used for training four times and for testing once. It is slower and it is honest, and for the pump table in the last chapter it would have told you clearly how little ten rows can support.

## Leakage, and How It Gets In

The most common way a project fools itself is not a statistical subtlety. It is a column in the spreadsheet that contains the answer.

A maintenance dataset includes a column called “repair date”. It is empty for pumps that have not failed, and filled for pumps that have. Train on that column and the model achieves near-perfect accuracy, because it has learned to read the future. The fix is to ask, of every column: would I know this value at the moment I need to make the prediction? If not, the column is not a feature.

Leakage arrives in less obvious forms as well.

**Duplicates.** The same photograph appears in both training and test sets, resized or cropped. The model memorises it and scores well on a test that is not a test.

**Group leakage.** X-rays from the same patient appear in both sets. The model learns the patient's anatomy rather than the disease. Splitting by patient is the fix.

**Time leakage.** A model that predicts tomorrow's demand is trained on a random sample of days, including days after the ones it is tested on. Split by time, always, when the task is forecasting.

**Preprocessing leakage.** The mean and spread used to scale the features are computed over all the data, including the test set. The model then knows something about the test set before it sees it. Fit the scaling on training data only.

None of these produce an error message. All of them produce a number that is too good, and a system that disappoints in service.

## The Benchmark Trap

Benchmarks have driven the field forward, and they have also taught it to cheat.

The ImageNet competition, which ran from 2010, asked systems to classify photographs into a thousand categories. In 2012 the winning deep network reached a top-five error of about 15%, against roughly 26% for the runner-up, and the result changed the direction of the field. By 2015 the best systems were below 4%, and the benchmark had, in a sense, been solved.

Something similar happened in language. Benchmarks such as GLUE measured how well systems handled a range of comprehension tasks. They were useful. They were then optimised against so hard that they stopped discriminating between good systems and lucky ones.

The mechanism is worth naming, because it is the same mechanism as overfitting, applied to research communities instead of models. When thousands of teams optimise against a fixed test set, information about that set leaks into the field. Results improve faster than the underlying capability. Then a new, harder benchmark appears, and the improvement slows abruptly, which is evidence that some of the earlier progress was aimed at the test rather than at the task.

The practical defence is the one your grandmother would recommend: keep a test set that is yours, drawn from your own world, and never publish its contents. A general benchmark tells you whether a method is promising. Only your own data tells you whether it works for you.

## A Service That Drifted

In 2008, Google launched Flu Trends, which estimated the level of influenza in a region from the volume of flu-related searches. It was a genuine success. In the United States, its estimates tracked official surveillance data closely, and it reported them about two weeks earlier, because people search before they see a doctor. The paper describing it, published in *Nature* in 2009, became a standard example of what large-scale data could do.

Then it drifted. For several seasons, including 2012–13, it substantially overestimated the number of cases; some analyses put the error at more than double the true figure. Google changed its search suggestions. People's habits changed. Media coverage changed what people typed. The model had been fitted to a world that no longer existed.

There was a methodological problem underneath the commercial one. The search terms had been selected partly by checking how well they matched past flu data — including the very seasons later used to judge the model. That is a mild form of the leakage described above, and it flattered the early results. The service was discontinued in 2015.

The lesson is not that search data is useless for epidemiology. It is that a model is a hypothesis about a distribution, and distributions move. Any system that does not measure itself after deployment is, sooner or later, reporting the past.

## Confidence, Revisited

The previous chapter introduced calibration as a property of a single prediction. At the level of a whole system, it becomes a monitoring question with a simple test.

Sort the system's outputs into buckets by stated confidence. In the 0.8 bucket, check how often it was right. If it was right 0.8 of the time, that bucket is calibrated. If it was right 0.65 of the time, the system is overconfident by a wide margin.

Two things follow. First, thresholds set from those numbers are wrong, because they were chosen as if the confidence meant what it said. Second, the system's own internal sense of difficulty is broken, so it cannot tell you when to ask for help.

Calibration is fixable, and it is measured on held-out data like everything else. What is not fixable is the belief that a softmax output is a probability in the everyday sense. It is a number produced by an arithmetic operation, and it becomes a probability only after you have checked.

## A Short List That Survives Contact

If you remember nothing else from this chapter, keep these five habits. They are unglamorous and they catch most of the failures that matter.

Split by time, by group and by person, not at random, whenever the real deployment will meet new times, groups or people.

Ask of every feature whether it would be available at prediction time. If not, remove it, even if it is delicious.

Fit every transformation on training data only, and apply it unchanged at run time.

Keep a private test set drawn from your own world, and open it once.

After deployment, measure again every month, on fresh labelled data, and plot the number over time. A flat line on that plot is the only evidence that a model is still working.

## Exercises

1. A hospital wants a model that predicts which patients will be readmitted within a month. Write down three columns that would leak the answer, and explain in one sentence each how the leak works.

2. Design the split for that model. Do you split by patient, by admission, by hospital, by date, or by some combination? Justify each choice, and say what would go wrong if you split at random.

3. A vendor reports 97% accuracy on a public benchmark. Write the five questions you would ask before believing that this implies anything about your hospital.

4. Sketch the monthly monitoring chart for a deployed model: what is on the vertical axis, what triggers an alarm, and what would you do when it fires?

5. Think of a number you have quoted about a system's performance — from a news story, a product page or a lecture. Rewrite it so that it states the dataset, the split, the date and the uncertainty. If any of those is missing, say what is missing.
