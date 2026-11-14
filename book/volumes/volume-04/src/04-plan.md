# How This Volume Is Arranged

The book has four parts, and they correspond to four questions a vision engineer asks in order.

**Part One — The Image as Evidence** is about the measurement. A camera converts light into integers, at a particular resolution, over a particular field of view, with a particular amount of noise. Those decisions are made before any algorithm runs, and they cap everything that follows. Three chapters: how light becomes a number, how sampling fixes what can be resolved, and how a kernel transforms a neighbourhood into a single value.

**Part Two — Structure Without Learning** is the classical toolkit, and it is still the right first attempt on most industrial problems. Edges, corners, thresholds, regions, depth. Each idea is worked on a nine-number patch so that the arithmetic is visible, and each is followed by the conditions under which it collapses: glare, occlusion, repetitive texture, a change of scale.

**Part Three — Learning to See** connects the classical vocabulary to convolutional networks, then spends its longest chapter on the part that decides whether a model is real: splitting a dataset so that the test set has not been contaminated by the training set. Detection, measurement uncertainty and tracking close the part, because a vision system in motion is a different problem from one that inspects still frames.

**Part Four — Making It Work** is engineering. Optics and lighting arithmetic, calibration, depth of field, motion blur, and the cost model that tells you when a laser, a load cell or a limit switch is a better answer than a camera.

The chapters are not identical in shape. Some are built around a single worked calculation, some around a failure story, one is a checklist. A book that repeats the same five sections thirteen times teaches the reader to skip, and the habit of skipping is fatal in a subject where the detail is the whole thing.

Every chapter closes with work. The headings vary — Problems, Exercises, Things to Try, Working Notes — because the work varies: some chapters want arithmetic, some want a decision, some want you to go and look at something with a camera.
