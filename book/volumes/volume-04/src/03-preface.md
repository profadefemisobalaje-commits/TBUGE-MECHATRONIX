# Preface

Vision is the sense everyone assumes a machine already has. We point a camera at a part, the software finds the defect, and the transaction looks trivial because human beings do it without effort twenty times a second. Underneath that effortlessness sits a chain of assumptions — about light, about focus, about what a defect looks like, about what "looks like" even means when the surface is scratched, oily, or moving.

When the chain breaks, it breaks quietly. A camera does not complain that the exposure has doubled since the last service. It does not mention that the new supplier's parts are two shades darker. It reports a confidence score, and the score is confident. Vision failures are almost always failures of the physical setup being described as failures of the model.

So this volume begins before the model. Chapters on sensors, sampling, optics and light come first, because the arithmetic of a lens determines what any algorithm downstream can possibly see. The middle chapters build the classical tools: convolution, edges, features, thresholding, depth. They remain in daily use in factories, and more importantly they teach the vocabulary that modern networks inherited — the kernel, the receptive field, the response map. The later chapters turn to learning, and to the unglamorous work that decides whether a vision system survives its second month: calibration, dataset capture, honest splitting, tracking, and the maintenance of a rig that drifts by a fraction of a millimetre a week.

## What this volume asks of you

Arithmetic, and a willingness to draw. Every operation in the first half of the book can be done with a pencil on a grid of nine numbers, and doing it once is worth reading about it ten times. When a kernel is introduced, the page shows a small patch of pixels and the sum that produces one output value. Work it through on paper. The moment the mechanic becomes obvious is the moment the rest of the subject becomes tractable.

A camera helps. Even a phone camera and a torch will do for most of the exercises: photograph a textured surface at an angle, photograph a printed edge, photograph the same object twice under different light, and look at the numbers.

## What it does not ask

No calculus, no matrix algebra, no framework. Networks appear near the end, and they are described in terms of the same convolution already built by hand, so that a reader who can compute a Sobel response has the concept needed to understand a layer.

## A word about the pictures

A book about images has an obvious difficulty: the pictures live in the reader's head and in the code, not on the page. Where a figure would help, the text gives a small table of numbers instead, and describes what you would see. It is slower than a photograph and it is more honest, because you can check the numbers.

## The promise

By the last chapter you should be able to stand in front of a machine, look at the camera, the light and the part, and estimate — before any software runs — whether the task is possible, how many pixels it needs, how much light it needs, and where it will fail. That estimate is the difference between a project that ships and a project that produces a demonstration.
