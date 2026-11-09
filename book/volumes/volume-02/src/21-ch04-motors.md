# Electric Motors

Almost every robot you will meet is moved by an electric motor, and almost every motor is chosen badly the first time. The reason is not ignorance of electromagnetism. It is that the two numbers people look at — power and voltage — are the two least useful numbers on the label.

What matters is torque at a given speed, and the relationship between them. A motor that produces 20 watts at 3,000 revolutions per minute and one that produces 20 watts at 30 revolutions per minute are completely different animals, and neither will do the other's job.

## Two Numbers, One Curve

A motor produces **torque**, a turning force, measured in newton-metres. It turns at a **speed**, measured in radians per second (or revolutions per minute, which is the same thing divided by 9.55). Multiply the two and you get mechanical power in watts.

The crucial fact is that a motor cannot give you both maximum torque and maximum speed at once. At zero speed it produces its largest torque, called the **stall torque**. At zero load it spins at its fastest, called the **no-load speed**. Between those two points the relationship is roughly a straight line:

> torque available falls as speed rises

This curve is the single most useful document about any motor, and it is the first thing to ask a supplier for. A motor with a high stall torque and a low top speed is a strong, slow motor. A motor with the opposite is fast and weak. Neither is better; they are different trades.

## What the Motor Feels

Inside a brushed direct-current motor, the physics is simple enough to state in three sentences, and those three sentences explain almost every behaviour you will see.

The **speed** of the motor is approximately proportional to the voltage applied, minus the losses. Double the voltage and the motor tries to spin twice as fast.

The **torque** is proportional to the current flowing through the windings. Demand more torque by loading the shaft, and the motor draws more current to supply it.

The winding has **resistance**. Current through resistance produces heat, and heat is what destroys motors.

Put those together and you get the behaviour that surprises beginners. When you stall a motor — hold the shaft so it cannot turn — the current is limited only by the winding resistance. A small motor with a 1 Ω winding on a 24 V supply will draw 24 A at stall, which is 576 W of heat inside a component the size of a matchbox. It will not survive for many seconds.

That is why a stalled robot arm can burn out a motor in the time it takes to walk across the room, and why the first protective measure in any motorised design is a current limit rather than a bigger motor.

## Choosing a Motor from the Task

Here is the calculation that turns a requirement into a purchase order. It has four steps and no calculus.

**Step 1: find the torque the joint must hold.** A link of 0.5 m carrying a 1 kg mass at the tip needs a torque of mass × gravity × distance: 1 × 9.81 × 0.5, which is about 4.9 N·m, just to hold it still against gravity. Add the torque to accelerate it: a modest 1 rad/s² of angular acceleration with an inertia of about 0.08 kg·m² needs another 0.08 N·m. Round up, and design for 6 N·m at the joint.

**Step 2: choose a gear ratio.** Small motors produce small torques; a typical hobby motor might produce 0.1 N·m of continuous torque. To get 6 N·m you need a ratio of at least 60:1, and that is before losses. With a gearbox that is 80% efficient, you need 7.5 N·m at the gearbox output, so the motor must supply 7.5 / 60 = 0.125 N·m. Choose a motor rated a little above that, say 0.15 N·m continuous.

**Step 3: check the speed.** The same gearbox divides speed by 60. If the motor spins at 3,000 revolutions per minute, or 314 rad/s, the joint turns at 5.2 rad/s — about 300 degrees per second. If your task needs the arm to move 90 degrees in 0.5 s, that is 3.1 rad/s, and the design passes with room to spare.

**Step 4: check the power and the heat.** The motor is delivering 0.15 N·m at 314 rad/s, which is about 47 W of mechanical power. At 80% efficiency in the gearbox and perhaps 75% in the motor, it is drawing around 78 W of electrical power, most of which becomes heat somewhere. That heat has to leave a small metal cylinder. Chapter 6 does the arithmetic.

| Quantity | Symbol | Formula | Example |
|---|---|---|---|
| Joint torque needed | T | m × g × r | 1 × 9.81 × 0.5 = 4.9 N·m |
| Gear ratio | N | T_joint / (T_motor × efficiency) | 6 / (0.1 × 0.8) = 75 |
| Joint speed | ω | motor speed / N | 314 / 75 = 4.2 rad/s |
| Motor power | P | T × ω | 0.15 × 314 = 47 W |

The four steps take ten minutes and prevent the most common failure in student robotics: a beautiful mechanism driven by a motor that cannot hold it.

## Steppers, Servos and Brushless Motors

Three families dominate small and medium robots, and each has a characteristic strength.

A **stepper motor** moves in fixed increments — typically 1.8 degrees per step, or 200 steps per revolution — and holds its position when stationary. It needs no sensor to know where it is, which is why it appears in 3D printers and cheap Cartesian robots. It loses steps silently if overloaded, and it draws current even when holding still.

A **hobby servo** contains a small motor, a gearbox and a position sensor in one box, and accepts a command in the form of a pulse width: about 1 ms for one extreme, 2 ms for the other, repeated 50 times a second. It is the fastest route to a moving joint, and it is limited in torque, accuracy and life.

A **brushless motor** replaces the mechanical commutator with electronics, which makes it more efficient, longer-lived and capable of higher power for its size. It requires a driver that knows the rotor position, which adds cost and complexity. Almost every serious robot arm, drone and electric vehicle uses them.

| | Stepper | Hobby servo | Brushless |
|---|---|---|---|
| Position feedback | None needed | Internal | Required (Hall or encoder) |
| Torque for size | Moderate | Low | High |
| Holding torque | Yes, with current | Yes | With control |
| Typical use | 3D printers, pick-and-place | Small joints, steering | Drones, arms, vehicles |
| Main risk | Silent loss of steps | Gear wear, limited life | Driver complexity, cost |

## Problems

1. A motor has a stall torque of 0.8 N·m and a no-load speed of 4,000 revolutions per minute. Assuming a straight-line torque-speed curve, what torque does it produce at 2,000 revolutions per minute? What mechanical power is that?

2. A joint must hold 3 kg at 0.4 m. Compute the torque required. With a gearbox of 40:1 and 85% efficiency, what continuous motor torque is needed?

3. A 12 V motor has a winding resistance of 2 Ω. What current flows at stall, and how much heat is produced in the winding? Why does this matter for a robot that might jam?

4. A stepper motor has 200 steps per revolution and is driven with 16× microstepping. How many commands per revolution? If a belt pulley of 20 mm diameter is on the shaft, how far does the belt move per microstep?

5. Explain in three sentences why a motor's power rating alone cannot tell you whether it will lift your arm.
