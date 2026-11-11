# Detection and Measurement

A defect-detection system flagged the same scratch twice. The operator marked both flags as correct — it was a real scratch — and the part was scrapped. The next day the same thing happened, and the next. When the engineer looked at the log, she found two boxes drawn on one scratch, nine millimetres apart, each with a confidence above 0.9.

The model was not confused. It was a *detector*, trained to put a box around each defect, and it had learned that a long scratch sometimes appears as two shorter segments — because in its training data, some had been labelled that way by annotators who stopped at a change in direction.

Two lessons follow, and this chapter is organised around them. The first is that a detector's output is a set of boxes, and sets require their own arithmetic — overlaps, thresholds, counts. The second is that a detection system which must also *measure* is doing two jobs, and the measurement half needs its own capability study.

## Boxes and the IoU

A detection is a rectangle with a class and a confidence: position, size, label, score. To say whether a predicted box is correct, the standard test is **intersection over union**.

> IoU = area of overlap / area of union

Two examples, in pixels.

Box A runs from (10,10) to (50,50), area 40 × 40 = 1,600. Box B runs from (30,30) to (70,70), also 1,600. They overlap from (30,30) to (50,50): 20 × 20 = 400. The union is 1,600 + 1,600 − 400 = 2,800.

> IoU = 400 / 2,800 = 0.14

Two boxes that a person would call the same defect, scoring 0.14, because one is displaced by half its width.

Now shift them closer. A' is (10,10) to (60,60), area 2,500. B' is (20,20) to (70,70), area 2,500. Overlap is (20,20) to (60,60): 1,600. Union is 2,500 + 2,500 − 1,600 = 3,400.

> IoU = 1,600 / 3,400 = 0.47

A conventional match threshold is 0.5, and these two — visibly the same object — fall just short of it. This is why detector evaluation is fussy: the metric is dominated by how tightly the box fits, not by whether the object was found.

For scratches and other elongated objects, IoU behaves even worse, because a small displacement along the long axis barely changes the overlap while a small displacement across it changes everything. The practical answer is to use a metric matched to the shape — distance between centroids, or overlap of a dilated mask — and to state which one you used.

## Removing Duplicates

The duplicate in the opening story is the normal output of a detector, not a bug. Sliding-window detectors and their modern descendants produce many overlapping candidates for one object, so a **non-maximum suppression** step runs afterwards.

The procedure: sort candidates by score; take the highest; delete every candidate whose IoU with it exceeds a threshold; repeat.

With a suppression threshold of 0.5, the pair scoring 0.47 above both survive — the duplicate remains. Lower the threshold to 0.3 and one is removed, but genuine pairs of nearby defects may also be merged. With elongated defects the right threshold is often 0.1, and the right IoU is not IoU at all but centroid distance.

| Suppression threshold | Duplicates removed | Risk |
|---|---|---|
| 0.7 | Few | Two boxes on one defect |
| 0.5 | Most | Occasional duplicates |
| 0.3 | Almost all | Nearby defects merged |
| 0.1 | All | Distinct defects lost |

The choice is a business decision: does a duplicate cost more than a merge? On a scrapping line, a duplicate costs a second look; a merge can hide a second defect. That asymmetry should set the threshold, and it should be written down where the next engineer can find it.

## Average Precision, Worked

Detection quality is summarised by precision-recall curves computed per class, then averaged. The arithmetic is short enough to do by hand.

Five detections, two ground-truth defects, sorted by confidence:

| Rank | Score | Correct? | Precision | Recall |
|---|---|---|---|---|
| 1 | 0.95 | yes | 1.000 | 0.50 |
| 2 | 0.88 | no | 0.500 | 0.50 |
| 3 | 0.80 | yes | 0.667 | 1.00 |
| 4 | 0.72 | no | 0.500 | 1.00 |
| 5 | 0.60 | no | 0.400 | 1.00 |

Precision is the running fraction of correct detections; recall is the fraction of the two real defects found so far.

The **average precision** is the area under this curve, computed as a sum of rectangles: each time recall increases, the increase is multiplied by the precision at that point and added.

> AP = 1.000 × 0.50 + 0.667 × 0.50 = 0.500 + 0.333 = 0.833

A perfect detector scores 1.0. A detector that finds one defect and then emits rubbish scores far less, because the precision collapses before recall completes.

Two cautions. AP is an average over thresholds and says nothing about the operating point you will actually run. And a mean over classes (mAP) can flatter a system that is excellent on a common class and useless on a rare one, since each class contributes equally regardless of how many examples it has. Report per-class numbers for the defects that matter, not only the mean.

## Detecting, Then Measuring

A detector answers "is there a defect, and roughly where". A measurement answers "how big is it". Systems that need both should be built in two stages, because the requirements are different.

The first stage finds candidates. It should be tuned generously — a low threshold, accepting false positives — because a missed candidate is unrecoverable, while a false candidate can be rejected by the second stage.

The second stage measures each candidate on the original image, using the tools of Part Two: subpixel edge fitting, calibrated scale, and a stated repeatability.

Calibration converts pixels to millimetres; without it, a length in pixels is a length on the sensor, not on the part. And a stated repeatability is what makes the measurement arguable. "The system reports 6.2 mm" is an assertion. "The system reports 6.2 mm, with a repeatability of ±0.03 mm over thirty repeat images" is an engineering claim.

## Capability: Is the Measurement Good Enough?

A measurement is only useful if its uncertainty is small compared with the tolerance it must police. The standard discipline, borrowed from manufacturing metrology, is a **gauge study**: measure the same parts repeatedly, with more than one operator or setup, and decompose the variation.

A worked version. Ten parts, three operators, three trials each, tolerance ±0.25 mm.

| Source | Standard deviation |
|---|---|
| Repeatability (same operator, same part) | 0.012 mm |
| Reproducibility (between operators) | 0.008 mm |
| Combined | √(0.012² + 0.008²) = 0.0144 mm |

The conventional index is six times the combined deviation divided by the tolerance width:

> %GRR = 6 × 0.0144 / 0.50 = 17%

Under 10% is excellent, 10–30% is acceptable depending on the consequence, and over 30% means the measurement cannot police the tolerance. A vision system at 17% is a usable gauge. The same system with 0.03 mm repeatability would sit at 36%, and no algorithm change would rescue it — only more light, a better lens, or a larger scale.

This is the most useful number a vision engineer can produce, and it is produced by taking pictures of the same thing many times.

## Things to Try

Photograph a coin on a plain background. Draw a box around it by hand, then draw a deliberately sloppy box, and compute the IoU of the two. Then compute the IoU of the sloppy box against a box drawn around a second, slightly different coin. The numbers will show how quickly IoU falls with box quality, and why a threshold of 0.5 is a strong demand.

Then take thirty photographs of the same coin without moving it, measure its diameter in each, and compute the standard deviation. That number, converted to millimetres, is your repeatability — and its relationship to the tolerance you would need is the whole of capability analysis.
