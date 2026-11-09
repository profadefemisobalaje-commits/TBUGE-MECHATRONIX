# Gearboxes, Belts and Screws

A motor on its own is fast and weak. A robot needs slow and strong, which means something must trade speed for torque. That something is a transmission, and it is where most of the mechanical personality of a robot comes from: how precisely it moves, how loudly it complains, how long it lasts, and how much it costs.

The physics of a transmission is one sentence long: what you gain in torque you pay for in speed, plus a tax called efficiency. The engineering is everything else.

## Gears Do Two Things

A pair of gears with 10 teeth driving a gear with 50 teeth has a **ratio** of 5:1. The output turns five times more slowly than the input, and produces five times the torque, minus losses.

That is the whole trade. If the motor has 0.1 N·m at 3,000 revolutions per minute, the output has 0.5 N·m at 600 revolutions per minute. Power is unchanged in theory — torque times speed is the same on both sides — which is a useful check on any gear calculation. If your numbers show more power out than in, you have made an arithmetic error or invented a perpetual motion machine.

Two details matter more than the ratio.

**Efficiency.** Every stage loses some power to friction, and the losses compound. A single spur gear pair is about 97% efficient. A planetary gearbox is typically 90% for one stage and 80% for two. A worm drive is often 50% or worse, which is why it is used where you want the load to hold itself rather than where you want efficiency.

**Backlash.** The small gap between teeth, needed so that gears do not jam, means the output can move a little without the input moving at all. In a cheap gearbox, backlash might be 1 degree. On an arm 0.5 m long, 1 degree of backlash is 8.7 mm of free movement at the tip, in every direction change. A robot that must draw a straight line will produce a wavy one, and no amount of encoder resolution will fix it, because the error is in the mechanism, between the sensor and the tool.

| Transmission | Typical ratio per stage | Efficiency | Backlash | Used for |
|---|---|---|---|---|
| Spur gears | 3:1 to 6:1 | 97% | Moderate | Simple drives, printers |
| Planetary | 3:1 to 10:1 | 90% | Low | Robot joints, hubs |
| Worm drive | 10:1 to 100:1 | 40–70% | Moderate | Holding loads, lifts |
| Timing belt | 1:1 to 5:1 | 96% | Very low | Gantries, mobile robots |
| Lead screw | — | 30–50% | Low | Linear motion, low duty |
| Ball screw | — | 90% | Very low | Linear motion, precision |
| Harmonic drive | 30:1 to 160:1 | 70–85% | Near zero | Robot arm joints |

## Belts and Screws

Not every transmission is a gearbox, and two alternatives deserve their own paragraph because they solve problems gears cannot.

A **timing belt** transfers motion over a distance, which is exactly what a gantry or a mobile robot needs. It is cheap, quiet, tolerates misalignment and has almost no backlash if tensioned properly. Its weakness is stretch under load, which limits precision, and its need for maintenance as it ages.

A **lead screw** turns rotation into straight-line motion. One turn advances the nut by one **lead**, so the relationship is geometric rather than mysterious. The force it can produce is

> force = 2π × torque × efficiency / lead

Take a screw with a 5 mm lead, a torque of 0.5 N·m and an efficiency of 90%. The force is 2π × 0.5 × 0.9 / 0.005, which is about 565 N — enough to lift 57 kg. The same screw in a cheap ACME version at 40% efficiency gives about 250 N. The difference between a lead screw and a ball screw is mostly this efficiency, and it shows up as heat, noise and wear.

The trade for screws is speed: to move 200 mm at a 5 mm lead takes 40 turns. A motor at 3,000 revolutions per minute does that in 0.8 s, which is fine for a lift and slow for a pick-and-place axis.

## Zero Backlash and Why It Costs

For a robot arm that must follow a curved path while a camera watches, backlash is fatal. The mechanism must have as little free play as possible, and the two devices that achieve this are both expensive and both worth understanding.

A **harmonic drive** uses a flexible cup with external teeth that meshes with a rigid ring with internal teeth, two teeth fewer. A wave generator inside deforms the cup so that it engages at two points, and each turn of the input advances the output by two teeth. A ratio of 100:1 is normal, the backlash is effectively zero, and the device is compact and light for its torque. It is in the joints of many industrial and humanoid robots.

A **cycloidal drive** uses a similar principle with a lobed disc rolling inside a ring of pins. It handles shock loads better than a harmonic drive and is common in the base joints of heavy robots.

Both cost more than a planetary gearbox, and both repay it in a machine that can move accurately in both directions. When you see the price of a collaborative robot arm and wonder why it is not cheaper, look at the six harmonic drives in its joints.

## Choosing a Transmission

The decision comes down to five questions, and they can be answered on one page.

How much torque must be transmitted, and how fast must the output move? This fixes the ratio.

How much backlash can the task tolerate? A welding robot working on a fixture can tolerate a lot. A robot drawing with a pen cannot.

How efficient must it be? Battery-powered machines care, because loss becomes heat and heat becomes shorter runtime.

How long must it last, and how will it be maintained? Grease dries, belts stretch, gears wear.

What does it cost, and can you buy it? A custom gearbox is a project; a standard one is a purchase order.

## A Gearbox for a Four-Kilogram Arm

Work the whole selection once, because the arithmetic is what turns a catalogue into a decision.

The task: lift a 4 kg payload at 0.45 m from the joint, move it through 90 degrees in 0.8 s, and hold it still while a camera inspects it.

**Torque to hold.** Four kilograms at 0.45 m gives 4 × 9.81 × 0.45 = 17.7 N·m. Add the mass of the link itself, say 1.5 kg with its centre of mass at 0.25 m: another 3.7 N·m. Total static torque: 21.4 N·m.

**Torque to accelerate.** The inertia of the payload about the joint is 4 × 0.45² = 0.81 kg·m², and the link contributes perhaps 0.03 kg·m². For 90 degrees (1.57 rad) in 0.8 s with a smooth profile, the peak acceleration is roughly 4 × 1.57 / 0.8² = 9.8 rad/s². Torque is inertia times acceleration: 0.84 × 9.8 = 8.2 N·m.

**Total design torque.** 21.4 + 8.2 = 29.6 N·m. Add a margin of 50% for friction, misalignment and the fact that the payload may be heavier than the label: design for 45 N·m.

**Gearbox.** A 50:1 planetary gearbox with 85% efficiency requires 45 / (50 × 0.85) = 1.06 N·m at the motor. That is a substantial motor — a 200 W class brushless with a rated torque near 1 N·m — and it is the reason serious arms are expensive.

**Speed.** The motor must turn at 50 times the joint speed. The joint needs a peak of about 4 rad/s, so the motor needs 200 rad/s, or about 1,900 revolutions per minute. A motor rated at 3,000 revolutions per minute has headroom.

**Power and heat.** At 1.06 N·m and 200 rad/s the motor delivers 212 W. At 80% motor efficiency it draws 265 W and produces about 53 W of heat. A motor that size can dissipate 53 W continuously if it is mounted on a metal structure, and not if it is wrapped in plastic.

| Stage | Quantity | Value |
|---|---|---|
| Static torque | m × g × r, summed | 21.4 N·m |
| Acceleration torque | I × α | 8.2 N·m |
| Design torque with margin | × 1.5 | 45 N·m |
| Motor torque needed | design / (ratio × efficiency) | 1.06 N·m |
| Motor speed needed | joint speed × ratio | 200 rad/s |

If the arithmetic produces a motor you cannot afford, the design changes rather than the physics. Shorten the link, reduce the payload, add a counterbalance spring, or move the heavy parts of the tool closer to the wrist. Each of those is a design decision, and each is cheaper than buying a motor twice the size.

## Problems

1. A motor produces 0.12 N·m at 3,000 revolutions per minute. A 30:1 planetary gearbox with 90% efficiency is attached. Compute the output torque and output speed. Verify that the power is roughly preserved minus losses.

2. A gearbox has 1.5 degrees of backlash. How far does the tip of a 0.6 m arm move without the motor turning? What task would this ruin, and what task would not notice?

3. A lead screw has a lead of 8 mm and an efficiency of 45%. With 0.4 N·m of torque, what force can it produce? How many turns are needed to move 120 mm?

4. A machine needs 15 N·m at 1 rad/s from a 0.2 N·m motor. What ratio do you need, and which transmission type from the table would you choose? Justify the choice in two sentences.

5. Explain why a belt drive can have almost no backlash and still be less precise than a gear train.
