# Closing the Loop: Simple Behaviours That Survive

A robot that checks its own result can survive a world it did not predict. The battery sags, the floor changes, a book is left on the carpet; the machine notices that it is not where it intended to be and corrects. This is **feedback**, and it is the difference between a machine that works in a laboratory and one that works on a Tuesday.

The mathematics of feedback fills several volumes. What follows is the smallest useful version: three behaviours you can build with one sensor, one motor and one line of arithmetic, and the reasons each of them behaves the way it does.

## Error Is the Whole Idea

Every feedback controller does the same thing. It measures the difference between where it is and where it wants to be, and it acts to reduce that difference.

> error = target − measured

If the target is 1.0 m from a wall and the sensor reports 0.85 m, the error is +0.15 m, and the robot should back away. If it reports 1.20 m, the error is −0.20 m, and it should approach.

The simplest controller acts on the sign of the error: move towards the target if the error is negative, away if positive. This is **on-off control**, and it is what a thermostat with a single threshold does. It works, and it chatters: the machine oscillates around the target because it has no sense of proportion.

Add proportion. If the error is large, act strongly; if it is small, act gently.

> command = gain × error

This is **proportional control**, and the gain is the single number that decides the personality of the machine. Too low and it drifts towards the target, sluggish and always a little short. Too high and it overshoots, comes back, overshoots again, and eventually oscillates.

## The Line Follower

A line follower is the classic first feedback robot, and it repays study because every part of it is visible.

Two light sensors sit either side of a black line on a pale floor. Each reports a value: high on pale floor, low on black line. The robot computes an error from the difference between them:

> error = left − right

If both sensors see pale floor, the error is zero and the robot drives straight. If the left sensor sees the line, the robot has drifted right, so it steers left. The size of the steering command is proportional to the difference, so a small drift produces a small correction.

Now watch what happens as the gain rises. At a low gain, the robot follows gently and cuts corners. At a moderate gain, it tracks the line closely. At a high gain, it oscillates across the line, overcorrecting each time, and eventually leaves the track at a corner.

There is a second, subtler problem: a proportional controller always leaves a small error when a steady disturbance is present. On a slope, the robot needs a constant steering offset to hold the line, and a controller that only responds to error will settle slightly off-centre. The cure is an **integral** term, which accumulates the error over time and adds a correction until the error disappears. That term is the subject of the volume on control systems; here it is enough to know that it exists and that it is the reason a well-tuned machine does not sit with a permanent offset.

## Adding the Integral Term, and What It Costs

The integral term accumulates error over time and adds a correction proportional to that accumulated total. Its purpose is to remove the steady offset that proportional control leaves behind.

Picture the line follower on a slightly sloped floor. To hold the line it needs a permanent steering offset, say 5% to the left. A proportional controller only produces output when there is an error, so it settles with a small permanent error: the robot tracks the line a few millimetres to one side forever. Add the integral term and the accumulated error grows until the offset is supplied, at which point the error returns to zero and the accumulation stops.

The cost is instability if the term is too strong. The integral term remembers the past, so it keeps pushing after the error has gone, overshoots, and then has to unwind. On a system with delay — and every robot has delay — a large integral gain produces slow, growing oscillations that are painful to diagnose because the proportional term looks correctly tuned.

Two practical rules keep it manageable. Clamp the accumulated value, so that a long period of saturated output does not build a huge total that takes seconds to discharge; this is called anti-windup and it is the difference between a robot that recovers from a jam and one that lurches when it is released. And add the integral term last, after the proportional gain is tuned on the flat floor, so that you can see what it changes.

| Term | Responds to | Removes | Risk if too large |
|---|---|---|---|
| Proportional | Current error | Most of the error quickly | Oscillation |
| Integral | Accumulated error | Steady offset | Slow growing oscillation |
| Derivative | Rate of change of error | Overshoot | Amplifies noise |

The derivative term, for completeness, acts on how fast the error is changing and damps the approach to the target. It is the term that makes a heavy machine stop without overshooting, and it is also the term that turns sensor noise into motor chatter, because differentiating a noisy signal amplifies the noise. Most small robots use proportional control alone, add integral when an offset appears, and add derivative only when the mechanics are stiff enough to tolerate it.

## Reflexes and Battles

Some behaviours should not be polite. A bumper switch that reports contact should stop the robot immediately, whatever the navigation planner thinks.

This is a **reflex**: a fast, local response that overrides everything else. It is the robot equivalent of pulling your hand from a hot pan, and it should be implemented in the same spirit: short, simple, and impossible to talk out of.

The classic architecture for combining reflexes is **subsumption**, introduced by Rodney Brooks in the 1980s. Each behaviour runs continuously and proposes an action. Higher-priority behaviours suppress lower-priority ones. A robot might have a wander behaviour, a wall-following behaviour, and a halt-on-bump behaviour, in that order of priority. When the bumper closes, the halt wins, and it wins because of the wiring of the arbitration, not because the scheduler happened to run it.

| Behaviour | Trigger | Action | Priority |
|---|---|---|---|
| Halt on bump | Bumper closed | Stop, reverse briefly | Highest |
| Avoid obstacle | Distance below 0.4 m | Turn away | High |
| Follow line | Line sensor active | Steer to line | Medium |
| Wander | Always | Drive forward slowly | Lowest |

Subsumption fell out of fashion as planners became more capable, and it has never stopped being useful. Every safety layer in a modern robot is a subsumption system: a reflex that suppresses the intelligent behaviour when the reflex is triggered.

## Timing: The Number Nobody Checks

A feedback loop has a period: the time between one measurement and the next. Everything about the behaviour depends on that period relative to how fast the machine can change.

A line follower cycling at 100 Hz sees the world every 10 ms. At 0.5 m/s it travels 5 mm per cycle, which is small compared with the sensor's field of view, and the control is smooth. The same robot cycling at 10 Hz travels 50 mm per cycle and will oscillate regardless of its gain, because it is always correcting a situation that has already changed.

The rule of thumb is that the loop should run at least ten times faster than the fastest thing the machine needs to respond to. For a line follower, 50 to 100 Hz is comfortable. For a balancing robot, 200 to 1,000 Hz. For a walking robot's joint, several kilohertz.

This is also the reason a control loop should never be slowed down by logging, printing or a network call. A `print` statement inside a loop that must run every millisecond is a bug, not a diagnostic.

## Problems

1. A distance controller has a target of 1.0 m, a sensor reading of 0.9 m, and a gain of 0.5 per metre. What command does it produce? What command with the error reversed?

2. A line follower with a proportional gain of 10 oscillates. What are the two most likely causes, and what would you change first?

3. A balancing robot cycles at 100 Hz and falls over. Why is 100 Hz probably too slow, and what would you expect to happen at 500 Hz?

4. Sketch a subsumption architecture for a robot that must follow a corridor, avoid people, and stop when a button is pressed. List the behaviours in priority order and say what each one overrides.

5. Explain in two sentences why an integral term is needed on a slope but not on a flat floor.
