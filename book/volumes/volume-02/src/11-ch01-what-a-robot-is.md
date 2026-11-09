# The Machine That Acts

In 1961, a two-tonne arm was bolted to the floor of a General Motors plant in Trenton, New Jersey, and set to work lifting hot metal castings out of a die-casting machine. It did nothing clever. It moved through a sequence of positions recorded by a human operator, over and over, for years. It was called Unimate, and it was the first industrial robot.

Visitors found it disappointing. It had no eyes, no hands in any useful sense, and no idea what it was holding. It simply repeated a motion, and in doing so it removed a man from a job that was hot, dangerous and dull. That is the pattern the industry has followed ever since: the first successful robots were not intelligent, they were useful.

This volume is about the machine that made that possible, and about the same machine, sixty years later, carrying surgical instruments and driving across warehouses. The principles have not changed much. The parts have become smaller, cheaper and vastly more precise.

## Five Things a Robot Must Have

Definitions of "robot" are a small industry of their own, and most of them are either too broad to be useful or too narrow to survive the next product launch. Here is a working definition, with five tests that a machine can pass or fail.

A robot has a **body** that exists in the physical world. It occupies space, has mass, and cannot be in two places at once. This sounds trivial until you compare it with a program, which can be copied a million times and run in parallel without collision.

It has **sensors** that measure something about itself or its surroundings. Even Unimate had limit switches and encoders, though no one would call them senses in the human meaning of the word.

It has **actuators** that change the world: motors, valves, heaters, speakers.

It has a **controller** that decides, from the sensor readings, what the actuators should do. The decision may be a fixed sequence, a feedback law, or a learned policy. The complexity of the decision is not part of the definition.

And it is **programmable**: the behaviour can be changed without rebuilding the machine. A washing machine has a body, sensors, actuators and a controller, and it fails this test. Its cycle is fixed in the design, and to change it you change the product. A robot arm can be taught a new task in an afternoon, which is why the same hardware can weld a car and pack biscuits.

| Test | Unimate (1961) | Washing machine | Humanoid research platform |
|---|---|---|---|
| Body in the world | Yes | Yes | Yes |
| Sensors | Limit switches, encoders | Temperature, level, door | Cameras, IMU, force, joint encoders |
| Actuators | Hydraulic joints | Motor, pump, valve | Electric joints, hands |
| Controller | Sequence and limits | Fixed cycle | Many, layered |
| Programmable | Yes | No | Yes |

## The Loop, With Physics Attached

Volume One drew the agent as a loop: sense, decide, act. Here the same loop has consequences that software does not have, and three of them shape every design decision in this volume.

**The loop takes time.** A sensor reading is not instantaneous, a computation takes milliseconds, an actuator takes time to move, and the world changes while all of this happens. A robot driving at 1.5 m/s covers 15 mm in 10 ms. If the total delay from sensing to action is 50 ms, the machine is reacting to a world that is 75 mm out of date. At walking pace that is harmless. At running pace it is the difference between stopping and falling.

**Mistakes are irreversible.** A program that writes the wrong file can be rerun. An arm that drives into a fixture at full torque has bent something, possibly the fixture and possibly a person. This is why the vocabulary of robotics is full of words that software engineering does not use: stall, backlash, backdrive, compliance, factor of safety.

**Energy has to come from somewhere.** Every action consumes power, generates heat, and wears a part. A robot that runs for eight hours must carry eight hours of energy or collect it from a cable. A motor that produces the torque you asked for will get hot doing it, and a gearbox that transmits that torque will wear.

These three facts explain why robot design is a negotiation rather than an optimisation. You want it strong, fast, precise, cheap, light and safe. You can have four of those, and the choice of which four is the engineering.

## How Much Freedom, How Much Help

A useful way to sort robots is by how much of the decision is theirs.

A **teleoperated** machine does what a human tells it, continuously. A surgical robot, a bomb-disposal vehicle, a drone under manual control. The human supplies the intelligence and the machine supplies precision, reach or safety.

A **semi-autonomous** machine takes instructions at a higher level and works out the details. "Go to bay 7 and pick up the pallet" is a task; the machine decides the route, the speed and the grasp. Most useful field robots are here, and this is where the interesting engineering lives, because the human and the machine must share a model of what is happening.

An **autonomous** machine is given a goal and no further help. A vacuum robot, a warehouse shuttle, an agricultural sprayer on a known field. Autonomy is narrow by nature: these machines are autonomous within a defined world, and they fail at its edges, which is why the volumes on perception, localisation and planning exist.

The categories are not a ladder of virtue. A teleoperated surgical robot is better than an autonomous one would be, because the surgeon's judgement is the point. The question is always which decisions should be delegated, and the answer depends on what happens when the machine gets it wrong.

## Three Questions for Any Body

When you meet a new robot, ask three questions. The answers describe the machine more completely than any marketing page.

**How strong is it, and at what distance?** Strength in a robot is torque at a joint, or force at a tool, and it depends on reach. An arm that lifts 20 kg close to its base may lift 8 kg at full extension, because torque is force times distance. The specification sheet that lists a single payload figure is telling you the best case.

**How precise is it, and at what speed?** Precision costs money and speed costs precision. A machine that positions to 0.02 mm will do so slowly, after settling. A machine that moves fast will overshoot, vibrate and settle late. The two figures together, with the settling time, describe the machine.

**What happens when it fails?** A robot with a brake that holds the arm when power is lost is a different product from one that drops it. A robot with a force limit that stops it when it touches a person is a different product again. The failure mode is a design feature, and it is chosen either deliberately or by accident.

## A Family Portrait

Robots come in a small number of body plans, and each plan solves a different geometry problem.

The **industrial arm** is a chain of rigid links on a fixed base, usually six joints, designed for repeatability rather than for moving around. It is the workhorse: welding, painting, picking, packing. It is fast, accurate, and dangerous to be near when running, which is why it lives behind a fence.

The **mobile robot** moves its base. Wheels on a flat floor, tracks on rough ground, legs where wheels cannot go. Its hard problems are localisation and perception rather than reach, and it usually carries less payload than an arm because it must carry its own power.

The **drone** flies, which means it must control its orientation continuously or fall. This makes its control loop fast and its endurance short: most multirotors fly for twenty to forty minutes, and every gram of payload costs minutes.

The **humanoid** copies a body plan that evolved for climbing trees and throwing things. It is the hardest platform in the field, because balance is a continuous negotiation with gravity, and it is pursued because the world is built for human shapes: stairs, doors, tools, shelves.

The **collaborative arm** is a small industrial arm designed to work beside people without a fence, using force limits, rounded shapes and sensors that stop it on contact. It trades speed for safety, and it changed the economics of small-batch manufacturing.

Each family has its own arithmetic. Part Two of this volume gives you the arithmetic for all of them.

## Problems

1. Take the five tests above and apply them to three machines you can name: a lift, a self-driving car, a robot vacuum. For each, decide whether it passes each test and write one sentence of justification.

2. A robot moves at 2 m/s. Its sensor takes 20 ms to produce a reading, its controller takes 10 ms, and its motor takes 30 ms to respond. How far does the robot travel between the moment the world changes and the moment its action reflects that change?

3. A specification sheet says an arm has a payload of 12 kg and a reach of 1.4 m. Write the two questions you would ask before believing that the arm can lift 12 kg at 1.4 m.

4. Think of a machine that is automatic but not programmable, and one that is programmable but not mobile. Explain in one sentence each why the distinction matters for the people who use them.
