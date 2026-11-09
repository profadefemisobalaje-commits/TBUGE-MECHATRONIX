# Electronics and Motor Drivers

A microcontroller is a small computer with pins. Some pins listen, some pins talk, and some pins can turn a voltage on and off. None of them can drive a motor, and the first lesson of robot electronics is understanding exactly why.

A typical microcontroller pin can supply about 20 milliamps. A small robot motor needs 2 amps, and a larger one needs 20. The ratio is a hundred to a thousand, and the gap is bridged by a driver: a component whose job is to take a small, polite signal and use it to switch a large, rude current.

## Sensors In, Power Out

The architecture of almost every small robot is the same. Sensors produce voltages that the microcontroller reads. The microcontroller computes. It sends low-power commands to drivers. The drivers switch power from the battery to the motors. Anything else — displays, radios, extra memory — hangs off the same pattern.

This separation exists for three reasons. The microcontroller is fragile and expensive; the driver is robust and cheap, and it is the part you want to fail. The motor generates electrical noise that would destroy a processor sharing its supply. And the current paths are different: signals flow in milliamps along thin wires, power flows in amps along thick ones, and mixing the two produces a machine that resets whenever it drives forward.

The last of these is worth a sentence of its own. A robot whose controller reboots when the motors start is not haunted. It has a wiring problem: the motor's current pulse is dropping the supply voltage below the controller's minimum, or the noise is coupling into a signal line. The fix is layout and capacitance, not software.

## The H-Bridge

A direct-current motor turns one way when voltage is applied one way and the other way when the polarity is reversed. To reverse it under software control, you need four switches arranged around the motor, and that arrangement is called an **H-bridge**.

Label the switches top-left and bottom-left, top-right and bottom-right. Close top-left and bottom-right: current flows one way and the motor turns forward. Close the other diagonal: it turns backward. Close both bottom switches: the motor is shorted across itself and brakes hard.

There is one combination that must never happen: both switches on the same side closed at once, which connects the supply directly to ground through two transistors. This is called **shoot-through**, and it destroys drivers in microseconds. Every competent driver includes a small delay, called dead time, to make shoot-through impossible even if the software makes a mistake.

The H-bridge is a good example of a general principle in this volume: the electronics exist to make the software's mistakes survivable. A microcontroller that asks for an impossible combination should get a safe outcome, not a fire.

## PWM and the Average Voltage

A digital output has two states: on and off. A motor wants a smooth, adjustable voltage. The trick that bridges them is **pulse width modulation**, which switches the output on and off very fast and relies on the motor's own inertia to smooth the result.

If a 12 V supply is switched on for 30% of each cycle and off for 70%, the motor sees an average of 3.6 V. Change the duty cycle to 80% and it sees 9.6 V. The switching frequency is typically 10 to 30 kHz, above the range that produces audible whine, and the motor's inductance keeps the current continuous.

Two numbers matter in practice. The **frequency** must be high enough to keep the current smooth, and low enough that switching losses in the driver stay small. The **resolution** of the duty cycle sets how finely the speed can be controlled: 8-bit control gives 256 levels, which on a 24 V system is a step of about 94 mV.

PWM is used for more than motors. Heating elements, lights, fans, solenoid valves and even some sensors are driven this way. Whenever you see a digital system controlling a continuous quantity cheaply, PWM is usually underneath.

## Current Sensing and Motor Protection

A driver that cannot measure current cannot protect anything. Two methods are common.

A **shunt resistor** in the current path produces a small voltage proportional to the current. A 10 milliohm shunt carrying 10 A drops 0.1 V, which is easy to measure and costs 1 W of heat.

**Hall sensors** measure the magnetic field produced by the current and need no shunt, at higher cost.

With current measurement, the driver can implement a **current limit**: when the measured current exceeds a threshold, reduce the duty cycle or switch off for the rest of the cycle. This is what saves a motor when the arm jams against a table. It is also what allows a collaborative robot to detect a human contact: the sudden rise in current, filtered and interpreted, is the signal that something unexpected has happened.

The limit must be set from the motor's ratings, not from the driver's capability. A driver that can pass 40 A will happily pass 40 A into a motor rated for 5 A until the winding fails.

## The Microcontroller's Real Constraints

Three properties of small computers shape what a robot can do, and they are worth stating plainly because they surprise people who have only written desktop software.

**Time is not guaranteed.** A desktop operating system schedules tasks when it feels like it. A microcontroller running a bare-metal loop executes your code in order, which is predictable, but any interrupt can delay the main loop. If a control loop must run every 1 ms, the designer must account for the worst case, not the average.

**Analogue inputs are coarse.** A typical 10-bit analogue-to-digital converter divides a 5 V range into 1,024 steps, which is about 4.9 mV per step. A sensor with a 0.01 V signal change per degree can therefore resolve about two degrees, no matter how good the sensor is.

**Memory is small.** A microcontroller with 32 kB of program memory cannot hold a camera image, a map, or a neural network of any size. Those functions move to a more capable computer, and the two communicate, which introduces the latency and failure modes of a network link inside the robot.

## A Wiring Plan That Survives

Most faults in a small robot are wiring faults, and most wiring faults come from decisions made in a hurry. A plan drawn before the first crimp prevents them.

**Separate the two worlds.** Power wiring — battery, switch, fuse, drivers, motors — runs on one side of the machine in thick wire. Signal wiring — sensors, encoders, communication — runs on the other side in thin wire. Where they must cross, they cross at right angles.

**Ground at one point.** The battery negative is the star point. Every return connects to it directly, or through a bus bar near it. Daisy-chaining grounds through several boards puts the motor current through the sensor's reference, and the result is a reading that changes whenever the robot accelerates.

**Fuse every branch.** The main fuse protects the battery and the harness; each driver branch has its own fuse sized to the wire, not to the motor's peak current. A 5 A branch on 0.5 mm² wire is sensible; a 20 A fuse on the same wire is a fire.

**Strain-relieve everything.** Every wire that leaves a connector should be supported within 50 mm, so that vibration is taken by the support rather than the crimp. A robot that fails after a week usually fails at a connector that was flexed a thousand times.

**Label both ends.** A strip of tape with a number, written at both ends of every wire, saves an hour every time something goes wrong. It costs ten minutes.

| Wire colour | Use |
|---|---|
| Red | Positive supply, after the switch |
| Black | Ground return |
| Yellow | Motor phase A |
| Blue | Motor phase B |
| Green | Sensor signal |
| White | Communication |

The colours are a convention, not a standard, and any convention is better than none. The machine you repair at midnight will be the machine you wired at noon, and you will not remember which black wire was which.

## Problems

1. A 24 V supply drives a motor through PWM at 25% duty. What average voltage does the motor see? What average voltage at 90%?

2. A 10 milliohm shunt carries 8 A. What voltage appears across it, and how much power does it dissipate?

3. A 10-bit analogue-to-digital converter measures 0 to 5 V. How many volts per step? A temperature sensor produces 10 mV per degree; what is the smallest temperature change the system can resolve?

4. Explain in two sentences why an H-bridge needs dead time, and what happens without it.

5. A controller resets whenever the drive motors start. List three likely causes in order of probability, and the test that would distinguish them.
