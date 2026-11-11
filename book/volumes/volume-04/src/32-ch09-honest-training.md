# Training a Vision Model Without Fooling Yourself

The report said 99.2%. It was printed, bound, and presented to the steering group, which approved the deployment.

On the line the system found 71% of the defects it was supposed to find, which is still respectable, and 40% of the good parts were rejected, which was not. The plant ran it for a fortnight with every rejection double-checked by hand, and the resulting log — four hundred decisions a day, two weeks — is one of the most useful documents the project produced.

The 99.2% was not a lie. It was an answer to a different question. The dataset had been captured by filming each of forty sample parts for fifty consecutive frames, then splitting the resulting 2,000 images randomly into training and validation. Every part in the validation set had thirty-nine near-identical twins in the training set. The model was not recognising defects; it was recognising parts it had already memorised, and the validation score was measuring that memorisation.

This chapter is about the decisions that make a vision dataset honest, and they are almost entirely about splitting and labelling. Architecture will forgive a great deal. A contaminated split forgives nothing, because it hides the failure until the failure is in production.

## The Split Is the Claim

A validation score is a claim about the future. The claim is only as good as the resemblance between the validation data and the future.

There are four ways to split image data, and they answer four different questions.

| Split | Construction | Question it answers |
|---|---|---|
| Random | Shuffle all images | How well does it fit this dataset? |
| By object | All images of one part stay together | Can it recognise a new instance? |
| By scene | All images from one setting stay together | Can it cope with new conditions? |
| By time | Train on earlier captures, test on later | Will it still work next month? |

Random splitting is the default in every library, and it is almost always wrong for images, because images of the same object are not independent samples. Fifty frames of one part are one sample, repeated fifty times, and random splitting distributes that sample across both sides of the wall.

The consequence is arithmetic, not opinion. With 80% of images in training and forty images per part, a validation image has around thirty-nine siblings in training. The model only has to memorise forty appearances to score perfectly. Move to a by-object split and the same model, on a truly unseen part, drops from 99% to somewhere between 75% and 90% — which is the number the line later produced.

Both splits are computable from the same dataset. Only one of them predicted the outcome.

## Duplicates Are Everywhere

Frames from a video are the obvious case. Four more are common and less obvious.

**The same part photographed twice under slightly different setup.** A dataset that looks like 800 images may contain 400 pairs.

**Augmented copies stored as separate files.** If the augmentation was applied before splitting, every augmented copy of a training image is a near-duplicate, and splitting afterwards puts siblings on both sides. Augment after splitting, never before.

**Images from the same physical site.** Two cameras on the same line see nearly the same scene; a model tested on the second camera has effectively seen it.

**Near-identical backgrounds.** A conveyor belt with a distinctive stain appears in a thousand images; the model may learn the stain.

The detection method is embarrassingly simple and almost never done: compute a cheap perceptual hash or a small downsampled fingerprint of every image, sort by similarity, and inspect the closest pairs. Twenty minutes of work, and it converts an unknown into a number.

## Augmentation Belongs After the Split

The rule deserves its own paragraph because it is broken so often. Split the originals into training, validation and test. Then augment *only* the training set. Then train. Then evaluate on the unaugmented validation and test images.

If you augment first and split afterwards, the test set contains altered copies of training images, and the score is inflated by exactly the amount the augmentations span. Brightness augmentation, for instance, will make the test set look like training data at every exposure — and the deployed model will then fail on an exposure it has not seen, which is precisely what the test was meant to predict.

## Labels, and How Wrong They Are

Human annotation of images disagrees with itself. Published agreement rates for defect labelling typically sit between 85% and 95% depending on the task and the training of the annotators, and your project is not an exception.

Two habits make this visible rather than fatal.

**Double-label a sample.** Take two hundred images and have a second person label them without seeing the first labels. Report the agreement rate. If it is 88%, then no model can be expected to exceed 88% against the original labels, and a reported accuracy of 99% is a sign of leakage, not excellence.

**Write the labelling rules down.** "A scratch is any linear mark longer than 2 mm that is visible at the specified lighting" is a rule. Without it, one annotator counts a polish mark as a defect and another does not, and the model learns the disagreement.

The practical consequence is that label noise sets a ceiling. Once a dataset's labels disagree with themselves at 10%, effort is better spent on clearer rules and better images than on a bigger network.

## Imbalance Is the Normal Condition

Defects are rare. A dataset with 1.5% positives is typical, and it produces two specific problems.

The model learns to predict the majority class, because that minimises error on the training data. A network that says "good" every time achieves 98.5% accuracy and is worthless.

The metric hides it. Accuracy, as discussed in the previous volume, is dominated by the majority class, and a training log that reports only accuracy will look excellent throughout.

What to do, in order of effectiveness:

Collect more positives. Nothing beats real examples of the thing you must find.

Weight the loss by inverse frequency. A positive example counted fifty times as heavily as a negative one forces attention to the rare class.

Sample the training set deliberately. Balanced batches, with positive examples repeated, work well.

Choose the operating threshold on validation data using costs. This is the step that turns a probability into a decision, and it is separate from training.

| Dataset | Positives | Accuracy if always "good" | Useful metric |
|---|---|---|---|
| 10,000 images | 150 (1.5%) | 98.5% | Recall at fixed precision |
| 10,000 images | 500 (5%) | 95.0% | Precision-recall area |
| 10,000 images | 2,000 (20%) | 80.0% | Either, with care |

## Capture Is Engineering

The most valuable hours in a vision project are spent designing the capture, not the model. A coverage matrix is the tool: list the conditions the system must handle, and ensure the dataset contains examples of each.

For a surface inspection cell, the rows might be supplier, surface finish, lighting condition (daylight through the window, lights on, lights off), part orientation, and camera (if more than one). The columns are images needed per cell, with a minimum of perhaps twenty. Filling the matrix takes a week. Discovering an empty cell in production takes a month and a customer complaint.

The matrix also produces the split. If camera is a row, split by camera. If time of day matters, capture across days and split by day. The structure of the split is a statement about what you believe the model must generalise to, and the matrix is the clearest way to say it.

## Problems

1. A dataset has 30 parts, 60 frames each, and is split 70/30 randomly. How many frames of a given validation part are likely in training? What does that imply for the measured accuracy?
2. You have 500 images from site A and 200 from site B, and the model must work at both. Describe a split and a reporting scheme that would tell you honestly whether it does.
3. A colleague augments 1,000 images into 8,000 by rotating each in 45-degree steps, then splits randomly. Identify the error and predict its effect on the reported score.
4. Two annotators agree on 87% of 200 images. Estimate the best achievable measured accuracy and explain the reasoning in three sentences.
5. A defect occurs in 0.8% of parts. A model achieves 95% recall and 12% precision. At 5,000 parts per day, how many false alarms per day does that produce, and is it operable?
6. A plant asks whether the model will still work after the summer shutdown, when the ambient temperature rises by eight degrees and the incoming parts come from a second supplier. What would you add to the dataset and to the split to answer that question?
