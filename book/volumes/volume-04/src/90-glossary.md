# Glossary

**Aliasing** — the appearance of false coarse patterns when a scene is sampled too coarsely. Caused by sampling, not by the software; cured by optics or by moving closer.

**Aperture** — the adjustable opening in a lens. Smaller openings increase depth of field and reduce light.

**Backlight** — illumination from behind the part, producing a silhouette. The most reliable lighting for outline measurement.

**Bayer pattern** — the repeating red-green-blue filter arrangement on a colour sensor. Three quarters of the pixels measure a colour other than the one they are used for.

**Bilateral filter** — a smoothing filter that preserves edges by weighting neighbours according to both distance and similarity.

**Bit depth** — the number of levels a sensor can report. Eight bits gives 256; twelve bits gives 4,096.

**Blur circle** — the diameter of a point image at the sensor. Used to define acceptable focus.

**Calibration** — the procedure that estimates a camera's internal geometry and its position in the world, from images of a known target.

**Capability index (%GRR)** — six times the measurement uncertainty divided by the tolerance width. Under 10% is excellent; over 30% is disqualifying.

**Canny detector** — an edge detector combining smoothing, gradient, non-maximum suppression and hysteresis thresholds.

**Connected components** — the grouping of touching foreground pixels into labelled regions.

**Convolution** — the operation of sliding a small kernel across an image, multiplying and summing, to produce a filtered value at every position.

**Coaxial light** — illumination along the lens axis, revealing flat shiny surfaces and exposing dents as dark spots.

**Dark field** — illumination at a very low angle, so that flat surfaces appear dark and scratches scatter light into the camera.

**Demosaicing** — the interpolation that invents the missing colour values at each pixel of a colour sensor.

**Depth of field** — the range of distances over which the image is acceptably sharp. Falls rapidly as magnification rises.

**Diffraction limit** — the smallest spot an aperture can form, roughly 2.44 wavelengths times the f-number.

**Disparity** — the horizontal shift of a point between two stereo images. Inversely proportional to distance.

**Erosion** — a morphological operation that keeps a foreground pixel only if the whole structuring element fits inside the foreground.

**Dilation** — the dual operation, growing foreground regions by one element.

**Exposure time** — the duration over which light is collected. Sets motion blur directly.

**Feature (local)** — a distinctive image point, such as a corner, described in a way that survives rotation, scale and lighting change.

**Field of view** — the width and height of the scene that the sensor covers at a given distance.

**Fringe projection** — a structured-light method using a sequence of sinusoidal patterns to measure depth to high precision.

**Gain** — amplification applied after collection. Increases signal and noise together.

**Gaussian blur** — smoothing with weights falling off from the centre. Separable into two one-dimensional passes.

**Gradient** — the rate of change of brightness, as a vector with horizontal and vertical components.

**Homography** — the eight-parameter mapping between two views of a flat surface.

**Hysteresis** — the use of two thresholds so that a weak edge is kept only when it connects to a strong one.

**Intersection over union (IoU)** — overlap area divided by union area. The standard measure of box agreement.

**Intrinsic parameters** — the camera's focal length in pixels, optical centre and distortion, independent of where it is mounted.

**Kernel** — the small grid of weights used in a convolution.

**Kalman filter** — an estimator that combines a prediction from motion with a measurement, weighted by their uncertainties.

**Learning curve** — performance plotted against the amount of training data used.

**Median filter** — a nonlinear filter that replaces each pixel with the median of its neighbourhood; removes impulses without spreading them.

**Morphology** — operations on binary or grey images defined by a structuring element; opening and closing are the common combinations.

**Non-maximum suppression** — thinning a response to its local maxima, or removing duplicate detections.

**Otsu threshold** — the threshold that maximises the variance between the two groups it creates.

**Photosite** — the individual light-collecting element of a sensor, beneath one colour filter.

**Point cloud** — a set of three-dimensional points produced by a depth sensor.

**Precision and recall** — the fraction of positive decisions that are correct, and the fraction of real positives that are found.

**RANSAC** — a consensus-fitting method that repeatedly samples the minimum number of correspondences and keeps the model with the most agreement.

**Receptive field** — the region of the input image that influences one output value of a network layer.

**Reprojection error** — the average pixel distance between where a calibration target's corners should appear and where they do appear.

**Repeatability** — the spread of repeated measurements of the same object under the same conditions.

**Sampling interval** — millimetres of scene per pixel. The decisive number for whether a task is possible.

**Specular reflection** — mirror-like reflection of the light source rather than the surface. Produces highlights that hide detail.

**Structured light** — projecting a known pattern to supply texture or to encode depth.

**Stereo vision** — depth from two views, using the geometry of disparity.

**Structuring element** — the small shape used in morphological operations.

**Threshold** — the value at which a continuous measurement becomes a decision.

**Time of flight** — depth from the phase delay of modulated light. Coarse, fast, and robust to texture.

**Transfer learning** — starting from a network trained on a large general dataset and continuing training on a smaller specific one.

**Watershed** — segmentation by flooding a brightness landscape from markers.
