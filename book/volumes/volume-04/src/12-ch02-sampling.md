# Pixels, Coordinates and the Cost of Sampling

A hairline crack, 0.06 millimetres wide, running across a cast housing. Under a microscope it is obvious. On the inspection image it is not there at all.

The camera was a 5-megapixel unit with a 12-millimetre lens at a working distance of 600 millimetres, and the housing filled the frame. The engineer measured the field of view with a rule: 660 millimetres across. He divided by the number of pixels across the sensor, 2,592, and wrote the answer on the whiteboard: 0.25 millimetres per pixel.

A crack two-tenths of a pixel wide does not make a dark line in an image. It makes each affected pixel very slightly darker than its neighbours — by an amount that depends on where the crack happens to fall inside the pixel's area. Move the part by a tenth of a millimetre and the effect changes. The crack is not hidden by the algorithm; it was never sampled.

This chapter is about that arithmetic, because it is the single calculation that decides whether a vision project is possible.

## Resolution Is a Physical Quantity

Camera datasheets quote megapixels, which is a number about the sensor and says nothing about the task. The number that matters is the **spatial sampling interval**: millimetres of the real world per pixel, at the working distance you intend to use.

> mm per pixel = (field of view width in mm) / (pixels across the sensor)

Three levers change it, and they are not equivalent in cost.

Move closer. Field of view shrinks in proportion to distance, so halving the distance halves the sampling interval and quadruples the effective resolution per unit area. This is the cheapest lever and the one most often blocked by the machine.

Use a longer lens. The same effect as moving closer, achieved without moving the camera: a lens of twice the focal length halves the field of view. It costs money, reduces depth of field, and requires a rigid mount.

Buy more pixels. Doubling the linear pixel count halves the interval without changing the optics, but it also halves the light per pixel and increases readout time, so it is rarely free in practice.

| Configuration | Field of view at 600 mm | Pixels across | mm per pixel |
|---|---|---|---|
| 12 mm lens, 1/1.8 in sensor | 360 mm | 1,280 | 0.28 |
| 50 mm lens, 1.1 in sensor | 158 mm | 4,112 | 0.039 |
| 12 mm lens, 1.1 in sensor | 660 mm | 2,592 | 0.25 |

The middle row is what the crack needed; the bottom row is what the project had.

## How Many Pixels Does a Feature Need?

The sampling theorem says you need more than two samples per cycle to reconstruct a pattern, and that is the floor for signals designed to be reconstructed. Vision is harder than that, because a defect has to be *detected* against noise, not merely represented.

The working rules used in practice:

- Three pixels across the smallest feature you must detect, as an absolute minimum.
- Five pixels across it for reliable measurement of its size.
- Ten pixels across it if you intend to measure position to a tenth of the feature's width.

These are not laws but they are remarkably durable, and they are cheap to apply. A 0.2 mm burr at 0.28 mm per pixel is 0.7 pixels — hopeless. The same burr at 0.04 mm per pixel is five pixels — comfortable. The project's fate was decided by a division, before anyone chose a network.

## Aliasing: The Failure That Looks Like a Different Problem

When a pattern finer than twice the sampling interval is imaged, it does not disappear. It reappears as a coarser pattern that is not in the object at all. This is aliasing, and in industrial images it takes three familiar forms.

**Moiré on woven or perforated material.** A mesh screen with 0.4 mm openings sampled at 0.28 mm per pixel produces broad wavy bands. An inspector looking at the image sees a defect that is an artefact of sampling; a real defect may be invisible underneath it.

**Broken edges on fine pitches.** A connector with 0.3 mm contacts sampled at 0.25 mm per pixel produces contacts of wildly different apparent widths, some darker, some lighter, none corresponding to the physical part.

**Crawling patterns in video.** The same mesh, viewed live, shimmers as the part moves — a signature that is almost diagnostic of undersampling.

The cure is optical or mechanical, not digital: fewer pixels per feature means blur first. Slightly defocusing the lens, or fitting a diffuser, removes the high frequencies before they are sampled, and a blurred honest image is far better than a sharp aliased one. Software anti-aliasing after sampling cannot undo the damage, because the information is already gone.

## Coordinates, and the Half-Pixel That Costs a Shift

Every image library puts the origin in a different place, and every one of them has been the cause of a rejected batch.

The convention that makes the arithmetic consistent: a pixel is an *area*, not a point. Pixel (0, 0) covers the square from 0.0 to 1.0 in both axes, and its centre is at (0.5, 0.5). A blob whose centroid computes to (100.0, 50.0) is therefore at the corner shared by four pixels, and a blob at (100.5, 50.5) is at the centre of one.

Why it matters, in millimetres: at 0.28 mm per pixel, a half-pixel disagreement between two pieces of code is a 0.14 mm disagreement in reported position. If a robot is asked to place a part with a ±0.1 mm tolerance, the convention alone can consume the budget.

Three habits prevent the class of error:

Write the convention down once, in the project notes, and refer to it. "Centroid coordinates are pixel centres; origin at the centre of the top-left pixel" is a sentence worth its ink.

Test with a synthetic image. Draw a disc whose centre you know exactly, run the centroid routine, and check it returns that centre to within 0.01 pixels. This takes twenty minutes and catches the error before it reaches a machine.

Never mix libraries silently. If one routine returns corners and another returns centres, convert at the boundary, in one function, with a comment.

## Resizing Is Not Free

Downsampling an image to speed up processing is one of the most common optimisations, and one of the most common ways to delete the defect.

A 1,280 by 1,024 image reduced to 320 by 256 has one output pixel for every sixteen input pixels. Each output is some average of its block. A one-pixel-wide scratch covering 2% of a block contributes 2% of the block's brightness change: in an 8-bit image where the scratch was 40 levels darker than its surroundings, the downsampled difference is 0.8 levels, which is below the rounding step.

Upsampling has the opposite problem: it invents smooth values between measurements and makes the image look more precise than it is. Interpolation is a display convenience, not an increase in information.

| Operation | Cost | Information |
|---|---|---|
| Nearest-neighbour downscale | Cheapest | Discards, badly |
| Area-average downscale | Cheap | Discards, fairly |
| Bilinear upscale | Cheap | Invents, smoothly |
| No resize, larger sensor | Expensive | Gains |

If the pipeline needs to be faster, crop before you shrink. A region of interest of 400 by 300 pixels contains 120,000 pixels instead of 1.31 million — eleven times less work, and every remaining pixel is a real measurement.

## Bandwidth Is Part of the Design

Numbers make the constraint concrete. A 1,280 by 1,024 8-bit image is 1.31 megabytes. At thirty frames per second that is 39 megabytes per second, which is comfortable for a Gigabit Ethernet link and awkward for USB 2. A 12-bit image is 1.97 megabytes, or 59 megabytes per second, which requires a faster link or a smaller frame.

Compression is a temptation. Lossy compression such as JPEG achieves ten-to-one reductions by discarding high-frequency detail — exactly the detail that a scratch or an edge consists of, and with visible blocking artefacts near high-contrast boundaries. For a photograph shown to a human it is excellent. For a measurement, use a lossless format or no compression at all, and if storage is the constraint, store fewer frames of better quality.

## Things to Try

Take a ruler, a camera and a textured surface — a coin, a printed page, a piece of woven cloth. Photograph it at your normal working distance with an object of known size in the frame. Compute millimetres per pixel yourself, from the image, not from the datasheet. Then measure something small in the image and compare with a caliper. The gap between the two numbers is the beginning of metrology.

Next, photograph the same cloth from far enough away that the weave is finer than a pixel, and look for moiré. Then defocus slightly and photograph it again. Compare. That pair of images explains more about sampling than any chapter can.

Finally, list three features in your own work or study that must be detected, and compute the sampling interval each one needs at three, five and ten pixels across. Compare against the camera you have. The answer is sometimes "this needs a different camera", and it is better to know that in week one.

## Problems

1. A sensor has 2,448 by 2,048 pixels and a 8.4 mm by 7.0 mm active area. With a 25 mm lens at 400 mm working distance, what is the field of view, and what is the sampling interval?
2. A defect is 0.15 mm wide. What sampling interval do you need for five pixels across it? What field of view does that imply for a 2,448-pixel sensor?
3. An image is downsampled from 2,048 by 2,048 to 512 by 512, then a 3 by 3 edge filter is applied. Estimate the smallest feature the filter can still respond to, in original pixels.
4. You are told the position of a part must be reported to ±0.05 mm, and the sampling interval is 0.2 mm. Is sub-pixel estimation needed? What accuracy would you expect from a simple centroid?
5. A conveyor runs at 0.8 m/s and the camera exposes for 3 ms. How far does the part move during the exposure, in millimetres and in pixels at 0.2 mm per pixel? What exposure time would keep the smear under one pixel?
6. Explain to a colleague, in plain language and without formulas, why blurring an image can make a fine pattern easier to interpret.
