# Neighbours, and the Trouble With Many Dimensions

The simplest classifier in the world stores every example it has ever seen. When a new case arrives, it finds the most similar stored cases and copies their answer. There is no training, no parameters, no optimisation. It is a filing cabinet with a search function, and on some problems it is startlingly hard to beat.

The method is called **k-nearest neighbours**, or kNN, and it is worth understanding for two reasons. It shows what learning looks like when the model has no opinion at all, and its failure in high dimensions explains why so much of modern machine learning looks the way it does.

## Distance Is a Choice You Make

"Most similar" is doing a lot of work in that description, and it is decided by a distance measure.

The usual choice is straight-line distance: for two examples with features x and y, square the differences in each feature, add them, and take the square root. With two features, it is Pythagoras.

The choice of measure is not neutral. If one feature is measured in millimetres and another in kilometres, the first will dominate every comparison. So features are usually **scaled** first: subtract the mean and divide by the spread, so that each feature contributes on the same footing.

Take two pumps. Pump A: vibration 2.0 mm/s, temperature 48 °C. Pump B: vibration 3.0 mm/s, temperature 49 °C. Pump C: vibration 2.1 mm/s, temperature 60 °C.

Without scaling, the raw squared distances are 1 + 1 = 2 to B, and 0.01 + 144 = 144 to C. B is nearest, which matches intuition. Now suppose temperature were recorded in tenths of a degree, so that C is 120 units away rather than 12. The distance to C becomes 0.01 + 14,400, and the distance to B becomes 1 + 100. B is still nearest, but the temperature now dominates so completely that vibration has stopped mattering. A pump with wildly different vibration but a similar temperature would be judged close.

Scaling removes that artefact. After standardisation, each feature's differences are measured in units of its own spread, and the comparison becomes about the data rather than about the choice of sensor.

## Choosing k

With k equal to one, the classifier copies the single nearest example. That is maximally flexible and maximally fragile: a single mislabelled point creates a small island of wrong answers around itself.

With large k, the classifier averages over a wide neighbourhood and eventually predicts the majority class everywhere. That is stable and useless.

The useful range is in between, and the choice is the familiar trade. A small k gives a model with low bias and high variance: it can represent complicated boundaries and it changes a lot when the data changes. A large k gives high bias and low variance: smooth, stable and unable to capture detail.

| k | Boundary | Behaviour | Typical problem |
|---|---|---|---|
| 1 | Very jagged | Memorises every point | Fooled by label noise |
| 3–5 | Locally detailed | Good for clean data | Sensitive near class overlap |
| 15–30 | Smooth | Stable | Blurs genuine structure |
| Very large | Nearly flat | Predicts the majority | Useless |

A rough starting point is the square root of the number of examples, so 10 for a hundred rows and 100 for ten thousand, but it is only a starting point. Ties matter too: with k even and two classes, a tie is possible, and the tie-break rule must be specified rather than left to the library.

## The Curse of Dimensionality

Here is the fact that turned kNN from a curiosity into a cautionary tale.

In one dimension, a line segment's interior is most of its length; only the two ends are near the boundary. In two dimensions, a square's interior is still most of its area. But as dimensions rise, almost all of the volume of a shape ends up near its surface.

Take a cube of side 1 and shrink it by 10% on every side, so the inner cube has side 0.9. The inner cube's volume fraction is 0.9 to the power of the number of dimensions.

- In 2 dimensions, 0.81: about 19% of the volume is in the outer shell.
- In 10 dimensions, 0.35: 65% of the volume is in the shell.
- In 50 dimensions, 0.005: 99.5% of the volume is in the shell.

So in high dimensions, almost every point is an outlier, and "nearby" points are not near in any useful sense. Distances between random points concentrate: the nearest neighbour and the farthest neighbour become almost equally far away. The ratio of the two distances shrinks towards one as dimensions rise, which means the notion of a local neighbourhood dissolves.

The practical consequence is sample size. To cover a space evenly, the number of examples needed grows exponentially with the number of dimensions. Ten examples per axis in two dimensions is a hundred; in ten dimensions it is ten billion.

This is why feature selection and dimensionality reduction are not optional refinements. They are how you bring the data back into a range where local methods work, and it is why so much of modern practice is about learning a good low-dimensional representation before classifying.

## Where Neighbours Win

For all that, kNN is not a museum piece. It is excellent in three situations.

**Recommendation.** "Customers who bought this also bought" is, underneath, a nearest-neighbour search over sparse vectors of purchases. The distances are strange and the data is enormous, but the principle is the same.

**Imputation.** To fill a missing value in a row, find the most similar complete rows and average their values. It respects local structure that a global mean destroys.

**Sanity checks.** A kNN model is a good first thing to run on a new tabular dataset, because if a flexible local method cannot beat a simple linear model, the data is probably not rich enough to justify anything complicated.

Its costs are worth naming: prediction requires comparing the new point with every stored point, so it is slow on large data, and it requires keeping the whole training set in memory. Modern libraries use trees and approximate search to mitigate this, but the fundamental trade remains — kNN buys simplicity with storage and search time.

## Problems

1. Standardise three features by hand: values 10, 12, 14 (mean 12, spread 2); 100, 110, 120 (mean 110, spread 10); and 1, 2, 3 (mean 2, spread 1). Show the standardised values and explain why the original scales are incomparable.

2. With five examples labelled 0, 0, 1, 1, 1, compute the kNN prediction for a new point equidistant from the two nearest examples, for k = 1, 3 and 5. What does the exercise demonstrate?

3. Compute 0.9 to the power of 5, 20 and 100. Interpret each as the fraction of a high-dimensional cube's volume that lies in its outer shell, and say what it means for the idea of a local neighbourhood.

4. A dataset has 200 rows and 60 features. Explain why kNN is likely to perform poorly, and name two things you would do before using it.

5. Describe a recommendation problem you use. What would "distance" mean in it, and which features would you have to scale before it made sense?
