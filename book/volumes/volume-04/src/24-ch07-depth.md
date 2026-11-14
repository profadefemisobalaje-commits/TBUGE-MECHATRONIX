# Depth: Two Eyes, One Camera, and the Arithmetic of Distance

A robot arm must pick a part from a bin. The part is a cast bracket, dark grey, lying at an angle among twenty others. The camera knows where the bracket is in the image — a bounding box, a centroid, an orientation — and none of that tells the gripper how far away it is.

The naive answer is to assume a height. The bin has a known depth of 200 millimetres, the parts are 40 millimetres thick, and the top one is probably somewhere in between. This works until it does not, which is on the day the bin is half empty and the top part is 90 millimetres lower than usual. The gripper closes on air, or worse, drives into the part and marks it.

Depth is a separate measurement, and it costs a second camera, a projector, or a time-of-flight sensor. This chapter is the arithmetic that says which one, and how accurate it will be.

## Stereo: The Geometry of Disparity

Two cameras, side by side, looking at the same scene. A point in the world projects to a position in the left image and a different position in the right, and the difference between those positions — the **disparity** — encodes distance.

For two cameras with parallel axes, separated by a baseline B, each with focal length f, the depth is

> Z = f · B / d

where d is the disparity in pixels.

Worked. Focal length 8 mm, baseline 120 mm, disparity 4 pixels:

> Z = 8 × 120 / 4 = 240 mm

Now the useful question: how much does a one-pixel error in disparity cost?

> depth error per pixel = Z² / (f · B)

At Z = 240 mm: 57,600 / 960 = 60 mm per pixel. That is enormous — the sensor can localise the point to within 6 cm, which is useless for gripping.

The formula explains the whole behaviour of stereo. The error grows with the square of the distance, because disparity itself shrinks with distance. At one metre, with the same rig, disparity is under one pixel and depth resolution is over a metre per pixel. At 240 mm the system works only if disparity is measured to a fraction of a pixel, which is possible with good texture and careful matching, and impossible on a blank grey casting.

| Baseline | Distance | Disparity | Depth error per pixel |
|---|---|---|---|
| 120 mm | 240 mm | 4.00 px | 60 mm |
| 120 mm | 1,000 mm | 0.96 px | 1,042 mm |
| 300 mm | 1,000 mm | 2.40 px | 417 mm |
| 300 mm | 500 mm | 4.80 px | 104 mm |

Reading the table: to work at a metre you need a baseline of hundreds of millimetres, which makes the rig large and the matching harder, because the two views see genuinely different surfaces. This is the fundamental trade of stereo, and no amount of processing removes it.

Stereo also needs texture. The matching is done by comparing patches, and a patch with no pattern matches everywhere equally well. Projecting a random dot pattern onto the scene — **structured light** — supplies the texture artificially and is one of the great practical tricks of the field.

## Structured Light and Laser Triangulation

If you project a known pattern and observe how it deforms, you can compute depth from a single camera. The projection supplies the second "viewpoint", and the pattern supplies the texture.

Two families dominate industry.

**Fringe projection.** A sequence of sinusoidal patterns is projected while the camera captures each. The phase of the observed sinusoid gives a very precise measurement of position along the projector's axis, and unwrapping across frequencies extends the range. Fringe systems achieve tens of micrometres over fields of a few hundred millimetres, and they are the standard for dimensional inspection of small parts. They are also slow — several images per measurement — and they dislike moving objects.

**Laser line triangulation.** A laser projects a line onto the surface; a camera offset by an angle sees the line displaced by an amount proportional to height. Scan the line across the part and you build a profile. The geometry is the same triangle as stereo with one vertex replaced by a projector, and the resolution along the line is set by the camera while the resolution across it is set by the scan step.

| Method | Accuracy | Speed | Weakness |
|---|---|---|---|
| Stereo | 1–5% of range | Fast | Needs texture; fails on blank surfaces |
| Fringe projection | 0.01–0.1 mm | Slow (0.1–1 s) | Ambient light; shiny parts |
| Laser line | 0.05–0.2 mm | Medium | Speckle; occlusion in deep features |
| Time of flight | 5–20 mm | Fast | Multipath, reflectivity, edges |

## Time of Flight, and Why It Is Not a Metrology Tool

A time-of-flight camera measures the phase delay of modulated light, and converts it to distance. It is cheap, it produces a full depth image at video rate, and it is excellent for coarse tasks: is there a person in the cell, how full is the bin, is the pallet present.

It is not a metrology tool. Three reasons.

The illumination is modulated at tens of megahertz, and the phase measurement has a resolution of a few millimetres at best. Reflections from nearby surfaces arrive twice — **multipath** — and bias the result towards the nearer surface. And shiny or dark materials return too little light, so the sensor reports depth where there is none and misses depth where there is.

For safety and presence sensing, none of that matters. For measuring a 0.1 mm gap, it is disqualifying.

## Calibration: Turning Pixels into Millimetres

Every method above depends on knowing the camera's geometry precisely. **Calibration** estimates two sets of numbers.

**Intrinsics** describe the camera itself: focal length in pixels, the position of the optical axis, and the lens distortion coefficients. They do not change when the camera is moved.

**Extrinsics** describe where the camera sits relative to the world, or to the other camera: a rotation and a translation. They change whenever anything is bumped.

The standard procedure is a printed chequered board of known square size, photographed in a dozen or more orientations. A solver finds the parameters that best explain all the views, and reports a **reprojection error**: the average distance, in pixels, between where a corner should appear and where it does.

| Reprojection error | Meaning |
|---|---|
| Under 0.2 px | Excellent; suitable for measurement |
| 0.2–0.5 px | Normal; fine for most tasks |
| Over 1 px | Something is wrong: motion blur, bad board, wrong square size |

Convert the error into physical units before deciding it is good enough. At a sampling interval of 0.28 mm per pixel, 0.3 pixels is 0.08 mm — acceptable for a ±0.2 mm task and not for a ±0.05 mm one.

Two practical points that are learned the hard way. Calibrate at the working distance and with the aperture you will use in production, because focus changes the effective focal length slightly. And re-check calibration after any mechanical work on the rig; a bumped mount is the most common cause of a system that "suddenly" measures 0.3 mm too wide.

## What Depth Does Not Solve

Having depth does not mean having understanding. A point cloud of a bin of parts is a surface, and finding the graspable part in it is a separate problem with its own literature.

It also does not solve occlusion. A camera, or a projector, sees one side. Deep recesses, undercuts and the far side of a part are invisible, and no algorithm can measure what was never illuminated. When a drawing specifies a feature that cannot be seen from any single direction, the answer is a second viewpoint or a different sensor, not better software.

And it does not solve the material. Black anodised aluminium absorbs most of the light; polished steel reflects it away from the sensor; clear plastic transmits it. All three are hard for every method in this chapter, and all three are usually solved by a surface treatment or a different physical principle — a touch probe, an air gauge, or an eddy-current sensor.

## Problems

1. A stereo rig has f = 6 mm, B = 200 mm, and resolves disparity to 0.5 pixels. What is the depth error at 300 mm? At 800 mm?
2. You need 2 mm depth accuracy at 500 mm. What baseline do you need with a 6 mm focal length and 0.25-pixel matching? Is that rig mechanically sensible?
3. A calibration reports 0.8 pixels of reprojection error at a sampling interval of 0.1 mm per pixel. What measurement uncertainty does that imply, and what would you check first?
4. Explain, in plain language, why stereo depth gets worse with distance while laser triangulation does not degrade as sharply.
5. A time-of-flight sensor reports a person at 1.2 m and a colleague standing 0.8 m away behind a glass panel. What has probably happened?
6. A bin-picking cell must find the top surface of parts between 300 and 500 mm from the camera, to ±3 mm, in under 100 ms. Which method from the table would you choose, and what would you need to add to make it work on grey castings?
