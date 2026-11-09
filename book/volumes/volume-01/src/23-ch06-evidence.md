# Evidence, Not Fact

A robot in a warehouse is told there is a pallet ahead. Its distance sensor reports 1.2 metres. The sensor is good, but not perfect: on a shiny floor it sometimes reads short, and in the cold room it occasionally drops a reading entirely. The robot has to decide whether to slow down, and the sensor has not given it a fact. It has given it evidence.

Almost everything a machine receives from the world is evidence. A camera reports brightness, not objects. A microphone reports pressure, not words. A thermometer reports a voltage, not a temperature. Every one of those readings is the result of physics that is partly unknown, electronics that are slightly different from the last unit, and a world that will not hold still. Learning to reason with evidence rather than with facts is the single largest step from the toys of Part One to the systems of Part Five.

## The Box That Was Probably There

Start with the simplest possible statement about a sensor: it is right 90% of the time. That sentence contains two different numbers wearing one coat, and pulling them apart is most of the work.

- If something is there, the sensor says “there” 90% of the time. Engineers call this the **sensitivity**, or the true positive rate.
- If nothing is there, the sensor still says “there” 10% of the time. This is the **false positive rate**.

Now the question almost everyone forgets. How often is something actually there? In a busy aisle, perhaps one reading in ten has a real pallet in front of the robot. That number is the **base rate**, and without it the other two tell you nothing at all.

Suppose the robot takes a thousand readings. A hundred have a pallet. Nine hundred are empty aisle.

- Of the hundred real pallets, the sensor sees ninety.
- Of the nine hundred empty stretches, the sensor reports a pallet in ninety, because 10% of 900 is 90.

So when the sensor says “pallet”, there are ninety true reports and ninety false ones. The chance that a pallet is really there is one half.

A sensor described as “90% accurate” has produced a reading that is right half the time. This is not a paradox, and it is not a criticism of the sensor. It is arithmetic, and it is why robots carry several sensors instead of trusting one.

## One Line of Arithmetic

The rule that turns a prior belief and a piece of evidence into an updated belief is named after Thomas Bayes, an eighteenth-century minister who never published it himself; his friend Richard Price found the manuscript and sent it to the Royal Society in 1763.

In words: the belief after the evidence is proportional to the belief before it, multiplied by how well the evidence fits.

In symbols, for a hypothesis H and evidence E:

> P(H given E) = P(E given H) × P(H) / P(E)

The three ingredients have names worth knowing. **P(H)** is the prior, what you believed before. **P(E given H)** is the likelihood, how probable the evidence would be if the hypothesis were true. **P(H given E)** is the posterior, what you should believe now.

Fill in the warehouse numbers. The hypothesis is “there is a pallet”. The prior is 0.1. The likelihood is 0.9. The total probability of a “pallet” reading is the true reports plus the false ones: 0.09 + 0.09 = 0.18.

The posterior is 0.09 / 0.18, which is 0.5.

Read that again as a story rather than a calculation. The robot believed there was a pallet with probability 0.1. One reading moved that belief to 0.5. That is a large change, and it is still not enough to justify stopping a forklift.

So add a second sensor with the same characteristics, pointing at the same place from a different angle. Run the arithmetic again, using 0.5 as the new prior:

> Posterior = (0.9 × 0.5) / (0.9 × 0.5 + 0.1 × 0.5) = 0.45 / 0.5 = 0.9

Two readings, each half-right on its own in this situation, produce a belief of 0.9. A third takes it above 0.97. This is **sensor fusion**, and the arithmetic you have just done by hand is the core of the volume on robotic perception.

There is a condition, and it is easy to violate. The multiplication only works if the two sensors fail independently. Two cameras on the same bracket, blinded by the same low sun at the same moment, are not two pieces of evidence. They are one piece of evidence, counted twice, and the arithmetic will tell you a comforting lie.

## What It Costs to Be Wrong

A robot never gets to act on certainty. It gets to act on a belief, and the right action depends on what happens if the belief is wrong.

Suppose the robot can stop, which costs two seconds of delay, or continue, which risks a collision with a forklift. Give the collision a cost of a thousand units, purely to represent that it is very bad.

If the robot continues, its expected cost is 1,000 × (1 − p), where p is its belief that the way is clear. If it stops, the cost is 2. Continuing is the better bet only when

> 1,000 × (1 − p) < 2

which is true only when p is greater than 0.998.

A belief of 99.8% before moving. That sounds absurd until you watch a robot in a real warehouse, where machines slow down near blind corners and at junctions, not because the software is cautious by temperament, but because somebody did this arithmetic and set the speed accordingly.

The lesson generalises beyond robots. The action threshold is not a property of the probability. It is a property of the consequences. Two systems with identical beliefs should behave differently if one can recover from a mistake and the other cannot. This is the whole of safety engineering in one paragraph, and it is why the phrase “the model was 99% confident” is not a defence after an accident.

## Two Crashes and One Sensor

On 29 October 2018, a Boeing 737 MAX 8 operating as Lion Air flight 610 crashed into the Java Sea shortly after take-off, killing all 189 people on board. On 10 March 2019, another 737 MAX 8, Ethiopian Airlines flight 302, crashed six minutes after take-off, killing 157. The two accidents were similar enough that the aircraft was grounded worldwide within days.

Investigators found that a software system, designed to push the nose down when it detected a risk of stalling, was receiving data from a single angle-of-attack sensor on the side of the fuselage. That sensor was faulty. There was no second sensor cross-checking it, and the pilots had not been told that the system existed, let alone how to override it.

The first lesson is about evidence, and it is the one this chapter can compute. One sensor, however good, is a weak basis for an action that cannot be undone. A second independent source would have moved the belief from “probably a stall” to “something is wrong with the instruments”, and the disagreement itself would have been information. The absence of a second opinion was not an oversight in the mathematics. It was a decision about cost, taken by people who did not do the arithmetic in this chapter.

The second lesson belongs to a later volume, and to a later chapter of this one. A system that acts on the world must let a human see what it believes, and must give that human a way to stop it. Evidence handling and interface design are not separate subjects. They meet in the cockpit, and in the operating theatre, and in the factory.

## Confidence Is Not Truth

Modern systems attach a number to every answer. A classifier says “cat, 0.97”. A language model says it is fairly sure. It is tempting to read those numbers the way you read a fuel gauge, and it is a mistake.

A number is **calibrated** if, among all the cases where the system says 0.9, it is right about nine times in ten. Many systems are not calibrated at all. They produce confident answers because the arithmetic of their output layer produces large numbers when inputs are far from anything familiar, which is exactly backwards from what a cautious engineer would want.

The test is simple and rarely run. Collect a few hundred predictions with their confidence, sort them into buckets, and check the hit rate in each bucket. If the 0.9 bucket is right 60% of the time, the system is overconfident, and every threshold you set from those numbers is wrong.

You cannot fix this by asking the model to be more careful. You fix it by measuring, by recalibrating on held-out data, and by never letting a single confidence number authorise an irreversible action.

## Problems

1. A factory alarm has sensitivity 0.95 and a false positive rate of 0.05. A fault occurs in 2% of production runs. Imagine 10,000 runs and count four things: runs with a fault, true alarms, false alarms, and total alarms. Then compute the probability that there is a fault, given an alarm.

2. Repeat the calculation with a false positive rate of 0.01. Which change helps more: halving the false alarm rate, or raising sensitivity from 0.95 to 0.99? Compute both.

3. Stopping a production line costs 1,000 units. Letting a fault through costs 50,000. Using your answer to question 1, what belief should trigger a stop? Does the real alarm meet it?

4. A door sensor has sensitivity 0.92 and a false positive rate of 0.08. Doors are genuinely open in 15% of readings. Compute the probability a door is open after one positive reading, and after two independent positive readings. How many readings would you require before letting a robot pass through, and why?

5. Write down one number you have seen quoted about a system's reliability, and the three numbers you would need in order to judge it.
