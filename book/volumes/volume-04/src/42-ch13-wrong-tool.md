# When Vision Is the Wrong Tool

A hole, 6 millimetres in diameter, drilled 22 millimetres deep into a blind bore. The drawing specifies a depth of 22 ±0.15 mm, and the inspector must check every tenth part.

The proposal on the table was a vision system: a camera looking down the bore with a coaxial light, measuring the depth from the apparent position of the bottom face. The quotation was 38,000, and the demonstration worked on a sample.

It was the wrong tool, for a reason that can be stated in one sentence: a camera looking down a 22-millimetre hole sees a circle of light at the bottom, and the relationship between that circle and the depth depends on the reflectivity of the bottom face, the tilt of the drill, the oil film, and the amount of light reaching the bottom — which falls off with the square of the depth. The measurement would work on clean, dry, perpendicular samples and fail on the third shift.

An air gauge cost 9,000, measured depth to 0.01 mm, tolerated oil, and was insensitive to everything except the diameter of the hole. The right answer was not a better camera. It was a different sensor.

This chapter is the discipline of asking that question early.

## Four Questions

Before any vision project, ask four questions in order. A "no" at any point is a stop, not a challenge.

**Is the information carried by light?** If the feature does not change the brightness, colour or polarisation of what leaves the surface, no camera will see it. Depth inside a narrow bore, hardness, internal voids, electrical continuity and material composition are the common cases where the answer is no.

**Is the tolerance within reach of the optics?** Compute the sampling interval, then the repeatability, then the capability index. A tolerance of ±0.05 mm demands a sampling interval of about 0.01 mm and a repeatability better than 0.01 mm — which is achievable, at a price, on a rigid rig.

**Is the environment stable enough?** Light, temperature, vibration, dust, coolant spray, and the presence of people all change between the demonstration and the third shift. If the answer is "we will manage it", the project has a hidden cost that will appear later.

**Is the cost justified?** Not "is it impressive", but "what does a missed defect cost, how many defects occur, and how many years does the capital take to return".

## The Alternative Toolkit

Engineers who work only with cameras tend to see every problem as an image. The table is a reminder that the sensing world is wider.

| Requirement | Better first choice |
|---|---|
| Depth in a narrow bore, with oil present | Air gauge |
| Presence of a metal part at 1 mm | Inductive proximity sensor |
| Thickness of a sheet, from one side | Ultrasonic gauge |
| Force, weight, fill level | Load cell |
| Cracks in conductive material | Eddy current |
| Sub-micrometre displacement | LVDT or laser interferometer |
| Internal structure, voids, welds | X-ray or ultrasound |
| Identification, not inspection | Barcode, RFID |
| Temperature, stress, gas | Thermal camera, strain gauge, sensor |

None of these is exotic. Most cost less than a vision system, and all of them are insensitive to lighting, which is the failure mode that consumes the most engineering time in vision projects.

There is also a class of problem where the correct answer is not a sensor at all but a change to the process: a fixture that makes the feature accessible, a poke-yoke that makes the error impossible, a drill with a depth stop. The best inspection is the one that is not needed.

## The Arithmetic of Justification

A vision project is capital spending, and the case is made with numbers.

Suppose a line produces 200,000 parts a year. The current escape rate is 1.2%, meaning 2,400 defective parts reach the customer, each costing 8 in warranty, rework and goodwill: 19,200 a year. A vision system costing 45,000 is predicted to reduce escapes to 0.2%, or 400 parts, costing 3,200.

| Item | Before | After |
|---|---|---|
| Escapes per year | 2,400 | 400 |
| Cost of escapes | 19,200 | 3,200 |
| Inspection labour | 12,000 | 4,000 |
| Annual saving | — | 24,000 |
| Capital | — | 45,000 |
| Simple payback | — | 1.9 years |

The arithmetic is simple and the assumptions are where projects die. Three of them need testing before the capital is committed.

Does the escape rate really fall by that much? A system with 95% recall and 12% precision does not remove 83% of escapes; it removes 95% of the escapes it sees, and it creates a new cost in false alarms. Recompute with the actual operating point, and with the labour cost of handling rejections.

Does the labour saving exist? Inspectors are rarely removed; they are reassigned. The saving is real only if the headcount falls or the capacity is used.

Is the capital complete? The camera, lens, light and enclosure are perhaps half of it. Fixtures, integration, commissioning, validation, training and the first year of support are the rest, and they are the part that surprises.

## Where Machine Learning Fits, and Where It Does Not

Inside a vision system, learning is the right tool for appearance problems: texture, scratches, corrosion, weld quality, fabric defects. These are cases where the rule is easy for a person to recognise and hard to write down, which is exactly the signature of a learning problem.

It is the wrong tool for measurement, for counting, for geometric verification, and for anything where the answer must be traceable to a calibrated instrument. A network that reports 6.2 mm has not measured 6.2 mm; it has classified an image into a bin labelled "about 6.2 mm".

The most reliable industrial pattern combines the two: classical geometry where geometry is the question, learning where appearance is the question, and a rule that vetoes physically impossible answers. A model that proposes a 12 mm scratch on a part that is 8 mm wide should be overruled by arithmetic, not by a bigger model.

## A Closing Checklist

Ten questions, in the order they should be asked. A project that can answer all ten before writing code has a reasonable chance.

1. What exactly must be decided, in millimetres or in classes, and at what rate?
2. Is the discriminating information in the light, and which lighting geometry reveals it?
3. What sampling interval does the tolerance require, and what field of view does that imply?
4. What is the depth of field, and does the part fit inside it?
5. How fast does the part move, and what exposure does that allow?
6. Where will the light come from in production, and what changes when the sun moves or a lamp ages?
7. What is the repeatability of the measurement, measured over fifty images of one part?
8. What is the capability index against the tolerance, and is it under 30%?
9. How will the dataset be split so that the validation score means something?
10. What is the annual saving, what is the true capital cost, and what is the payback?

Notice that only two of the ten involve software. This is not an accident of the subject; it is the subject.

## For Practice

Take a task you know — from work, from a project, from the room you are sitting in — and answer the ten questions for it on one page. Do not look anything up. The gaps in your page are the things to investigate, and the exercise is more valuable than it sounds, because most failed vision projects are failures to write that page.

Then take the four questions and apply them to a problem you have already been told needs vision. If the honest answer is air gauge, load cell or fixture, say so. Saying so early is the most valuable thing a vision engineer does.
