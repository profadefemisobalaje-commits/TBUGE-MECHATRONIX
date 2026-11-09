# Sensors: Turning the World into Numbers

A robot knows nothing except what its instruments tell it, and every instrument lies a little. A wheel encoder under-reports when the wheel slips. A distance sensor reports the nearest reflective surface, which may be a chair leg or a hanging coat rather than a wall. A gyroscope accumulates a small error into a large one. The skill of sensing is not finding an instrument that is always right; it is knowing how each one is wrong, and by how much.

## Four Questions About Any Sensor

Specifications are written in a private language, and four words in that language decide whether a sensor is suitable.

**Range.** The span of values it can measure. A distance sensor that works from 0.2 m to 4 m is blind to a wall at 10 cm, which matters when the robot is parking.

**Resolution.** The smallest change it can report. A 12-bit encoder gives 4,096 counts, so its resolution is one part in 4,096, whatever the physical quantity.

**Accuracy.** How close the reported value is to the truth. A sensor can have fine resolution and poor accuracy: it reports 1.002, 1.004, 1.006 when the truth is 1.010. The numbers are precise and the answer is wrong.

**Drift.** How much the error changes over time and temperature. A cheap gyroscope may drift by 0.1 degrees per second, which is 6 degrees a minute and 360 degrees an hour. On a robot that integrates that signal to estimate heading, drift is not a curiosity; it is the whole problem.

There are two more properties that never appear on the datasheet and always appear in practice: **latency**, the delay between the event and the report, and **failure behaviour**, what the sensor outputs when it is broken. A sensor that fails to zero is very different from one that fails to its last value, and a robot that cannot tell the difference will happily drive on a frozen reading.

## Measuring the Robot Itself

Most robot control depends on knowing the position of its own joints, and three devices do that work.

A **potentiometer** is a variable resistor that reports angle as a voltage. It is cheap, simple, and wears out, because a wiper slides on a track millions of times. It is fine for a hobby arm and unacceptable for a machine that must run for years.

An **incremental encoder** produces pulses as a disc with slots turns between a light and a sensor. Two channels, offset by a quarter of a slot, allow the controller to know both the amount and the direction of rotation. It has no absolute reference: after a power cycle it knows how far it has moved, not where it is.

An **absolute encoder** reports the full angle at every reading, using a coded disc or a magnetic pattern. It costs more and removes the need to home the joint at start-up, which is why industrial robots use them.

The arithmetic is worth doing once. An encoder with 1,000 cycles per revolution, read in quadrature, gives 4,000 counts per revolution. On a wheel of 50 mm radius, the circumference is 2π × 0.05 = 0.314 m, so each count is 0.314 / 4,000 = 0.0785 mm of travel. That is the finest distance the robot can resolve from its wheels — and only if the wheel does not slip.

## Measuring the World

The instruments that look outward are more varied, and each has a characteristic failure.

An **ultrasonic rangefinder** emits a burst of sound at about 40 kHz and times the echo. The distance is the speed of sound times the time, divided by two, because the pulse travels out and back. At 343 m/s, a wall at 1 m produces an echo after 5.8 ms. Soft surfaces absorb the sound and disappear; angled surfaces reflect it away; two robots using the same frequency interfere with each other.

An **infrared proximity sensor** measures reflected light. It is cheap, fast and fooled by colour: a black surface returns almost nothing, and a white one at the same distance looks close. It is a good cliff detector and a poor distance meter.

A **laser scanner**, or lidar, sweeps a beam and measures time of flight or phase. It gives thousands of accurate ranges per second over a wide angle, which is why it is the backbone of mobile robot navigation. It is expensive, it dislikes rain and dust, and a black or mirrored surface can vanish.

A **camera** measures light, and everything else is inference. Its great strength is that it captures a whole scene at once; its weakness is that the mapping from pixels to metres requires calibration, and the calibration drifts when the lens is knocked.

A **force or torque sensor** measures the mechanical interaction, which is essential for any task where contact is the point: assembly, polishing, handover to a person. A **microswitch** is the crudest force sensor and remains the most reliable: it reports contact, and it does so for a few cents.

| Sensor | Measures | Typical resolution | Characteristic failure |
|---|---|---|---|
| Incremental encoder | Rotation | 0.09° at 4,000 counts | Loses position at power-off |
| Potentiometer | Angle | 0.5° | Wear, noise, limited life |
| Ultrasonic | Distance | 5 mm | Soft or angled surfaces |
| Infrared proximity | Presence, rough distance | Not a distance | Surface colour |
| Lidar | Distance, many points | 10–30 mm | Rain, dust, black surfaces |
| Camera | Light | Depends on calibration | Lighting change, motion blur |
| IMU | Acceleration, rotation rate | Fine, but drifting | Bias drift over time |

## The Instrument That Forgets

The inertial measurement unit deserves a section of its own, because it is the clearest example of a sensor whose errors compound.

An IMU contains accelerometers that measure acceleration and gyroscopes that measure angular rate. To get orientation, you integrate the rate: angle is the sum of rate multiplied by time. To get position, you integrate acceleration twice.

Each integration turns a small error into a large one. A gyroscope with a bias of 0.1 degrees per second accumulates 6 degrees a minute. An accelerometer with a bias of 0.01 m/s² produces a velocity error of 0.01 m/s after a second, a position error of 5 mm after one second, and 1.8 m after a minute, before any vibration is counted.

This is why no serious robot navigates on inertial data alone. The IMU is fast, smooth and locally accurate, and it is combined with a slower absolute reference — wheels, a laser scan, a camera, a satellite fix — so that the drift is corrected before it grows. That combination is the subject of the volumes on perception and localisation, and the arithmetic you have just done is the reason they exist.

## Problems

1. An encoder gives 2,000 counts per revolution. A wheel of 80 mm radius is attached. How far does the robot move per count?

2. An ultrasonic sensor measures an echo after 11.6 ms. How far away is the surface? What would the reading be if the surface were a curtain?

3. A gyroscope drifts by 0.05 degrees per second. How much heading error accumulates in 5 minutes? What would you add to the robot to correct it?

4. A camera is knocked sideways by 2 mm. Explain in two sentences why the robot's grasp may now miss by more than 2 mm.

5. Choose a sensor for each of these tasks and say what would make it fail: detecting a table edge, measuring the force of a gripper, finding a person in a corridor, knowing how far a wheel has turned.
