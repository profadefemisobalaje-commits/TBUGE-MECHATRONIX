# Open Loop: Doing What You Are Told

The simplest robot does not check. It is told to turn the wheel for two seconds, and it turns the wheel for two seconds. Whether the robot has moved one metre or ninety centimetres, the program does not know and does not care.

This is **open-loop** control, and it is the right place to begin, for a reason that has nothing to do with simplicity. Open loop exposes the physics. When a machine driven by a fixed command consistently ends up 8 cm short, you have learned something concrete about friction, load or battery voltage. When the same machine is wrapped in feedback, that knowledge hides inside the correction, and the underlying problem stays in the machine, waiting to reappear when the battery is low.

## The Command and the Consequence

Open-loop control has three parts: a trajectory of commands, a timing, and a hope.

For a wheeled robot, the command might be "left motor 60% forward, right motor 60% forward, for 2.0 s". If the wheel radius is 50 mm, one revolution covers 314 mm, and at 60% duty on a 12 V motor with a no-load speed of 300 revolutions per minute, the wheel turns at roughly 180 revolutions per minute, or 3 revolutions per second. Two seconds gives six revolutions, which is 1.88 m.

That number is a prediction, not a measurement. It assumes the motor's speed is proportional to duty cycle, that the floor is flat, that the wheels do not slip, that the battery is at 12 V, and that the robot's mass has not changed. Each assumption is slightly false, and the errors add.

| Assumption | Typical error |
|---|---|
| Speed proportional to duty | 5–10% over the range |
| No wheel slip | 1–5% on a hard floor, far more on carpet |
| Battery at nominal voltage | 10% drop from full to empty |
| Constant load | Varies with floor and payload |

Multiply those errors and a robot commanded to travel 2 m may travel 1.75 m or 2.15 m. Neither is catastrophic, and both are enough to miss a docking station.

## Dead Reckoning, and How It Drifts

A slightly better open-loop machine measures its own wheels with encoders and integrates. This is **dead reckoning**: if the wheels turned this much and did not slip, the robot moved this far.

For a two-wheeled robot, the arithmetic is small. Let the wheel radius be r, the distance between wheels b, and let each wheel's encoder count give its travel, s_left and s_right. Then

> distance travelled = (s_left + s_right) / 2
>
> change in heading = (s_right − s_left) / b

Take a robot with r = 0.05 m, b = 0.3 m, and 4,000 counts per revolution. The left wheel travels 1.000 m and the right 1.030 m over a straight-line command.

The centre moves (1.000 + 1.030)/2 = 1.015 m, and the heading changes by (1.030 − 1.000)/0.3 = 0.1 rad, or 5.7 degrees. The robot intended to go straight and has turned slightly, because one wheel ran faster.

Over a long run, this error compounds. A 2% difference between the wheels means that after 10 m the heading is off by 0.2 rad, about 11 degrees, and the robot is 1 m away from where it thinks it is. Add wheel slip, and the number gets worse quickly. This is why no mobile robot relies on dead reckoning alone, and why the volumes on localisation exist.

## Profiles: Not All Commands Are Steps

Telling a motor to go from zero to full speed instantly is a bad idea, for the same reason that stamping on a car accelerator is. The mechanism must accelerate its own mass, the gears take a shock, and the structure rings.

The standard solution is a **motion profile**: a smooth change from one velocity to another. The simplest is the trapezoid — accelerate at a constant rate, cruise at a maximum speed, decelerate at the same rate.

Work an example for an arm joint that must move 1.0 rad. It accelerates at 2 rad/s², cruises at 1 rad/s, and decelerates at 2 rad/s².

The acceleration phase takes 0.5 s and covers 0.25 rad. The deceleration phase takes 0.5 s and covers 0.25 rad. The remaining 0.5 rad is covered at 1 rad/s, which takes 0.5 s. Total: 1.5 s, and the joint arrives with zero velocity and zero acceleration.

Without the profile — a step command — the joint would demand infinite acceleration, which the motor cannot supply, so it would saturate, lag, overshoot and ring. The profile does not make the machine faster. It makes the machine arrive where it was aimed.

## Calibrating the Command

A command that is roughly right can be made accurate with a ruler and ten minutes, and the procedure is worth knowing because it converts an open-loop machine from a toy into an instrument.

Run the robot forward at 40% duty for exactly 2.0 s, ten times, and measure the distance travelled each time on a hard floor. Suppose the results are 0.94, 0.96, 0.93, 0.97, 0.95, 0.96, 0.94, 0.98, 0.95 and 0.94 m.

The mean is 0.952 m, and the spread from lowest to highest is 0.05 m, about 5%. Two numbers come out of this.

The **scale factor** is the true distance divided by the predicted distance. If the model predicted 1.00 m, the factor is 0.952, so the controller multiplies every commanded duration by 1.05 to correct it. The robot now travels where it is told on that floor, at that battery level, with that payload.

The **spread** is the honest limit of the method. A 5% variation means that repeating the same command puts the robot anywhere within a 5 cm band per metre. For docking to a charger that tolerance may be enough; for placing a part it is not, and no calibration can fix it because the variation is not a constant offset. It is friction, carpet, battery sag and wheel slip changing from run to run.

Two refinements improve the result without adding a sensor. Compensate for battery voltage: measure the pack at the start of each run, and scale the command by the nominal voltage divided by the measured voltage. And calibrate at the temperature and load you will actually use, because a machine calibrated cold and light will overshoot when it is warm and loaded.

| Trial | Distance (m) |
|---|---|
| 1 | 0.94 |
| 2 | 0.96 |
| 3 | 0.93 |
| 4 | 0.97 |
| 5 | 0.95 |
| 6 | 0.96 |
| 7 | 0.94 |
| 8 | 0.98 |
| 9 | 0.95 |
| 10 | 0.94 |

The discipline here is the same one that appears in every volume of this series. Measure ten times, keep the mean and the spread, correct the systematic part, and state the random part honestly. A robot specification that says "accurate to 2%" without saying over what distance and on what floor is not a specification.

## When Open Loop Is Enough

It would be a mistake to treat open-loop control as a beginner's technique to be outgrown. Several important machines use it deliberately.

A **stepper-driven axis** moves a fixed increment per pulse and is designed to hold that assumption. With a homing routine at start-up, it is accurate enough for 3D printers and pick-and-place machines, at a fraction of the cost of a servo axis.

A **fixtured industrial task** — welding, painting, screwdriving — happens in a world that has been built to be predictable. The part is clamped, the robot is bolted down, and the trajectory is repeated thousands of times. Feedback on the tool position would add cost without adding value, so the machine is open-loop in position and closed-loop only in the motor's own commutation.

A **conveyor or lift** moves between two limit switches, and the switches are the feedback. The motion between them is open loop, and it does not matter, because the endpoints are certain.

The engineering rule is: use open loop where the world is constrained and feedback where it is not. Then measure. A machine that is open loop and repeats to 0.1 mm is a better machine than one that is closed loop and argues with itself.

## Problems

1. A robot with 50 mm wheels is commanded at 50% duty for 3 s. Assuming a no-load speed of 240 revolutions per minute at full duty and no slip, how far does it travel? What would you guess the real distance to be?

2. A two-wheeled robot has wheels 0.25 m apart and encoders giving 2,000 counts per revolution on 60 mm wheels. The left wheel records 1,200 counts and the right 1,260. Compute the distance travelled and the change in heading.

3. A robot's wheels differ in effective diameter by 1.5%. After travelling 20 m in a straight line, how far off course is it? Is that acceptable for a warehouse aisle 3 m wide?

4. Design a trapezoidal profile for a joint moving 2.0 rad, with a maximum speed of 1.5 rad/s and acceleration of 3 rad/s². How long does the move take?

5. Name one task in your own environment where open-loop control would be adequate, and one where it would fail badly. Explain the difference in terms of how predictable the world is.
