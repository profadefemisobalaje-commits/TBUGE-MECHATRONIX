# Preface

Software can be wrong and then be fixed. A robot can be wrong once, at 2 m/s, in a room with a person in it, and the mistake is permanent. That asymmetry is what makes this subject different from programming, and it is the reason this volume exists before any of the clever ones.

A robot is a machine that acts. It has a body, which has mass and therefore momentum. It has joints, which bend and wear. It has muscles, which are motors that draw current, heat up and stall. It has senses, which are imperfect instruments that drift in the cold and pick up the hum of a nearby motor. It has a power supply that runs down. And it has a controller that must decide what to do with all of that in a few milliseconds, because the world does not pause while the software thinks.

None of this is background. It is the material. A vision system that finds a cup to a millimetre is useless if the arm cannot hold the cup steady. A planner that computes an elegant path is useless if the wheels slip on a polished floor. Half of the failures in robotics are failures of the body, and half of the rest are failures of the seam between body and code.

This volume is therefore about hardware, but it is written for people who intend to program. It does not assume you have a workshop, a 3D printer or a soldering iron. It assumes you have a pencil and the willingness to compute: torque on an arm, current through a motor, counts from an encoder, the energy in a battery, the time available in a control loop. Those five calculations, done honestly, will let you read a robot's specification sheet and know what it means, and let you design something that will actually work rather than something that looks like it should.

## What you will be able to do

By the end of the volume you will be able to look at a robot — a factory arm, a vacuum cleaner, a drone, a delivery cart — and answer the questions an engineer asks first. How strong is it, and at what reach? How fast, and at what accuracy? What does it sense, and how good are those senses? What happens when it fails, and who is protected when it does? And what would it cost to build, in money and in months?

You will also be able to build a first robot of your own, or at least to specify one precisely enough that somebody else could build it: a list of parts, a wiring plan, a control loop, a test plan and a safety case.

## A note on numbers

Every calculation in this volume uses ordinary units and is worked in full. Torque is in newton-metres, current in amperes, energy in joules and watt-hours, angles in degrees and radians. When a figure depends on an assumption, the assumption is stated. When a figure is a rough rule of thumb rather than a law of physics, it says so.

The arithmetic is deliberately small. You will not need calculus. You will need to multiply, divide, and keep track of units, which is 90% of engineering and 100% of the difference between a design that works and one that quietly destroys itself on the third day.
