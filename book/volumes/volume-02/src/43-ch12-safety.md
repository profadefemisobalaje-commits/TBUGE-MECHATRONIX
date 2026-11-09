# When Robots Hurt People

On 25 January 1979, at a Ford casting plant in Flat Rock, Michigan, a worker named Robert Williams climbed into a storage rack to retrieve parts. A robot arm on the other side of the rack continued its programmed motion and struck him. He died later that day. It was the first recorded death caused by an industrial robot in the United States, and the details are more instructive than the headline: the machine was doing exactly what it had been built to do, in a place where a person had no way to tell it that someone was there.

Two years later, in Akashi, Japan, a maintenance worker named Kenji Urada was killed at a Kawasaki Heavy Industries plant. He had climbed over a fence to work on a robot without switching it off completely. The machine's hydraulic arm pushed him into an adjacent grinding machine.

Neither accident involved a malfunctioning robot. Both involved a person inside the working envelope of a machine that had no way to know, and a set of procedures that allowed the situation to arise. That pattern has not changed in forty-five years, and it is the reason this chapter is not an appendix.

## How Machines Fail

Before designing a guard, it helps to know what is being guarded against. Robot failures fall into five groups, and the groups have different characters.

**Mechanical failures** are broken parts: a fatigued bracket, a sheared key, a bearing that seizes, a bolt that vibrates loose. They are usually preceded by warning signs — noise, heat, vibration — and they are usually found by inspection rather than by software.

**Electrical failures** are shorts, opens, insulation breakdowns and connector faults. Vibration is the great enemy of connectors, and the machine that works on the bench and fails on the floor often has a connector that half-disconnects when the wheel hits a bump.

**Software failures** are logic errors, race conditions, unbounded loops and unhandled states. They are the most discussed and the least common cause of injury, because most injuries require a physical energy source and the software is usually not one.

**Sensing failures** are the dangerous middle ground. A sensor that reports stale data, an encoder that misses counts, a camera blinded by the sun. The machine believes something false and acts confidently on it.

**Human failures** are the largest category in practice: someone reaches past a guard, forgets to lock out power, presses the wrong button, or trusts the machine's confidence more than their own eyes.

The engineering response differs by category. Mechanical and electrical failures are prevented by design margins and inspection. Sensing failures are prevented by redundancy and plausibility checks. Human failures are prevented by design as well, because the best way to stop someone defeating a guard is to make the guard unnecessary.

## Risk, in Two Numbers

A **risk assessment** is a structured way of asking what could go wrong, how bad it would be, and how likely it is. The simplest useful version scores each hazard on two scales and multiplies them.

| Hazard | Severity (1–5) | Likelihood (1–5) | Risk score |
|---|---|---|---|
| Arm strikes a person during normal cycle | 5 | 2 | 10 |
| Pinch point at the gripper | 3 | 4 | 12 |
| Hot motor surface touched during maintenance | 2 | 3 | 6 |
| Robot drives off a mezzanine edge | 5 | 1 | 5 |
| Cable trip hazard around the cell | 2 | 5 | 10 |

The scores are not physics; they are a disciplined conversation. What they buy is a ranking, which tells you where to spend the effort, and a record, which tells a regulator, an insurer and a court that the conversation happened.

Two things are worth noticing about the table. First, the highest score is not the most dramatic hazard: the pinch point at the gripper outranks the arm strike because it is far more likely. Second, the edge hazard has the highest severity and the lowest likelihood, which is characteristic of the failures that kill people: rare, and fatal.

## The Order of Controls

Engineers have a hierarchy of ways to make a machine safe, and the order matters. Each step is more reliable than the one below it.

**Eliminate the hazard.** Design the machine so the dangerous thing cannot happen. A robot that carries the part on a conveyor instead of reaching into a press has removed a hazard rather than guarded it.

**Guard it.** Put a physical barrier between the person and the energy. A fence around a welding cell is crude, cheap and extremely effective.

**Interlock it.** Make the machine stop or slow when a person is detected. A light curtain, a pressure mat, a scanner. An interlock is a guard with a sensor, and it is only as good as the sensor.

**Warn.** Lights, sirens, floor markings, signs. Warnings are the weakest control, because they depend on attention, and attention is exactly what a tired worker at the end of a shift has least of.

**Train and instruct.** Procedures, permits, lockout-tagout. Necessary, and insufficient alone, as both the 1979 and 1981 deaths demonstrate.

**Personal protective equipment.** The last line, and the least reliable, because it protects only the person wearing it and only if it fits.

A design that relies on the bottom three while calling itself safe is a design that has moved the risk onto the person least able to bear it.

## What a Real Safety System Contains

A modern industrial robot cell has several independent layers, and each one is designed to work when the others fail.

The **emergency stop** cuts power to the actuators through a contactor, not through software. It is latching, so that restarting is deliberate, and it is placed where a person would naturally reach.

The **enabling device** is the dead-man switch held by a programmer inside the cell. Release it, and the robot stops. It is how a person is allowed to be near a moving machine at all.

The **light curtain** or **scanner** detects an intrusion and stops or slows the machine before contact. Its resolution determines the smallest object it can detect, and therefore the minimum safety distance.

The **speed and separation monitor** is the modern refinement used in collaborative cells: instead of stopping, the robot slows as a person approaches, keeping a calculated minimum distance. It requires reliable human detection, and its safety depends entirely on the perception system.

The **mechanical brake** holds the arm when power is removed, so that gravity does not finish what the fault started.

The **force and torque limit** in a collaborative robot stops the motion when contact produces a force above a threshold. It is the last layer, and it is designed to make the residual injury minor rather than fatal.

The relevant standards are worth knowing by name even if you never read them in full. ISO 10218 covers industrial robots and their integration. ISO/TS 15066 covers collaborative operation and sets out force and pressure limits for contact with different parts of the body. ISO 13849 defines performance levels for safety-related control systems, from PLa to PLe. IEC 61508 defines safety integrity levels for electrical and electronic systems. These are not formalities; they encode decades of accidents.

## Human Factors

The hardest safety problem is not the machine. It is the person who has been asked to watch it.

Vigilance does not survive boredom. A supervisor asked to watch an autonomous vehicle for hours will look away, and the more reliable the vehicle, the more often they will look away. This is not a moral failing; it is a well-documented property of human attention, and it is why the Tempe crash in 2018 happened with a safety driver who was not looking at the road.

**Automation bias** is the tendency to trust the machine's judgement over your own, especially when it is usually right. A surgeon who has seen the robot be correct a thousand times will hesitate before overriding it on the thousand-and-first, and the hesitation is the accident.

**Mode confusion** is the third. A machine that behaves differently in automatic and manual modes, with no clear indication of which mode it is in, will eventually be operated in the wrong one. The fix is design: unambiguous state indication, and controls that are physically different for different modes.

None of these are solved by better software. They are solved by designing the human's job so that it is possible to do it well.

## Problems

1. Take the risk table above and add three hazards from a robot you have seen or used. Score them and re-order the list.

2. A light curtain has a response time of 20 ms, and the robot takes 200 ms to stop from full speed. If the robot moves at 1.5 m/s, what is the minimum safety distance?

3. Explain in three sentences why an emergency stop should cut power through a contactor rather than ask the software to stop.

4. A collaborative robot is rated for a maximum contact force of 140 N. What could make that rating meaningless in a real installation, and what would you check?

5. Describe one task in which a human supervisor is asked to monitor a machine for long periods. What would you change about the task to make vigilance realistic?
