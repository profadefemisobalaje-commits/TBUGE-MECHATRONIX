# How a Camera Becomes a Number

The complaint arrived on a Tuesday, from a customer who had bought four hundred brackets. Three of them would not fit. The inspection cell had passed all four hundred, and its report was clean: no defects found, confidence high.

The engineer who investigated did the obvious things first. She re-ran the images through the model. She checked the model version against the one that had been validated. She looked at the rejected brackets on the bench, and then at the photograph the cell had taken of each one, and the answer was sitting there in plain sight. In the photograph the three bad brackets looked exactly like the good ones. Not similar. Identical, down to the last visible pixel.

The camera had been installed eight months earlier. In those eight months the maintenance team had replaced the diffuser on the light, and the new diffuser was a slightly different grade of acrylic. It scattered 12% less light. The automatic exposure on the camera had compensated, as it was designed to, by lengthening the exposure time from 4 milliseconds to 4.5. Everything stayed the same brightness. And the defect — a burr on an internal chamfer that was visible only as a shadow at a particular angle — stopped existing.

Nothing in that chain was a software failure. The software did exactly what it was told, on data that no longer contained the information it needed. This is the normal shape of a vision problem, and it is why this book starts with a sensor rather than a network.

## Light Is a Count

A camera does not record brightness. It counts photons.

Inside the sensor, behind each lenslet and colour filter, there is a small well of silicon. A photon that lands in the well has a chance of knocking an electron loose, and the electron stays there until the camera reads it out. The number of electrons is proportional to the number of photons that arrived during the exposure, and the number the camera reports is a digitised version of that count.

Two consequences follow immediately, and both matter more than any algorithm in this book.

The first is that brightness is a *rate*, not an amount. A dark scene exposed for a long time produces the same count as a bright scene exposed briefly. This is why a camera can photograph a black rubber seal and a white ceramic one and produce images of similar average brightness — and why that convenience is dangerous, because it erases the very difference that might have identified the material.

The second is that the count is finite. A typical industrial sensor well holds somewhere between ten thousand and fifty thousand electrons before it saturates. Once saturated, further light adds nothing, and the pixel reports its maximum value. Everything brighter than that limit becomes the same flat white. In a photograph of a shiny machined surface, the specular highlights are not bright; they are *uninformative*, and no amount of processing will recover texture that was clipped at the top of the well.

| Quantity | Typical value | What it means in practice |
|---|---|---|
| Full well capacity | 10,000 electrons | Brightest usable signal before clipping |
| Read noise | 3 electrons | Floor of the measurement, per pixel |
| Dark current | 1 electron per second at 25 °C | Grows with temperature and exposure |
| Bit depth | 8 or 12 bits | 256 or 4,096 reported levels |

## Counting Has a Square Root in It

Photon arrival is a random process. If a pixel receives an average of 10,000 photons, it will not receive exactly 10,000 every time; it will receive 10,000 give or take about 100, because the standard deviation of a count is its square root.

That rule, noise equals the square root of the signal, is the most useful single fact in practical vision. It says that bright pixels are proportionally cleaner than dark ones:

> relative noise = 1 / √(number of electrons)

At 10,000 electrons the relative noise is 1 part in 100, or 1%. At 400 electrons it is 1 part in 20, or 5%. At 100 electrons it is 10%.

Now put that beside a typical defect. A scratch on a brushed steel plate might reduce the local brightness by 8 grey levels out of 255. If the surface is well exposed and sitting at 180 grey levels, the pixel noise is around 4 levels, and the scratch is two noise-widths deep — detectable, marginally, with filtering. If the same surface is underexposed by two stops and sits at 45 levels, the noise is still around 4 levels, and the scratch is now a single noise-width: the signal has shrunk and the noise has not. The defect has not become smaller. It has become invisible.

This is the reason an engineer will spend an afternoon on a light and ten minutes on a threshold. Contrast is a physical quantity, bought with photons; thresholds only decide where to cut.

## Twelve Bits, Eight Bits, and the Cost of Rounding

Industrial cameras usually digitise to 12 bits, giving 4,096 levels, and then hand you 8-bit images because every library expects them. The conversion is a division by sixteen, and it throws away 94% of the available levels.

Usually that is fine, because noise occupies several of those levels anyway: there is no point preserving distinctions finer than the measurement uncertainty. It becomes a problem in three situations.

Low-contrast work. If the entire part occupies 20 grey levels in the 12-bit image — a dark component on a dark background — dividing by sixteen compresses it into one or two levels, and the shape dissolves into quantisation steps. Keep the 12-bit image, or stretch it before converting.

Gradient work. When you compute a derivative across neighbouring pixels, you are subtracting numbers that are nearly equal. Rounding error, which was invisible in the image, becomes a large fraction of the difference.

Thresholds near a peak. Histograms with a narrow mode become comb-like after aggressive rounding, and a threshold that looked stable starts jumping.

The practical rule: convert late, and never convert twice. Do the arithmetic in the widest format the camera supplies, and quantise only when you must display or store.

## Three Numbers Are Not a Colour

A colour camera puts a red, green or blue filter over each pixel in a repeating pattern, usually two greens for every red and blue. The camera then invents the missing two values at each pixel by interpolating from neighbours, a step called demosaicing.

Two things go wrong for machine vision.

The first is resolution. A 5-megapixel colour sensor resolves detail at roughly the level of a 1.25-megapixel monochrome sensor, because three of every four pixels are measuring a different colour rather than the same one. For measurement, monochrome is almost always the better choice.

The second is that the channel values depend on the illuminant. The same white plastic reads as slightly blue under daylight and slightly orange under an incandescent lamp, and the camera's automatic white balance will "correct" it — silently changing the numbers your threshold depends on. Turn automatic white balance off. If colour matters, calibrate it with a reference patch in the field of view, and treat the channels as ratios rather than as absolute values.

Colour is genuinely useful when the *material* is the discriminator: copper versus brass, a red seal versus a black one, a label versus a bare can. It is nearly useless for geometry, where monochrome contrast and a good light will beat it every time.

## The Three Dials

Every camera gives three controls that change exposure, and a beginner treats them as interchangeable because they all make the picture brighter. They are not interchangeable, and the table is worth memorising.

| Control | Changes brightness | Changes noise | Changes blur |
|---|---|---|---|
| Aperture (f-number) | Halving the area costs one stop | Little, if light is plentiful | Changes depth of field |
| Exposure time | Linear | Longer helps, until motion intrudes | Linear smear |
| Gain (ISO) | Linear | Amplifies signal and noise together | None |

Aperture is the only control that also changes what is in focus, and in a fixed rig it is usually set once and left. Exposure time is the control that interacts with motion: a conveyor at half a metre per second moves 2 mm in 4 milliseconds, and 2 mm at a resolution of 0.28 mm per pixel is seven pixels of smear. Gain is the control that looks free and is not, because it multiplies the noise as faithfully as it multiplies the signal.

The sequence that works is: open the aperture as far as depth of field allows, set the exposure time from the motion budget, and add gain only to reach the brightness that the exposure time forbids.

## What the Numbers Mean for the Rest of the Book

Every chapter that follows inherits the limits set here. A filter cannot recover a clipped highlight. A threshold cannot separate two materials that produce the same electron count. A network trained on images with automatic exposure has learned the camera's compensating behaviour as if it were a property of the part.

So the first question about any vision task is not "which algorithm" but "how many photons carrying the difference will land on how many pixels". If that question has no good answer, the honest response is to change the light, the lens, or the part's presentation — and to do it before writing a line of code.

## Exercises

1. A pixel receives 2,500 electrons on average. What is the relative shot noise, in percent? What does it become if the exposure is halved?
2. A defect changes local brightness by 6 grey levels. The region sits at 60 grey levels out of 255. Estimate the pixel noise from the square-root rule (assume the sensor maps 10,000 electrons to 255) and say whether the defect is detectable without filtering.
3. A camera is set to automatic exposure and automatic white balance, and runs unattended for a year. List three ways its output could change without any part changing.
4. Explain, in two sentences, why increasing gain does not improve a marginal image, using the electron counts from this chapter.
5. A shiny aluminium part produces large white regions with no texture. Describe two physical changes that would give the camera something to measure there.
6. You are asked to tell brass from copper on a conveyor. Would you use colour or monochrome with a coloured light? Give one advantage of each and pick one.
