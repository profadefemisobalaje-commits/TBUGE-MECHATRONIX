# Light, Lenses and the Rig

A project was commissioned in November and accepted in February. Between those dates the plant's heating was on, the workshop doors were shut, and the ambient temperature in the inspection cell sat at about 23 degrees. In June the doors opened and the cell reached 33 degrees.

The camera did not care; it was rated to 45. The lens did not care. The part did not care. The *bracket* cared: three hundred millimetres of extruded aluminium, bolted to a frame at one end and carrying the camera at the other, expanded by

> 300 mm × 23 × 10^-6 per °C × 10 °C = 0.069 mm

Sixty-nine micrometres. On a task with a tolerance of ±0.1 mm and a sampling interval of 0.04 mm per pixel, that is 1.7 pixels of drift, appearing slowly over a fortnight, with no error message and no obvious cause.

Everything in this chapter is at that level: micrometres, millimetres, and the difference between a rig that measures and a rig that merely takes pictures. It is the least glamorous material in the book and the most decisive.

## Choosing a Lens From the Field of View

Three numbers determine the lens, and any two determine the third.

> focal length = (sensor width × working distance) / field of view width

A 8.8 mm sensor, a field of view of 100 mm and a working distance of 400 mm:

> f = 8.8 × 400 / 100 = 35 mm

In practice, choose the working distance from the machine — far enough that the camera is out of the way of hands and tooling — choose the field of view from the part plus a margin for positioning error, and compute the focal length. Then pick the nearest standard lens and check what the field of view becomes, because lenses come in steps.

The same arithmetic in the other direction is the one that catches people out: given a lens, the working distance required for a field of view may be impossible. A 12 mm lens on that sensor needs a working distance of 136 mm to see 100 mm — closer than most cells allow, and inside the near limit of many lenses.

## Depth of Field: The Budget Nobody Makes

A lens focuses at one distance. Either side of it, sharpness falls gradually, and the range over which it is acceptable is the **depth of field**. It shrinks rapidly as magnification rises.

| Field of view | Magnification | Depth of field at f/8 |
|---|---|---|
| 300 mm | 0.029 | about 134 mm |
| 100 mm | 0.088 | about 16 mm |
| 30 mm | 0.293 | about 1.7 mm |

The numbers assume a blur circle of two pixels and a pixel size of about 3.5 micrometres. Read the bottom row and think about what it implies: at a field of view of 30 mm, only 1.7 mm of the part is sharp. A casting that is 12 mm thick cannot be inspected in one image at that magnification unless the aperture is closed — which costs light, and light costs exposure time, and exposure time costs motion blur.

This chain of trades is the substance of rig design. It is not unusual to discover that a specification is achievable only at f/16 with a five-millisecond exposure, which requires a light four times brighter than the one originally budgeted.

## The Diffraction Floor

Closing the aperture has a limit that is not mechanical. Light passing through a small hole spreads, and the spot it forms has a diameter of roughly

> 2.44 × wavelength × f-number

At f/8 with green light of 0.55 micrometres, that is 10.7 micrometres. At f/16 it is 21.5 micrometres.

Now compare with the pixel: a modern sensor's pixels are around 3.5 micrometres. At f/16 the optical blur covers six pixels, and no amount of resolution in the sensor will recover detail finer than that. This is why small-pixel cameras often perform no better than larger-pixel ones on fine work: the optics, not the sensor, is the limit.

The working compromise for most industrial cells sits between f/4 and f/8, where the lens is sharp, the depth of field is workable at moderate magnification, and diffraction has not yet taken over.

## Lighting Is Geometry, Not Brightness

The single most common mistake in machine vision is to treat lighting as a brightness problem. It is a geometry problem: the question is not how much light arrives, but from which directions, and what the surface does with it.

Four arrangements cover most needs.

**Bright field.** Light arrives from the camera's side, at a shallow angle or through a diffuser above the part. Flat surfaces appear bright, tilted or scratched surfaces appear dark, and texture is emphasised. The standard for surface inspection.

**Dark field.** Light arrives at a very low angle, nearly parallel to the surface. A flat surface reflects it away from the camera and appears black; any edge, scratch or raised feature scatters light into the camera and appears bright. Superb for finding scratches on polished metal, hopeless for reading a label.

**Backlight.** The light is behind the part, and the camera sees a silhouette. Contrast is perfect, the part is a black shape on a white field, and every measurement of outline, hole and gap becomes trivial. Useless for surface defects, and the first thing to try whenever a task is about shape.

**Dome and coaxial.** A dome scatters light from every direction, removing shadows and giving a soft even illumination; coaxial light travels along the lens axis and reflects straight back from shiny flat surfaces, revealing dents as dark spots on a bright field. Both are ways of controlling reflections rather than adding light.

| Task | First light to try |
|---|---|
| Measure the outline of a part | Backlight |
| Find scratches on polished metal | Dark field, low angle |
| Read a printed label | Diffuse dome, or coaxial |
| Detect a dent in painted steel | Coaxial |
| Segment a dark part from a dark background | Backlight, or a colour that the part reflects |

## Colour as a Filter

A monochrome camera with a coloured light is often better than a colour camera with white light, because the light chooses what the part reflects before the sensor ever sees it.

The rule is complementary colours. To make a red label disappear into a white background, illuminate with red: the label reflects red strongly, the white background reflects it too — both bright. To make the red label dark against white, illuminate with green or blue: the red label absorbs it, the white background reflects it. One lamp, one decision, and a contrast ratio that no amount of processing could produce.

For metals, wavelength affects penetration and scattering, and the effect can be large — copper under blue light looks different from copper under red. This is an advantage when a material must be distinguished, and a hazard when the ambient light changes colour across a shift.

## Motion, Exposure and Light Are One Equation

A conveyor at half a metre per second, an exposure of ten milliseconds, and a sampling interval of 0.1 mm per pixel:

> smear = 500 mm/s × 0.010 s = 5 mm = 50 pixels

Fifty pixels of blur is not a photograph of a part; it is a photograph of a part's journey. To reduce it to one pixel, the exposure must be 0.2 milliseconds — forty times shorter, which requires forty times the light, or a strobe synchronised to the encoder.

This is why high-speed vision is mostly a lighting discipline. Pulsed LEDs delivering the same energy in a hundredth of the time are standard equipment, and the design question becomes whether the part is in the strobe's field long enough to be illuminated at all.

## The Rig Is Part of the Measurement

Everything above assumes the camera stays where it was put. Four mechanisms move it.

**Thermal expansion**, as in the opening story. Repair: shorter mounts, a material with a lower coefficient, a temperature log, or a reference target visible in every image.

**Vibration.** A conveyor or a press transmits motion through the floor. A one-millisecond exposure during a vibration of 0.05 mm amplitude produces a blurred edge; a longer exposure produces an average that is stable but biased.

**Mechanical creep.** Bolted joints settle, particularly in the weeks after installation. This is one reason calibration drifts early and then stabilises.

**Dirt.** A fingerprint on a lens or a dust speck on a window is a permanent defect in every image. Air purges and scheduled cleaning are not optional, and the cleaning interval should be measured rather than guessed — photograph a white target daily and watch the mean brightness.

The general defence is a **reference target** inside the field of view: a small machined feature, or a fiducial, whose measured position and size are checked every cycle. If the reference moves, the rig has moved, and the correction can be applied to everything else. This single habit converts an unmonitored measurement into a monitored one.

## Problems

1. A 11.3 mm sensor must see a 220 mm field of view at 500 mm working distance. What focal length is needed? What field of view would a 25 mm lens give at that distance?
2. A cell needs a depth of field of 8 mm at a field of view of 40 mm. Using the table's trend, is f/8 sufficient? What would you change?
3. Compute the diffraction spot at f/5.6 and compare with a 2.4 micrometre pixel. At what f-number does the spot exceed two pixels?
4. A conveyor runs at 1.2 m/s and the sampling interval is 0.08 mm per pixel. What exposure time keeps the smear under 1.5 pixels?
5. A bracket is 450 mm of steel (coefficient 12 × 10^-6 per °C) and a second is 250 mm of aluminium. Which drifts more over a 15 °C change, and by how much?
6. A task requires distinguishing a black plastic part from a dark grey one on a black conveyor. Propose a lighting arrangement and explain, in terms of reflection, why it works.
7. Design a monitoring scheme that would have detected the thermal drift in the opening story within a week, using equipment already present in the cell.
