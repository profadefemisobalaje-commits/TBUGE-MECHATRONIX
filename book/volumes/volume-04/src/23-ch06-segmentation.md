# Segmentation: Regions, Thresholds and the Shape of Things

The parts arrived on a tray, nine of them, black plastic with a small locating hole in each. The counting system was a straightforward piece of work: threshold the image, find connected regions, count the ones above a size limit. It had been in service for a year and had never been wrong.

Then the mould was reconditioned, and the parts came out slightly shinier. On three of the nine, a specular highlight sat exactly where the moulding tool left a smooth patch. The highlight was bright enough to exceed the threshold. Each of those three parts now produced two regions instead of one, and the count read twelve.

The threshold was not wrong. The lighting was not wrong. The *definition of a region* — the assumption that a part is one connected blob of one brightness class — had stopped being true.

## Thresholding, and Where the Number Comes From

A global threshold turns a grayscale image into a binary one: pixels above the value become 1, pixels below become 0. It is the simplest segmentation there is and, used well, one of the most reliable.

Where does the number come from? Three sources, in descending order of quality.

**A physical argument.** If the illumination is controlled and the reflectances are known, the threshold corresponds to a reflectance. Under a backlight, a hole in a metal sheet transmits nearly all the light and the metal nearly none, so any threshold in the middle of the range separates them, and the exact value does not matter. This is the situation to aim for, because it is the only one that stays correct when the parts change.

**A histogram valley.** Plot the distribution of pixel values. A good image for thresholding is bimodal: two humps with a valley between. Put the threshold at the bottom of the valley, as far from both modes as possible.

**A formula.** Otsu's method chooses the threshold that maximises the variance *between* the two groups it creates. It is worth doing once by hand, because it makes visible what the algorithm assumes.

## Otsu by Hand

Ten pixels, values 30, 35, 40, 45, 50, 160, 170, 180, 190, 200. The overall mean is 110.

For each candidate threshold, split the pixels into those at or below it and those above, compute each group's mean and weight, and evaluate

> between-class variance = w0 × w1 × (m0 − m1)²

| Candidate | w0 | m0 | m1 | Between-class variance |
|---|---|---|---|---|
| 30 | 0.10 | 30.0 | 118.9 | 711 |
| 45 | 0.40 | 37.5 | 158.3 | 3,504 |
| 50 | 0.50 | 40.0 | 180.0 | 4,900 |
| 160 | 0.60 | 60.0 | 185.0 | 3,750 |
| 180 | 0.80 | 88.8 | 195.0 | 1,806 |

The maximum is 4,900, at a threshold of 50 — and, note, at every threshold between 50 and 100, because the data has a gap there and no pixels fall inside it. The method is not confused; the answer is genuinely non-unique, and any value in the gap separates the two groups perfectly.

That plateau is more informative than a single number. When Otsu returns a threshold in the middle of a wide empty gap, the image is easy and the task is robust. When the variance curve has a shallow peak and no gap, the image is marginal, and you should expect the result to depend on the day.

## What Thresholding Cannot Do

Two classes only. Three materials of different brightness need two thresholds, or a different method.

No spatial information. Each pixel is decided alone, so noise becomes speckle and a smudge becomes an island.

No notion of an object. A part with a hole yields two regions, and a part with a highlight yields three.

The repairs for all three are the same family: use neighbourhood information. Morphology cleans the shape; connected components assembles the shape; local thresholds handle uneven lighting.

## Morphology, on a Small Grid

Two operations, defined on a binary image and a small structuring element (usually 3 by 3).

**Erosion** keeps a pixel only if the entire structuring element fits inside the foreground. It shrinks objects and deletes anything thinner than the element.

**Dilation** sets a pixel if any part of the element touches foreground. It grows objects and closes small gaps.

Take this 5 by 5 patch, with a 3 by 3 block of ones surrounded by zeros:

    0  0  0  0  0
    0  1  1  1  0
    0  1  1  1  0
    0  1  1  1  0
    0  0  0  0  0

Eroding with a 3 by 3 square of ones leaves exactly one pixel: the centre. Every other foreground pixel has at least one zero in its neighbourhood.

Dilating the original fills the whole 5 by 5 patch: every pixel is within one step of the block.

Chaining them gives the two workhorses. **Opening** (erode, then dilate) removes small protrusions and isolated specks while leaving large shapes roughly the same size. **Closing** (dilate, then erode) fills pinholes and joins pieces separated by a thin gap — which is exactly the repair for the specular highlight, provided the gap is smaller than the element.

The size of the element is a physical statement: "anything smaller than 0.9 mm is noise". Express it in millimetres, and check it against the real feature sizes, or it will eventually delete a real defect.

## Connected Components

Once the image is binary, **connected components** labels each group of touching foreground pixels. Two flavours: 4-connectivity (up, down, left, right) and 8-connectivity (including diagonals). The choice changes the answer on diagonal structures — a thin diagonal line is one component under 8-connectivity and many under 4.

From each labelled region you can compute area (in pixels, then in square millimetres), centroid, bounding box, orientation, and a hundred shape descriptors. Two cautions.

**Area in pixels is not area in millimetres unless the scale is uniform.** With perspective it is not, and with a tilted part it is definitely not.

**Perimeter and area are biased by the threshold.** Raising the threshold shrinks every region slightly, and the bias is not uniform: a thin feature loses proportionally more than a thick one. Report the sensitivity: how much does the measured area change when the threshold moves by ten levels? If the answer is 8%, the measurement is a property of your threshold, not of the part.

## Colour, and the Space You Choose

Segmenting by colour is often the fastest route when the discriminator is hue: a red seal, a blue label, a copper contact.

Do it in a space where hue is separated from brightness, such as HSV, rather than in RGB, where a change in illumination moves all three channels together. In HSV, the hue channel wraps at 360 degrees, which means a red object spans values near 0 and near 180 — a detail that produces the classic bug of half an object being segmented and the other half not.

For materials rather than pigments, prefer ratios: the red-to-green ratio of copper is stable across lighting levels in a way that raw red is not. And if the lighting can be controlled, a coloured light is often better than a colour camera: illuminate with red, and a red part becomes bright while everything else stays dark, with no need for colour processing at all.

## When Objects Touch

Watershed segmentation treats brightness as a landscape and floods it from the minima. It is the standard answer to touching objects — overlapping nuts in a bin, adjacent cells under a microscope — and it depends entirely on finding good markers.

The practical version: threshold roughly to get the foreground, compute a distance transform (each foreground pixel's distance to the nearest background), and use the local maxima of that transform as seeds. The transform turns a dumbbell shape into two peaks joined by a saddle, and the watershed splits it there. If the peaks merge — genuinely touching objects of similar size — the method will not separate them, and the honest fix is to change the presentation so they do not touch.

## Exercises

1. Compute the between-class variance for these six values at thresholds 40 and 100: 20, 25, 30, 150, 160, 170. Which is the Otsu threshold?
2. A blob of 4,800 pixels at 0.05 mm per pixel: what is its area in square millimetres? If the threshold is raised so the blob shrinks by one pixel on every side, what is the new area, and what is the percentage error?
3. Erode and then dilate this 5 by 5 patch by hand, using a 3 by 3 square: rows 0,0,0,0,0 / 0,1,0,0,0 / 0,1,1,1,0 / 0,0,1,0,0 / 0,0,0,0,0. What survives?
4. Explain why closing fixes the specular highlight in the opening story, and name the condition under which it would not.
5. A line-scan system images a 300 mm wide strip at 0.1 mm per pixel. A defect must be detected if its area exceeds 0.5 mm². How many pixels is that, and what morphological opening size is safe?
6. Design a lighting setup for counting black plastic parts on a tray, such that the parts cannot break into two regions.
