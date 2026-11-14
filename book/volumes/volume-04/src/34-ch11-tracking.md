# Tracking Across Frames

Two identical bearings travel along a conveyor and cross in front of the camera, one behind the other. In one frame they overlap almost completely. In the next they have separated, and the system — which has been tracking each as a distinct object — assigns the left one's identity to the right-hand position and the right one's to the left.

Downstream, one bearing is recorded as having travelled backwards, and the count for the batch is wrong by two. Nobody notices for a week, because the count is only wrong when parts overlap, and parts only overlap when the line runs unevenly.

Tracking is the discipline of maintaining identity over time, and it is where many otherwise sound vision systems acquire their reputation for being "almost right". This chapter covers the small amount of arithmetic involved, the failure modes that survive it, and the timing budget that decides whether a track is worth anything at all.

## Why Track At All

Three reasons, in increasing subtlety.

**Counting.** A detector that fires on every frame counts one object many times. A track counts once, when the object enters, and is a bookkeeping device.

**Speed and direction.** The difference between an object's positions in successive frames, divided by the frame interval, gives velocity — which is often the actual quantity of interest, for a conveyor, a roller, or a falling part.

**Occlusion.** A single frame may not contain the object. A track carries a belief about where it should be, so that a gap of one or two frames is survivable. This is the property that makes tracking indispensable in cluttered scenes.

## Association: Who Is Who

The core operation is **association**: given tracks from the previous frame and detections in the current one, decide which detection belongs to which track.

The simplest version uses predicted position. Each track has an estimated position and velocity; extrapolate the position forward by one frame; for each detection, compute the distance to each predicted position; and match the closest pair, subject to a **gate** — a maximum distance beyond which the detection is treated as a new object.

The gate is not arbitrary. It should be set from the motion: an object moving at most 30 pixels per frame with a detection uncertainty of ±5 pixels needs a gate of roughly 3 standard deviations, or 45 pixels.

Worked. A conveyor at 0.2 metres per second, a camera at 30 frames per second, a sampling interval of 0.25 mm per pixel.

> movement per frame = 200 mm/s ÷ 30 = 6.67 mm
> in pixels = 6.67 / 0.25 = 27 px

A gate of 45 pixels therefore accommodates the expected motion plus four deviations of jitter, and it is about to be tested, because the parts are 40 pixels wide.

The gate is bigger than the part. That is the fundamental difficulty of this example: at this speed and frame rate, an object moves most of its own width between frames, so proximity alone cannot distinguish it from its neighbour. The remedies are to increase the frame rate, reduce the speed, or use a better motion model — and of the three, only the first two are reliable.

## One-to-One Assignment

Matching greedily, closest pair first, fails exactly when it matters. Two objects approach each other; the nearest detection to track A is the other object; greedy matching takes it, and track B is left with a detection 60 pixels away, outside the gate, and is dropped.

The correct formulation is an assignment problem: choose the set of pairings that minimises total distance, with each track and each detection used at most once. The classical solution is the Hungarian algorithm, which for realistic numbers of tracks costs nothing measurable. Most vision libraries provide it, usually under a name like `linear_assignment`.

A practical compromise that works in most cells: compute the full distance matrix, solve the assignment, then discard any pairing whose distance exceeds the gate and treat the remaining unmatched detections as new tracks. This is simple, fast, and — crucially — it cannot produce the crossed assignment that greedy matching produces.

## Predict, Then Correct

Once association is done, each track's state is updated. The standard estimator is a **Kalman filter**, whose central idea is small enough to state in one paragraph.

You have two sources of information about where the object is: your prediction from its previous motion, and the measurement in the current frame. Both are uncertain. The filter combines them in proportion to their certainty, giving more weight to whichever is more reliable at that moment.

In one dimension, with a predicted position uncertainty of 3 pixels and a measurement uncertainty of 2 pixels, the weight given to the measurement is

> gain = 3² / (3² + 2²) = 9 / 13 = 0.69

and the estimate becomes 0.69 × measured + 0.31 × predicted. Next frame, the prediction is more certain — it has been corrected — so the gain rises, and the filter trusts its own model more. When a detection is missing, the prediction carries the track for a frame or two, with growing uncertainty, which is exactly the behaviour wanted during an occlusion.

| Frames without detection | Track status | Typical action |
|---|---|---|
| 1 | Coasting | Keep, widen gate |
| 2–3 | Coasting | Keep, widen further |
| 4–10 | Lost | Keep hidden, allow re-acquisition |
| Over 10 | Dead | Remove, count as exited |

The numbers are conventions. What matters is that the policy exists and is written down, because the alternative — dropping a track the instant a detection is missed — is why counting systems undercount by a few percent, always in the same direction, and are never quite trusted.

## The Cost of an Identity Switch

Identity switches are not cosmetic. Their cost is quantifiable, and quantifying it is the fastest way to justify a faster camera.

Consider a line producing 500 parts per hour, with a tracking system that switches identity once per 100 overlaps, and overlaps occurring for 20% of parts.

> switches per hour = 500 × 0.20 / 100 = 1

One switch per hour sounds trivial, and it is until the consequence is examined: a switch typically produces one double-count and one missing count, so two records are wrong. Over a two-shift day, that is thirty-two wrong records, and if each record is a part that must be traceable, the record system is no longer usable for its intended purpose — which is usually the moment somebody asks for the tracking to be "fixed" by buying a better model, when what the system needs is 60 frames per second instead of 30.

The arithmetic also works in the other direction: at 60 frames per second the movement per frame halves, the gate shrinks below the object width, and the ambiguity that caused the switch disappears. Frame rate is often a tracking parameter, not merely a video parameter.

## The Latency Budget

A vision system that reports a position is reporting where the object was, not where it is. If anything downstream acts on that position, the delay between exposure and action must be accounted for, and the accounting is a table.

| Stage | Delay |
|---|---|
| Exposure | 2 ms |
| Sensor readout and transfer | 4 ms |
| Image preprocessing | 3 ms |
| Inference | 18 ms |
| Network and PLC handshake | 2 ms |
| Actuator response | 8 ms |
| Total | 37 ms |

At 0.2 metres per second the part moves 7.4 millimetres during those 37 milliseconds. If the robot is to grasp a feature that is 6 millimetres wide, the delay is larger than the feature, and the system must compensate: either predict the position at the time of action — which is where the track's velocity estimate earns its keep — or trigger the camera earlier with a photo-eye, so that the part is captured at a known position rather than wherever it happens to be.

The second option is usually better, and it is a hardware decision made in an afternoon. The first is what people attempt when the hardware decision was not made, and it works until the conveyor speed varies.

## Exercises

1. A conveyor runs at 0.35 m/s, the camera at 25 frames per second, and the sampling interval is 0.3 mm per pixel. Compute the movement per frame in millimetres and in pixels. Is a gate of 40 pixels sensible for parts 50 pixels wide?
2. A track has a predicted position uncertainty of 5 pixels; a detection has uncertainty of 1.5 pixels. What is the Kalman gain, and what does it mean in words?
3. Two parts cross. Track A is predicted at x = 100, track B at x = 140. Detections appear at x = 118 and x = 122. Explain what greedy matching does and what the correct assignment is.
4. A system counts 12,000 parts per shift and is known to undercount by 1.2%. How many parts are lost per shift, and what three checks would you make first?
5. Total latency is 55 ms and the line speed is 0.5 m/s. How far does a part travel before the actuator responds? What would you change if the tolerance is ±5 mm?
6. Design a tracking policy for a cell in which parts may stop on the conveyor for several seconds. What should a track do when the object has not moved, and what should happen when it moves again?
