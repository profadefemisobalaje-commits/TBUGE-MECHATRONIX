# Edges, Gradients and the Honest Line

The task was to measure the width of a weld seam to a tenth of a millimetre, on a part that had already been welded. The camera was adequate, the light was a bar above the fixture, and the software was a commercial package with an edge tool that let the operator drag a box across the seam and read a width.

It worked in the afternoon and failed in the morning, and the difference between afternoon and morning was a window.

By three o'clock the sun came round to the west side of the building and added a soft gradient of light across the fixture. The seam's left edge darkened; the right edge brightened. The edge tool found both edges, exactly as designed, and reported a width that was 0.4 millimetres too large. The tool was not confused. It was an honest detector reporting a dishonest signal.

Edges are the first structure most people extract from an image, and the most misunderstood. An edge is not a property of an object. It is a property of the light that happened to fall on the object when the shutter opened.

## What an Edge Is

An edge is a place where brightness changes quickly. In a continuous world, that change is a slope; in a digital image, it is a difference between neighbouring pixels.

The simplest estimate of the horizontal slope at a pixel is the difference between its right and left neighbours:

> Ix = I(x+1) − I(x−1)

This "central difference" is cheap and surprisingly good, because it averages over two pixels and so cancels some noise. Its vertical twin gives Iy. Together they form the **gradient**, a vector with two components.

A 3 by 3 version weights the near neighbours more heavily than the diagonal ones, and this weighted version is the Sobel operator:

    -1    0   +1
    -2    0   +2
    -1    0   +1

## A Worked Response

Take the patch from the previous chapter, this time with a clean vertical step: dark on the left, bright on the right.

    30   30  120
    30   30  120
    30   30  120

Apply the horizontal Sobel kernel to the centre pixel:

    (-1)(30) + (0)(30) + (+1)(120) =   90
    (-2)(30) + (0)(30) + (+2)(120) =  180
    (-1)(30) + (0)(30) + (+1)(120) =   90
    total Gx = 360

Now the vertical kernel, which is the horizontal one turned on its side:

    -1   -2   -1
     0    0    0
    +1   +2   +1

    (-1)(30) + (-2)(30) + (-1)(120) = -210
    ( 0)(30) + ( 0)(30) + ( 0)(120) =    0
    (+1)(30) + (+2)(30) + (+1)(120) =  210
    total Gy = 0

The gradient magnitude is the hypotenuse: √(360² + 0²) = 360. Its direction is horizontal, pointing right — across the edge, which is always the case, because that is the direction in which brightness changes fastest.

The raw number depends on the kernel's weights, so it is customary to divide by the sum of the positive weights to bring it back into image units. For Sobel that sum is 4 in each column, giving 360/8 = 45: the step was 90 grey levels, and the normalised response reports half of it. The factor of two is an artefact of the weighting, not a physical law, which is why thresholds should be set on your own images and never copied from a textbook.

## From Gradient to Edge Map

The gradient magnitude field is an image in its own right: bright where structure exists, dark where the picture is flat. Turning it into a set of lines requires two decisions.

**Threshold.** Above the threshold, call it an edge; below, discard. Choose the threshold by looking at a histogram of gradient magnitudes on a real image, and pick a value in the valley between the noise and the structure. If there is no valley, the image does not support the task.

**Thinning.** A step edge produces a ridge several pixels wide, because both the rising and falling filter responses exceed the threshold. **Non-maximum suppression** keeps only the local maximum along the gradient direction: for each pixel, compare its magnitude with the two neighbours on either side across the edge, and delete it if it is not the largest.

The Canny detector combines these with one more idea: **hysteresis**. Two thresholds are used, a high one that starts an edge and a low one that continues it. A strong edge is kept only if it connects to another strong edge. The effect is to suppress isolated noise responses while keeping faint continuations of genuine boundaries — and the effect is dramatic on textured surfaces, where a single threshold either drowns in texture or loses the object.

| Step | Question answered | Typical failure if skipped |
|---|---|---|
| Smooth | Is the pixel noise below the step size? | Thousands of spurious edges |
| Gradient | Where does brightness change? | Nothing found |
| Magnitude threshold | Which changes are real? | Noise retained or structure lost |
| Non-maximum suppression | Where exactly is the edge? | Two-pixel-wide bands |
| Hysteresis | Is this edge connected to a real one? | Isolated specks |

## Where Is the Edge, Exactly?

For measurement, the interesting question is not whether an edge exists but where its centre lies, to a fraction of a pixel.

A blurred step has a transition width of roughly four times the blur radius. Fit a curve to the gradient profile — a straight line through the two steepest points is usually enough — and the crossing of its midpoint gives a position accurate to about a tenth of a pixel on a clean, well-lit, straight edge.

That "clean, well-lit, straight" is doing heavy work. On a curved edge the fit must account for curvature; on a low-contrast edge the noise dominates; and on a surface with visible microstructure the profile is not a step at all but a stutter.

The measurement to report alongside the width is therefore not just a number but a **repeatability**: take fifty images of the same part without moving it, compute the width each time, and report the standard deviation. If that number is 0.15 mm, then a specification of ±0.1 mm is unmeetable and the argument is over before it starts. This one habit — measuring the measurement — prevents more bad projects than any algorithm choice.

## The Four Ways Edges Lie

**Lighting gradients.** A smooth change in illumination across the field produces a gradient that is not on the object at all. It shifts every edge it touches in the same direction, so widths stay roughly right while positions drift. Repair: diffuse the light, or calibrate it with a blank reference image and divide it out.

**Glare and specular reflection.** A shiny surface reflects the light source rather than the surface. Edges vanish inside the reflection, and new edges appear at its boundary. Repair: change the geometry — use a dome light or a polariser — rather than the threshold.

**Texture.** A brushed or cast surface has thousands of real micro-edges. A low threshold finds them all; a high one loses the object. Repair: blur along the edge direction before differentiating, which averages the texture while preserving the boundary.

**Curvature and perspective.** An edge that is straight in three dimensions may be curved by the lens, and a width measured in pixels is not a width in millimetres unless the scale is known at that location. Repair: calibrate, and measure in millimetres rather than pixels.

None of these is fixed by a better detector. All four are fixed by the rig, which is why Part Four exists.

## Problems

1. Compute Gx and Gy for the centre of this patch with the Sobel kernels: rows 40, 40, 160 / 40, 40, 160 / 40, 40, 160. What is the magnitude, and in which direction does the gradient point?
2. The same patch is imaged again with a gain of 1.5 applied. What happens to the gradient magnitude, and what does that tell you about using a fixed threshold across two cameras?
3. Explain why non-maximum suppression compares along the gradient direction rather than along the row and column.
4. A blurred edge has a transition 6 pixels wide. Estimate the blur radius, and the smallest feature width that will still produce a distinct pair of edges.
5. An edge tool reports a width of 12.4 mm with a repeatability of 0.08 mm over fifty static images. The tolerance is ±0.1 mm. Is the tool adequate? What would you check before answering?
6. Design a lighting change that would remove the gradient in the opening story without moving the camera or the part.
