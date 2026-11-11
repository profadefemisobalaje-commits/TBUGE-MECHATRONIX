# Corners, Features, and the Points That Survive

Two photographs of the same printed circuit board, taken a second apart from a camera that has not moved. Between them the board has been nudged by a handling robot, rotated by perhaps two degrees, and lit slightly differently because a shadow moved.

A template matcher compares the two and fails. The template is a rectangle of pixels; rotating the board rotates the pixels inside it; the comparison is now between two arrangements that no longer line up. Everything correlates less, the peak score falls, and the system reports no match.

A feature matcher compares the same two and succeeds, because it does not compare pixels. It finds a few hundred distinctive points, describes each by its local neighbourhood in a way that is stable under rotation and moderate changes of brightness, and then finds the arrangement of descriptors that best explains both images. From that arrangement it computes the rotation, the translation, and the scale.

This is the idea that carries machine vision from "measuring a part that always appears in the same place" to "understanding a scene". It is also the idea that underlies modern three-dimensional reconstruction, panorama stitching, and the alignment step inside many industrial systems.

## Three Kinds of Neighbourhood

Look at a small window of an image and ask how it would change if you slid it by one pixel in each direction.

**Flat region.** Nothing changes. The window has no information about where it is, and no amount of matching will localise it.

**Edge.** Sliding along the edge changes nothing; sliding across it changes a lot. The window is localised in one direction only — the classic aperture problem, where a straight edge tells you it has moved but not how far along itself.

**Corner or texture.** Sliding in any direction changes something. The window is localised in both directions, and that is what makes it usable as a landmark.

The Harris corner detector turns this description into arithmetic. For each pixel, sum three quantities over a small window: the squared horizontal gradient, the squared vertical gradient, and their product.

> Sxx = sum of Ix², Syy = sum of Iy², Sxy = sum of Ix·Iy

Then form a 2 by 2 matrix from those three numbers and compute two values that summarise its shape:

> R = Sxx·Syy − Sxy² − k·(Sxx + Syy)²

with k around 0.04. Large positive R means a corner. Negative R means an edge. Small values mean flat.

Worked, on a hypothetical window: suppose Sxx = 100, Syy = 100 and Sxy = 0. Then

> R = 10,000 − 0 − 0.04 × (200)² = 10,000 − 1,600 = 8,400

A corner, strongly. Now suppose the window lies on a horizontal edge: Sxx = 100, Syy = 0, Sxy = 0.

> R = 0 − 0 − 0.04 × (100)² = −400

Negative: an edge, to be rejected.

The two numbers are not measurements of anything physical. They are a compact way of asking the sliding-window question, and they are worth computing once by hand on a small patch so that the response map stops being a black box.

## Descriptors: Making a Corner Recognisable

A corner is a location. To match corners between images, each needs a description that is stable when the image changes in the ways images change: rotation, scale, brightness, small perspective shifts, noise.

The standard recipe has three parts.

**Orientation.** Compute the dominant gradient direction in the neighbourhood, using a histogram of gradient angles weighted by magnitude. Rotate the description to that direction, so that the same physical corner produces the same descriptor regardless of how the camera was rotated.

**Sampling.** Divide a square region around the point into a grid of sub-regions — typically 4 by 4 — and record, for each, a summary of the gradient directions within it. The result is a vector of numbers, usually 128 of them, which is the descriptor.

**Normalisation.** Scale the vector so its length is one, and clamp the largest components. This makes the descriptor insensitive to overall brightness and contrast changes, which is exactly what a change of lighting produces.

Then matching is a matter of distance. For each descriptor in the first image, find the nearest and second-nearest in the second image, and accept the match only if the nearest is clearly closer. The **ratio test** is the standard guard:

| Nearest distance | Second nearest | Ratio | Decision |
|---|---|---|---|
| 40 | 60 | 0.67 | Accept |
| 40 | 45 | 0.89 | Reject |
| 25 | 90 | 0.28 | Accept, confidently |

A threshold of 0.8 is conventional. The logic is worth stating: a descriptor that is equally close to two different features is probably ambiguous, and a wrong match is more expensive than a missing one.

## Turning Matches into a Transformation

Matches alone are a cloud of correspondences, some of them wrong. The next step fits a geometric model and rejects the matches that do not obey it.

For a flat object viewed from a fixed camera — a board on a table — the appropriate model is a **homography**, an eight-parameter mapping that accounts for rotation, translation, scale, shear and perspective. Four point correspondences determine it exactly.

Because some matches are wrong, the fitting is done by consensus rather than by least squares. **RANSAC** picks four matches at random, computes the transformation they imply, and counts how many of the remaining matches agree with it within a tolerance. It repeats this many times and keeps the transformation with the most agreement.

The arithmetic explains why the repetition is necessary. Suppose 60% of the matches are correct. The chance that a random set of four is entirely correct is 0.6^4 = 0.13, so a single attempt usually fails. After ten attempts the chance of at least one clean set is 1 − (1 − 0.13)^10 ≈ 0.75. After forty attempts it is 1 − 0.87^40 ≈ 0.996. Forty attempts cost almost nothing, which is why RANSAC is set to hundreds rather than tens in practice.

| Inlier fraction | P(clean sample of 4) | Attempts for 99% success |
|---|---|---|
| 0.3 | 0.008 | 570 |
| 0.5 | 0.063 | 71 |
| 0.6 | 0.130 | 34 |
| 0.8 | 0.410 | 9 |

The table is a useful diagnostic in reverse: if a system needs a thousand attempts to find a consistent transformation, the matches are mostly wrong, and the place to look is the descriptor quality or the lighting, not the attempt count.

## Where Features Fail

Feature methods are robust to more than template matching and less than intuition suggests. Four failures recur.

**Repetitive texture.** A grid of identical holes, a woven fabric, a brick wall. Every descriptor looks like every other, the ratio test rejects almost everything, and the survivors are arbitrary. Repair: add a non-repetitive marker, or use a method that exploits structure rather than points.

**Scale change beyond the descriptor's range.** A printed label photographed at twice the distance has features twice as large. Descriptors handle this by being computed at several scales, but the range is finite, and a factor of four exceeds it. Repair: constrain the working distance, or use a scale-invariant pipeline explicitly.

**Motion blur and defocus.** Blur destroys the fine gradients that descriptors depend on. A feature map from a blurred image has few points and poor localisation. Repair: shorten the exposure, or accept fewer points and rely on geometry.

**Reflective and transparent surfaces.** A specular highlight moves with the light, not with the object, so the same physical point produces different descriptors in successive frames. Repair: polarisation, diffuse lighting, or features chosen away from highlights.

Note the shape of these repairs. Not one of them is "use a better matcher". They are all changes to the physical situation or to the assumptions, which is the recurring theme of this book.

## What Features Are Good For

The classical uses remain valuable and are often cheaper than a network.

**Alignment before measurement.** Locate the part by its features, then measure in a coordinate frame attached to the part rather than to the camera. This single trick removes most of the fixture's tolerance from the measurement budget.

**Stitching.** Overlapping images of a large surface, aligned by shared features, produce a mosaic wider than any single field of view.

**Three-dimensional reconstruction.** Correspondences across two views, plus calibration, give depth by triangulation — the subject of Chapter Seven.

**Verification of change.** Features present in a reference image and absent in a test image, in the same geometric arrangement, are evidence of a missing component.

In each case, the value lies in the *arrangement* rather than in any single point. A hundred points that all agree on a rigid transformation are far stronger evidence than any one of them, and this is a statistical argument that survives long after the specific detector has been superseded.

## Things to Try

Photograph a page of text from directly above, then from an angle of about thirty degrees. Run a corner detector on both — most image libraries have one built in — and compare the number and distribution of points. Then rectify the angled image with a homography and check whether the text becomes readable. That sequence, in fifteen minutes, is the whole classical pipeline.

Next, photograph a tiled floor or a brick wall and run the same detector. Look at how the points distribute: they will cluster at the same relative position in every tile, which is exactly the repetition problem described above. Understanding why the matcher fails there is more instructive than any amount of reading about robustness.
