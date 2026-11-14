# Building Your First Robot

There is a moment, about three weeks into a first robot, when the parts are all on the bench and nothing works. The motors spin when tested alone; the sensors read sensibly when tested alone; the code runs on the desk. Assembled, the robot twitches, resets, or does nothing at all.

That moment is not a sign of failure. It is the actual work of integration, and the way through it is method rather than inspiration. This chapter is a build procedure: what to write down before you buy anything, in what order to assemble, and how to test so that when something breaks you know which part broke.

## Start With a Brief, Not a Kit

A robot begins as a sentence: *this machine will carry a 2 kg box across a flat floor for 90 minutes, at walking pace, and stop within 10 cm of a marker.*

That sentence contains a task, a payload, a duration, a speed and an accuracy. Each of those numbers will drive a decision later, and a project without them will drift into whatever the parts allow. Write the brief before the shopping list, and keep it where you can see it.

| Requirement | Target | Why it matters |
|---|---|---|
| Payload | 2 kg | Sets motor torque and structure |
| Speed | 1.0 m/s | Sets gearing and control loop rate |
| Runtime | 90 min | Sets battery capacity and mass |
| Stopping accuracy | 0.1 m | Sets sensor choice and control method |
| Floor | Flat, indoor | Rules out suspension and rough-terrain design |
| Budget | Fixed | Forces the trade-offs early |
| Safety | Stops on contact | Sets bumper placement and firmware |

Two of these numbers, speed and runtime, will fight each other through the battery and the motors. A faster robot covers more ground per second and therefore needs more power; a longer runtime needs a bigger battery, which adds mass, which needs more torque, which draws more current, which shortens the runtime. Every mobile robot design is a resolution of that loop, and the resolution is arithmetic, not opinion.

## Choosing the Shape

Three body plans cover most first projects.

A **differential drive** robot has two powered wheels and one or more castors. It can turn in place, it is simple to control, and it is hopeless on rough ground. It is the right choice for a first mobile robot, because the mathematics of its motion is two lines long.

A **four-wheeled** robot is more stable and harder to turn, because the wheels fight each other unless one axle can slip or steer. It is the right choice when stability matters more than manoeuvrability.

An **arm on a base** replaces wheels with joints. It does not go anywhere, and it can do far more interesting things with objects. It is the right choice when the task is manipulation rather than transport.

Whichever you choose, decide early where the heavy parts go. The battery and the electronics belong low and near the centre, because mass high up makes the machine tippy and mass far from the drive wheels reduces grip.

## The Bill of Materials

A bill of materials is a table, and it is the most useful document in the project. Here is an illustrative one for the brief above, with prices that are typical rather than exact.

| Item | Quantity | Unit cost | Notes |
|---|---|---|---|
| Geared motor, 12 V, 200 rpm | 2 | 18 | With encoder if possible |
| Wheel, 100 mm | 2 | 6 | Matches the gearing calculation |
| Castor wheel | 2 | 3 | Low profile |
| Motor driver, dual H-bridge | 1 | 15 | Must handle stall current |
| Microcontroller board | 1 | 12 | Enough pins and a hardware timer |
| Battery, 11.1 V, 5 Ah | 1 | 40 | With management board and fuse |
| Chassis plate | 1 | 20 | Aluminium or plywood |
| Bumper switches | 2 | 3 | Mechanical stop detection |
| Distance sensor | 3 | 12 | Front and sides |
| Fasteners, wire, connectors | — | 25 | Budget more than you think |
| Switch, fuse holder, emergency stop | 1 set | 20 | Do not omit these |

The total is around 220 in the currency of your choice, which is roughly the price of a decent bicycle and about a tenth of a commercial research platform. The proportions matter more than the total: the battery, the motors and the driver are most of the cost, and they are the parts that decide whether the machine works.

## Assembly in Order

Build in the order that lets each stage be tested before the next is added. This is the single most important habit in the chapter.

**Stage 1: the frame.** Assemble the chassis, wheels and castors with no electronics. Push it. Does it roll straight? Does it wobble? Fix it now, when the fix is a drill and not a redesign.

**Stage 2: the motors, on the bench.** Connect one motor to the driver and the driver to a power supply with a current limit. Run it forward, backward, slow, fast. Measure the current at stall with the shaft held. Compare with the datasheet.

**Stage 3: the electronics, unpowered by the motors.** Power the controller alone. Read one sensor. Print its values. Then read all sensors and check for plausible numbers, not just numbers.

**Stage 4: the drivetrain under load.** Put the robot on blocks so the wheels spin free, then on the floor. Command a slow forward motion for one second. Measure how far it actually went, and compare with the prediction from the chapter on open loop.

**Stage 5: behaviour.** Add the first feedback loop. Tune the gain on a smooth floor before trying carpet.

**Stage 6: the safety layer.** Add the bumpers, the stop button and the current limits. Test them by deliberately triggering each one, and confirm that the robot stops.

Each stage ends with a test whose failure is informative. A robot assembled in one go and switched on has a single symptom — "it does not work" — and no way to narrow it down.

## When It Misbehaves

Integration faults have a small number of usual suspects, and the order of checking saves hours.

**Power.** Measure the battery voltage under load, not at rest. A pack that reads 12.4 V with no load may read 10.1 V when the motors start, which is below the controller's minimum.

**Grounds.** Check that every component shares a single ground point. A missing ground produces signals that wander; two grounds produce loops that hum.

**Connectors.** Wiggle every connector while the robot is running. Intermittent faults live here, especially after the robot has driven over a bump.

**Noise.** Does the fault appear only when the motors run? If so, it is electrical noise, and the fixes are physical: separate the wires, add capacitance, twist the signal pair.

**Logic.** Only after the four above should you suspect the code. Software is easier to inspect than a loose crimp, which is precisely why people inspect it first and find nothing.

## Document While You Build

A robot without documentation is a robot that cannot be repaired, and a project report without measurements is an essay. Keep three things as you go.

A **log**, one line per test: date, what you changed, what happened, what you measured. It takes a minute and saves a week.

A **wiring diagram**, drawn by hand and kept next to the machine. The version in your head will not survive a week.

A **bill of materials with the actual parts**, including the ones you substituted, because the substitute is what is in the machine.

Add version control for the code, even if you are working alone. The ability to return to the version that worked yesterday is worth more than any clever feature you might add today.

## Problems

1. Write a one-sentence brief for a robot you would like to build, containing a task, a payload, a speed, a duration and an accuracy.

2. Derive the motor torque needed for your brief. Show the mass, the distance and the acceleration you assumed.

3. Estimate the battery capacity your brief requires, using the runtime and an average current you justify.

4. List the six assembly stages for your robot and the test that ends each one.

5. Your robot resets when it drives forward. Write the four checks you would perform, in order, and what result would confirm each cause.
