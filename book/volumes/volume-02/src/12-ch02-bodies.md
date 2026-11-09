# Bodies: Links, Frames and Stiffness

A robot arm looks solid. It is, in fact, a spring with a motor on the end. Load it and it bends; tap it and it rings; run it fast and it whips. The entire art of mechanical design for robots is deciding where the bending is acceptable, where it must be eliminated, and what it costs to eliminate it.

This chapter is about the bones of the machine: the links that connect one joint to the next, the frames that describe where everything is, and the two properties that decide whether a design will work — stiffness and mass. It is not a chapter about manufacturing. It is a chapter about the numbers you need before you choose a material, a wall thickness or a bearing.

## A Body Is a Set of Frames

Engineers describe a robot's geometry with **frames**: coordinate systems attached to parts of the machine. There is a frame fixed to the floor (the base), a frame at the end of each link, and a frame at the tool. The position and orientation of one frame relative to another is what a robot program ultimately computes.

This is not abstraction for its own sake. A robot that picks up a part must know where the part is in the camera's frame, where the camera is in the base's frame, and where the gripper is in the base's frame. If any of those three relationships is wrong, the robot misses. Most industrial robot failures that involve "the robot went to the wrong place" are frame errors, not control errors: a camera mounted two millimetres off its nominal bracket, or a tool length entered incorrectly in the controller.

The chain of frames from base to tool is called the **kinematic chain**, and every link in the chain adds a small error. A six-axis arm with a repeatability of 0.05 mm at the tool may have a link-by-link tolerance that adds up to several tenths of a millimetre in absolute accuracy. Repeatability — returning to the same point — is easier than accuracy — going to the right point. A machine can be very repeatable and quite inaccurate, which is fine for a welding robot working on a fixture and hopeless for a robot that must use a camera to find a part on a table.

## Stiffness Is Not Strength

Two properties are constantly confused, and the confusion produces machines that break or wobble for no apparent reason.

**Strength** is the load at which something breaks or yields permanently. **Stiffness** is how much it deflects under a load it survives. A steel ruler is strong and floppy. A ceramic plate is stiff and brittle.

Robots usually fail on stiffness long before they fail on strength. The arm does not break; it sags, so the gripper arrives 3 mm low. It does not snap; it vibrates for 400 ms after every move, so the cycle time doubles.

The deflection of a simple cantilever — a link fixed at one end, loaded at the other — is given by

> deflection = force × length³ / (3 × E × I)

where E is the stiffness of the material (its Young's modulus) and I is a property of the cross-section called the second moment of area. The important term is the cube on the length. Double the reach and the deflection goes up eightfold for the same load and section. This single fact explains why long-reach robots are expensive: they need enormous sections, or they accept poor accuracy, or they are slow.

Work an example. Take an aluminium tube 0.5 m long, 30 mm outside diameter, 2 mm wall, with a 50 N load at the tip — about 5 kg hanging off the end.

- The second moment of area for a tube is π/64 times (outer diameter to the fourth power minus inner diameter to the fourth power). With those dimensions, I is about 1.73 × 10⁻⁸ m⁴.
- Aluminium has E of about 69 GPa, or 69 × 10⁹ N/m².
- The deflection is 50 × 0.125 / (3 × 69 × 10⁹ × 1.73 × 10⁻⁸), which is approximately 0.0017 m, or 1.7 mm.

A 5 kg load bends the arm by 1.7 mm. If your task needs 0.2 mm, the tube is ten times too floppy. Doubling the wall thickness does not quadruple the stiffness, because I depends on the difference of fourth powers; increasing the diameter helps far more than adding material. This is why robot links are tubes and not solid bars: a tube puts material where it does the most good, away from the neutral axis.

## The Enemy Is Vibration

A spring with a mass on the end has a natural frequency at which it likes to oscillate. Push it and let go, and it rings at that frequency. In a robot, that ringing is the settling time after every move, and settling time is often the largest single component of a cycle.

The natural frequency of a simple mass on a spring is

> frequency = (1 / 2π) × square root of (stiffness / mass)

For the tube above, the stiffness at the tip is about 28,700 N/m. With a 2 kg mass at the end, the frequency works out to about 19 Hz. That means the arm oscillates roughly nineteen times a second after a sudden stop, and each oscillation decays according to the damping. With light damping, the arm may still be visibly moving 300 ms later.

Three consequences follow, and all three are design decisions.

You can make the structure stiffer, which raises the frequency and shortens the ringing. This costs mass and money.

You can reduce the moving mass, especially at the far end. A gripper that weighs 1 kg instead of 3 kg does more for the dynamics than a thicker tube, because the mass is at the tip where it counts most.

You can shape the motion so that it does not excite the resonance. This is called input shaping, and it is a lovely piece of engineering: instead of moving directly to the target, the controller sends two or three impulses timed to cancel the oscillation. It costs nothing but software, and it can cut settling time by half on a machine that is already built.

## Materials, and What They Cost

The choice of material is a compromise between stiffness, weight, strength, cost and how easy it is to make into the shape you want.

| Material | Density (kg/m³) | Young's modulus (GPa) | Stiffness per kg (MN·m/kg) | Typical use |
|---|---|---|---|---|
| Steel | 7,850 | 200 | 25 | Bearings, screws, shafts |
| Aluminium | 2,700 | 69 | 26 | Links, brackets, frames |
| Titanium | 4,500 | 110 | 24 | High-value, weight-critical parts |
| Carbon fibre composite | 1,600 | 70–150 | 45–90 | Racing arms, drones |
| PLA (3D printed) | 1,240 | 3.5 | 2.8 | Prototypes, light covers |
| Nylon (3D printed) | 1,140 | 3 | 2.6 | Gears at low load, fixtures |

Read the fourth column carefully, because it is the lesson. Steel and aluminium have almost identical stiffness per kilogram. Aluminium wins in practice not because it is stiffer per kilo but because it is easier to machine into a large tube, does not rust, and is cheaper to buy in the shapes robots need. Carbon fibre is genuinely better per kilogram, which is why it appears in drones and racing machines, and it is expensive, brittle under impact, and difficult to join.

The 3D printed plastics are an order of magnitude worse. That does not make them useless; it makes them suitable for prototypes, covers, fixtures and lightly loaded parts. A student who prints a 400 mm robot arm in PLA and wonders why it chatters has not met a mysterious problem. They have met the table above.

## Mass at the End of the World

There is a rule in machine design that applies to every robot ever built: mass at the end of an arm is ten times more expensive than mass at the base.

The reason is torque. A joint must produce enough torque to hold the weight of everything beyond it, times the distance to that weight, plus the torque needed to accelerate it. Move a 1 kg gripper out by 0.3 m and you have added about 3 N·m of static torque at the wrist, permanently, in every pose. That torque has to come through the gearbox, the motor and the structure, and it appears again as heat.

The practical consequences are everywhere once you look for them. Cables are routed along the structure rather than hanging. The heaviest components — batteries, controllers, pumps — sit near the base. Tooling is made as light as the task allows. A robot that is 20% lighter at the tip can often be 20% faster on the same motors, which is a large commercial advantage for a small mechanical change.

## Problems

1. A link is 0.6 m long, made of aluminium tube with a 40 mm outside diameter and 3 mm wall. Compute its second moment of area and its deflection under a 30 N tip load. Then recompute with a 2 mm wall and say how much stiffness you lost.

2. Using your answer to question 1, estimate the natural frequency with a 1.5 kg mass at the tip. What settling time would you expect if the damping is light?

3. A design uses a solid aluminium bar of 20 mm diameter instead of a tube of the same outside diameter. Which is stiffer, and why? Which is heavier, and by how much per metre?

4. Explain in two sentences why a robot can be repeatable to 0.05 mm and accurate only to 0.5 mm.

5. List four things you would do to reduce the settling time of an arm that rings for 300 ms after every move, in order of cost.
