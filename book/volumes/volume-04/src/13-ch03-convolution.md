# Convolution: The One Operation Everything Uses

Blur a photograph. Sharpen a photograph. Find its edges. Remove its noise. Detect a texture, measure a gradient, feed a convolutional network. Five different verbs, one arithmetic: a small grid of numbers slid across the image, multiplying and adding as it goes.

It is worth learning properly, because every vision system you will meet is either doing this or describing itself in its vocabulary. The operation is also the last piece of mathematics in this book that can be done entirely on paper in under a minute, so it is the last place where you can check your understanding by hand.

## The Kernel

A **kernel** — also called a filter, a mask, or a window — is a small grid of numbers, usually 3 by 3 or 5 by 5. The **convolution** places the kernel over a neighbourhood of the image, multiplies each image value by the kernel value underneath it, adds the products, and writes the total as one output value.

Take this patch of a grayscale image, with a single bright pixel in the middle:

    30   30   30
    30  200   30
    30   30   30

And this kernel, the average of a 3 by 3 neighbourhood, in which every weight is one ninth:

> kernel = (1/9) × [[1,1,1],[1,1,1],[1,1,1]]

The output for the centre position is

> (30 + 30 + 30 + 30 + 200 + 30 + 30 + 30 + 30) / 9 = 440 / 9 = 48.9

The bright pixel, which was 200, becomes 49. Its eight neighbours, which were 30, become 49 as well. The spot has not been removed; it has been spread over nine pixels, and the peak has fallen by three quarters.

That is blurring, and it is worth noticing that it is *lossy by design*. The kernel cannot know that the bright pixel was a defect and not noise. It treats every neighbourhood alike.

## A Kernel That Behaves Differently

Averaging treats the centre and the corners equally. A Gaussian kernel does not: it weights the centre most and the corners least, on the reasonable assumption that nearby pixels are more related than distant ones. The standard 3 by 3 approximation is

     1    2    1
     2    4    2
     1    2    1

with a divisor of 16, the sum of the weights. On the same patch:

> (30 + 60 + 30 + 60 + 800 + 60 + 30 + 60 + 30) / 16 = 1,160 / 16 = 72.5

Compare the two answers: mean gives 48.9, Gaussian gives 72.5. The Gaussian has smoothed less, keeping more of the peak, because it trusted the centre value more. That is the whole trade in one pair of numbers. A Gaussian blurs more gently and preserves structure slightly better; a box filter is cheaper and has a characteristic square artefact.

The divisor is not decoration. A kernel whose weights do not sum to the divisor will brighten or darken the image, and a kernel whose weights sum to zero will produce an image of edges only — which is exactly what the next chapter does.

## Borders, and the Dark Frame

A 3 by 3 kernel cannot be centred on a pixel at the very edge of the image, because two of its neighbours do not exist. Every library solves this with **padding**: it invents values outside the image.

Zero padding is the simplest and the worst. The invented neighbours are black, so the border pixels are dragged towards zero, and the result is a dark one-pixel frame around every filtered image. On a large image nobody notices. On a small region of interest, or when you filter repeatedly, the frame contaminates the measurement.

Other options, in increasing order of quality: replicate the edge value outwards; reflect the image at its border; wrap it around. Replication is the usual default in industrial libraries because it neither darkens nor invents a symmetry that is not there.

The general rule: filter inside a region, then measure in the interior. If you need values at the boundary, crop the region of interest slightly larger than you need and discard the filtered margin.

## Sharpening Is a Subtraction

If blurring is a kernel, sharpening is blurring used against itself. The classic **unsharp mask**:

> sharpened = original + amount × (original − blurred)

The bracket is the detail that the blur removed. Adding it back exaggerates local contrast, which the eye reads as sharpness.

Work it through on the bright pixel. With amount = 1 and the Gaussian above: 200 + (200 − 72.5) = 327.5. That value does not exist in an 8-bit image, and it clips to 255. The pixel saturates, the surrounding ring is darkened by the subtraction, and the result is a hard white dot with a black halo.

That halo is not a bug in your code. It is what sharpening does when pushed past the available range, and it is why sharpening is a display tool rather than a measurement tool. If you sharpen before measuring an edge position, you have moved the edge by an amount that depends on the amount setting.

## Separability: Why Blurring Is Cheaper Than It Looks

A 3 by 3 kernel needs nine multiplies per pixel. A 7 by 7 kernel needs forty-nine. That grows quickly, and it is why real systems exploit a property of the Gaussian: it can be written as two one-dimensional passes.

> [[1,2,1],[2,4,2],[1,2,1]] = [[1],[2],[1]] × [[1,2,1]]

So a 7 by 7 Gaussian can be applied as a 7-tap horizontal pass followed by a 7-tap vertical pass: fourteen multiplies instead of forty-nine, a saving of 3.5 times.

| Kernel size | Direct cost per pixel | Separable cost | Saving |
|---|---|---|---|
| 3 by 3 | 9 | 6 | 1.5× |
| 5 by 5 | 25 | 10 | 2.5× |
| 7 by 7 | 49 | 14 | 3.5× |
| 15 by 15 | 225 | 30 | 7.5× |

The saving is the reason large blurs are affordable at frame rate, and the property is worth checking before you implement any kernel by hand: if it can be factored into a row and a column, factor it.

## What a Filter Costs at Frame Rate

A 1,920 by 1,080 image has 2.07 million pixels. A 3 by 3 filter at 9 multiply-adds per pixel is 18.7 million operations per frame; at thirty frames per second that is 560 million per second. A modern processor does that without noticing, which is why filtering seems free.

It stops being free when the kernels multiply. A convolutional layer with thirty-two 3 by 3 filters over a 640 by 640 three-channel image performs 640 × 640 × 32 × 27 = 354 million multiply-accumulates for one frame. That number, not the elegance of the architecture, is what decides whether your system runs on a CPU or needs an accelerator.

The arithmetic is also where the practical wisdom lives: crop before you filter, build pipelines that stop early when a cheap test answers the question, and do not run a 15 by 15 blur on a 12-megapixel image if a 5 by 5 on a quarter-sized region will serve.

## Two Things Convolution Cannot Do

**It cannot remove an impulse of unbounded size.** A median filter can, because it takes the middle value of the neighbourhood: on the patch above, the median of the nine values is 30, so the bright pixel is deleted entirely rather than spread. Median filtering is nonlinear, it is not a convolution, and for salt-and-pepper noise it is the correct tool.

**It cannot preserve an edge and smooth a region with the same kernel.** This is the oldest tension in the subject; the bilateral filter and edge-preserving variants exist precisely to weaken the trade.

## Working Notes

1. Compute the mean-filtered and Gaussian-filtered values at the centre of this patch, with the kernels given above: 10, 10, 10, 10, 250, 10, 10, 10, 10. Which filter would you use to find a small bright defect, and why?
2. A kernel is [[0,1,0],[1,-4,1],[0,1,0]]. Its weights sum to zero. What will the output look like on a flat grey region? On an edge?
3. A colleague applies a 5 by 5 mean filter five times to clean up an image. What has happened to a 2-pixel-wide dark line after the third pass?
4. A 7 by 7 Gaussian must run on 4,096 by 3,000 images at 10 frames per second. Compute the operations per second for direct and separable implementations.
5. Padding with zeros produces a dark border. Describe what a threshold applied to the filtered image would do at the border, and how you would prevent it.
6. Write down a 3 by 3 kernel that would detect a horizontal line one pixel thick and nothing else. Test it on paper against a vertical line.
