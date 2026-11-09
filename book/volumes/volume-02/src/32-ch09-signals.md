# Signals, Noise and Sampling

A sensor reading is never a number. It is a number with a history: it was produced by a physical process, converted by electronics, sampled at intervals, and delivered with some of the world's randomness attached. The difference between a robot that works and one that twitches is usually not the sensor but what happens to its output between the sensor and the decision.

This chapter is about that stretch of the journey. It covers three things: how often to sample, how to reduce noise without destroying the signal, and how to tell whether a reading is drifting rather than changing.

## How Often to Sample

A sensor that is read every 10 ms is sampled at 100 Hz. The question is whether 100 Hz is enough, and the answer is given by the **Nyquist criterion**: to represent a signal faithfully, you must sample at more than twice the highest frequency present in it.

If a motor vibrates at 50 Hz and you sample at 60 Hz, you do not see 50 Hz. You see a slow wobble at 10 Hz, because 60 minus 50 is 10. This is **aliasing**, and it is pernicious because the false signal looks perfectly real. It is a smooth, plausible oscillation that is an artefact of the sampling, and no amount of filtering after sampling can remove it, because the information needed to distinguish it was never captured.

The defence has two parts. Sample faster than you think you need — a factor of five or ten above the bandwidth you care about is common. And filter the analogue signal before the converter, so that content above the sampling rate never reaches it.

Work an example. A vibration sensor is mounted on a gearbox that rings at 800 Hz. To see the ring in the data, the sample rate must exceed 1,600 Hz; 2 kHz is comfortable. A system that samples at 200 Hz will report a 0 Hz signal, a flat line, while the gearbox rings. The data will look calm and the machine will be failing.

## Noise, and the Square Root of N

Noise is the part of a measurement that changes when nothing in the world has changed. Some of it is thermal, some of it is electrical interference, some of it is quantisation, and all of it can be reduced — at a cost in time.

The simplest reduction is **averaging**. Take N readings and average them, and random noise falls by the square root of N. Sixteen readings reduce the noise by a factor of four, and sixty-four reduce it by a factor of eight. The cost is time: averaging sixteen readings at 1 kHz delays the answer by 16 ms, which is 24 mm of travel at 1.5 m/s.

A **moving average** does the same thing continuously, keeping the last N readings and reporting their mean at every step. It is easy to implement and it has a cost: it delays the signal by half its window, and it smooths genuine changes as well as noise.

A **low-pass filter** does the job more elegantly. A simple resistor-capacitor filter has a cut-off frequency of

> cut-off = 1 / (2π × R × C)

With a 1 kΩ resistor and a 10 µF capacitor, the cut-off is about 16 Hz: faster changes are attenuated, slower ones pass. In software, the same idea appears as an exponential filter that keeps a running estimate and moves it a fraction of the way towards each new reading. A factor of 0.1 gives a smooth signal and a lag of a few samples; a factor of 0.5 gives a fast signal and lets more noise through.

The choice of filter is always a trade between smoothness and delay, and the delay is the one that gets you into trouble. A robot that filters its distance readings heavily will detect an obstacle late, and no amount of accuracy makes up for reacting after the collision.

## Where the Noise Comes From

Motors are the loudest thing in most robots, electrically speaking. Brushed motors produce sparks at the commutator, which radiate across a wide band. Switching drivers produce fast edges at tens of kilohertz. Long wires to a sensor act as antennas, and the shared ground connection carries every current back to the battery.

Four practical measures make an enormous difference and cost almost nothing.

**Keep signal wires away from power wires.** Route them on opposite sides of the machine, and cross at right angles when they must cross.

**Twist signal pairs.** A twisted pair picks up roughly the same interference on both wires, which cancels at the receiver.

**Use a star ground.** Every return path meets at one point near the battery, rather than daisy-chaining through the electronics. Ground loops — where two paths to ground exist — create currents that appear as noise in every signal that shares them.

**Add decoupling capacitors** near the electronics, so that a brief demand for current is supplied locally rather than through a long, inductive path.

None of these are advanced. All of them are missing from most student robots, and all of them show up as "the sensor is unreliable" when the sensor is fine.

## Calibration: Zero, Span and Drift

A sensor reports a number; the robot needs a physical quantity. The mapping between them is established by **calibration**, and it has two parts.

**Zero** is the reading when the quantity is zero. A force sensor must read zero with nothing on it; if it reads 0.3 N, every measurement carries a 0.3 N offset.

**Span** is the change in reading per unit of the quantity. A temperature sensor that reports 10 mV per degree needs that figure, measured rather than assumed.

Calibration is usually a two-point procedure: measure at a known low value and a known high value, then fit a straight line. It sounds trivial until you discover that the sensor's response is not linear, that the span changes with temperature, and that the zero moves as the electronics warm up.

That last effect is called **drift**, and it is the reason serious instruments are calibrated before each use, or include a reference they can check against. A robot that measures force to decide whether it has gripped an object will fail if its force sensor has drifted by 2 N since the morning, because the threshold it compares against was set in the morning too.

The practical defence is a **zeroing routine**: with the gripper empty and still, take a hundred readings, average them, and subtract that value from every subsequent reading. It takes half a second, and it removes the largest single source of error in cheap sensors.

## Problems

1. A signal contains content at 60 Hz. What is the minimum sampling rate needed to represent it? What happens if you sample at 100 Hz and what happens at 70 Hz?

2. You average 25 readings. By what factor does the random noise fall? If each reading takes 2 ms, what delay have you introduced?

3. Compute the cut-off frequency of a filter with a 4.7 kΩ resistor and a 1 µF capacitor.

4. A force sensor reads 0.4 N with nothing touching it. What would you do before using it, and what would happen if you did not?

5. Name three ways to reduce electrical noise in a robot without changing any software, and say which one is most likely to fix a sensor that misbehaves only when the motors run.
