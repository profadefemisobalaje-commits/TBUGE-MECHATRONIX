# Learning to See

The first version of the scratch detector was four hundred lines of code. Threshold, Sobel, dilate, skeletonise, measure length, filter by orientation, and a set of tuning constants that had been adjusted by hand over three weeks. It worked on the aluminium panels from line one. On line two, where the panels were anodised and slightly darker, it found scratches everywhere.

The replacement was a convolutional network trained on two thousand labelled images from both lines. It took a day to label, an afternoon to train, and it worked on both lines without a tuning constant in sight.

The temptation is to conclude that the network was smarter. What actually happened is more specific and more useful. The hand-written pipeline encoded a *guess* about what a scratch looks like — a thin dark line, roughly straight, longer than 5 millimetres — and the guess was the part that failed. The network did not need the guess. It learned a set of local patterns from examples, and among those patterns were several that the engineer would never have written down: the way a scratch interrupts the fine brushing direction, the way its ends taper, the way a polishing mark differs from a cut.

This chapter explains what a convolutional network is, in the same vocabulary as the previous chapters, and what it is not.

## A Layer Is a Stack of Kernels

A single 3 by 3 kernel produces one output image — one filter's opinion about every neighbourhood. A convolutional layer produces dozens: thirty-two kernels, say, each with its own nine weights, applied to the same input.

The output has thirty-two **channels**. Each channel is a map of how strongly that particular pattern occurs at each location. One channel may respond to horizontal edges, another to diagonal texture, another to a specific shade transition. Nobody assigns these roles; they emerge from training.

For colour input there is a further dimension: each kernel is 3 by 3 by 3, with separate weights for red, green and blue, so that the response can depend on colour as well as on shape.

The parameter count follows directly, and it is worth computing because it explains why convolution is efficient:

> parameters per kernel = (3 × 3 × 3) + 1 bias = 28
> thirty-two kernels = 896 parameters

A second layer of sixty-four kernels operating on those thirty-two channels needs 3 × 3 × 32 × 64 = 18,432 weights plus 64 biases, or 18,496.

Compare with a fully connected layer on the same image. A 640 by 640 colour image has 1.23 million input values; a single fully connected layer with a thousand outputs would need 1.23 billion weights. That is not merely expensive; it is a structural mistake, because it destroys the spatial arrangement that makes an image an image.

| Layer | Input | Weights | Output size |
|---|---|---|---|
| Conv 3×3×32 | 640×640×3 | 896 | 640×640×32 |
| Conv 3×3×64 | 640×640×32 | 18,496 | 640×640×64 |
| Max pool 2×2 | 640×640×64 | 0 | 320×320×64 |
| Dense 1,024 to 10 | 1,024 | 10,250 | 10 |

## Receptive Fields, and Why Depth Beats Width

Each output value of a single 3 by 3 layer depends on a 3 by 3 patch of the input. Stack three such layers and the third depends on a 7 by 7 patch: each step adds two pixels of context in each direction.

> receptive field after n layers of 3 by 3 = 1 + 2n

So four layers see 9 by 9, eight layers see 17 by 17, and twenty layers see 41 by 41. A deep stack of small kernels covers a wide area with far fewer parameters than one large kernel, and — the reason it works — it builds a hierarchy. Early layers see edges, middle layers see combinations of edges, later layers see parts of objects.

This is the same trade already met in Chapter Three with separable filters: structure beats brute force. A single 41 by 41 kernel would need 1,681 weights per channel; twenty 3 by 3 layers need 180.

## What the Network Learns, and What It Is Told

Three things determine what a network learns, and only one of them is the architecture.

**The labels.** If a scratch is labelled only when it is longer than 5 millimetres, the network learns that threshold, faithfully, including its arbitrariness.

**The examples.** A dataset of panels from one supplier teaches the appearance of that supplier's surface. The network will treat a different surface finish as a different phenomenon, and no amount of confidence will warn you.

**The augmentation.** This is where the engineer's judgement enters most directly. Augmentation means generating modified copies of the training images — flipped, rotated, brightened, blurred, noised — so the network sees the variations it must tolerate.

It is powerful and it is dangerous, because an augmentation asserts an invariance. Flipping a photo of a scratch is harmless: a scratch looks like a scratch mirrored. Flipping an image of a part with an asymmetric feature is a lie: you have told the network that the mirrored part is the same part, and it will believe you. The test is simple and must be asked every time: *would a human still label this image the same way?* If not, the augmentation is teaching a falsehood.

## Transfer Learning, Honestly

Most industrial projects do not train a network from scratch. They start from a model trained on millions of general images and continue training on a few thousand of their own. This works because the early layers of any vision network learn edges, blobs and textures — features that are as true of castings as of cats.

What it buys: usable accuracy with a thousand images instead of a hundred thousand, and faster convergence.

What it costs: a subtle dependence on the pre-training data's assumptions. Networks pre-trained on photographs of scenes expect certain statistics of colour and contrast, and an industrial image — grey, flat, high-contrast, tightly cropped — is not a photograph of a scene. The mismatch is usually small and occasionally decisive, and the remedy is to fine-tune more layers rather than fewer, so that the later stages can specialise.

A rough rule that holds up in practice: freeze nothing if you have more than a thousand labelled images; freeze the early third if you have a few hundred; and if you have fewer than a hundred, reconsider whether a network is the right tool at all.

## What a Network Does Not Do

It does not measure. A network can tell you a scratch is present with high confidence and be unable to tell you it is 6.2 millimetres long to a tenth of a millimetre. Measurement still wants edges, calibration, and geometry.

It does not count reliably. Counting is a global operation, and networks that look at local patches have no mechanism for it; objects that touch or overlap are counted wrongly, confidently.

It does not know when it is out of its depth. A network asked about a surface it has never seen will produce a number, and the number will look like all its other numbers.

It does not replace the light. If the defect is not in the photons, it is not in the network, and the most common cause of a disappointing model is a dataset captured under lighting that never revealed the defect properly in the first place.

## Exercises

1. Compute the parameter count for a layer of sixteen 5 by 5 kernels applied to a 640 by 640 single-channel image. How does it compare with sixteen 3 by 3 kernels?
2. Six consecutive 3 by 3 layers: what is the receptive field? How many parameters per channel path, compared with a single 13 by 13 kernel?
3. A dataset contains 1,500 images of steel panels and 200 of aluminium panels. Predict two specific failures of the trained model, and design an augmentation policy that would not fix them.
4. For each augmentation, say whether it is safe, and why: horizontal flip of a scratch image; 90-degree rotation of an image of a gear; brightness change of ±20%; Gaussian blur; colour inversion.
5. A network reports 0.98 confidence on an image of a part type it has never seen. Explain to a plant manager, in three sentences, what that number means.
6. A 640 by 640 image passes through four conv layers of 32, 64, 64 and 128 channels with 3 by 3 kernels, with a 2 by 2 pool after the second and fourth. Sketch the tensor sizes at each stage and compute the multiply-accumulates for the first layer.
