# Robots at Work and at Home

The word "robot" carries a science-fiction shadow that makes the real machines look disappointing. The real machines are more interesting, because they had to solve the problems of dirt, heat, vibration, cost and insurance, and the solutions are visible in their shapes.

Look at the machines that already work for a living and you will see the same three questions answered again and again: what is the energy source, what is the world like, and who is responsible when it goes wrong.

## The Arm Behind the Fence

The industrial arm is the most successful robot ever built by the numbers: several hundred thousand are in service, and the number grows every year. The typical machine lifts 6 to 200 kg, reaches 1 to 3 m, and repeats a position to between 0.02 and 0.1 mm, tens of thousands of times without rest.

Its design follows from a single decision: the arm is bolted to the floor and the work comes to it. That removes localisation, perception, battery and navigation from the problem, and it leaves speed, accuracy and reliability — the three things industry will pay for.

The economics are simple enough to compute. A welding cell might cost 150,000 including the robot, the fixture, the fence and the integration. It runs two shifts, five days a week, which is roughly 3,600 hours a year. If it replaces two operators whose fully loaded cost is 30,000 each, the payback is a little over two years, and the machine then runs for a decade with maintenance. This arithmetic, rather than any interest in intelligence, explains why the arm exists.

Its weakness is equally simple. The arm knows nothing about parts that are not where the fixture says they are. A part presented at a random orientation defeats it completely, which is why the field has spent thirty years trying to add eyes, and why the volumes on vision and manipulation exist.

## The Warehouse

In 2012, Amazon bought a company called Kiva Systems for about 775 million dollars. Kiva made small, flat, orange robots that carried shelving units across a warehouse floor. Instead of a robot reaching a shelf, the shelf came to the picker.

The engineering is instructive because it is so constrained. The robots follow barcode-like markers on the floor, so their localisation is trivial. They move slowly and carry a lot, so their motors are modest. They cooperate by not colliding, using traffic rules and a central coordinator rather than sophisticated negotiation. The result is a system that increased picking productivity severalfold, and it works because the warehouse was rebuilt around the robots rather than the robots being dropped into an existing warehouse.

That last point is the one most often missed. The successful deployment changed the building, the shelving, the workflow and the job of the people in it. A robot that has to fit into an unchanged world is a much harder problem, and often a worse investment.

## Where Precision Is the Point

Surgical robots, led by the da Vinci system approved in 2000, do not operate autonomously. A surgeon sits at a console and moves instruments through a robot, which scales motion down, removes tremor and allows access through small incisions.

The robot's sensors report force and position; its actuators are precise and smooth; its failure modes are designed around the surgeon's control. The safety question is different from an industrial cell, because the patient is inside the working envelope. The answer is not a fence but a set of limits on force, speed and range, plus a control architecture that always leaves the surgeon in command.

Surgical robotics is the clearest case in the field for teleoperation: the value is not autonomy but precision, dexterity and the ability to see. Attempts to automate any part of the procedure run into the same wall as everywhere else, which is that the world inside a body is not the world of the training data.

## Outdoors

Agricultural robots, drones and mining machines work in places that are deliberately unstructured. They succeed by narrowing the task.

A field robot that removes weeds recognises one plant and ignores the rest, and it does so with a camera, a light source and a sprayer, at a speed slow enough to allow the perception to work. A drone that maps a field flies a planned grid and takes photographs; the intelligence is in the stitching on the ground. A mining truck follows a route that has been driven a thousand times and uses radar to avoid the other trucks.

The pattern is consistent: outdoors, the world is unpredictable, so the successful machines reduce the number of decisions they make and take their time over the ones that remain.

## At Home

A domestic robot vacuum sells in the tens of millions, and it is the closest thing the field has to a mass-market mobile robot. It also illustrates every constraint in this volume at once.

It must cost a few hundred, so its motors are small, its sensors are cheap and its structure is plastic. It must run on a battery, so its power budget is tight and its suction is modest. It must operate around furniture, pets and cables, so it must fail gracefully: bumping into things, getting stuck, and asking for help rather than damaging the house.

The generations of improvement follow the ladder from Volume One. Early models bounced at random. Later models mapped, planned coverage, and returned to a dock. Each step required better sensing, more computation and more careful power management, which is to say it required everything this volume has described.

## The Human Beside the Machine

The fastest-growing category of industrial robot is the one designed to be next to a person rather than behind a fence. A collaborative arm weighs twenty to thirty kilograms, lifts five to fifteen, and is limited in speed and force so that a contact with a human is uncomfortable rather than injurious.

The economics changed when these machines arrived. A traditional cell needs a fence, a safety relay, a fixture and an integrator, and the installation often costs more than the robot. A collaborative arm can be wheeled to a bench, taught by guiding it through the motion by hand, and put to work the same day. For a small factory making a hundred different products in small batches, that difference is decisive.

The safety argument is subtler than the marketing suggests. A collaborative rating describes what happens when the robot contacts a person under specified conditions: the force and pressure must stay below the limits in the standard, and the limits depend on which part of the body is contacted. A rounded forearm touching an arm is one case; a sharp gripper edge touching a face is another. The rating belongs to the whole application, not to the robot alone, and the tool, the workpiece and the fixture can each destroy it.

The human factors are the other half. A person working beside a machine that moves unpredictably will be startled, and a startled person makes mistakes. Good installations make the robot's intentions visible: it slows before it turns, it pauses when a hand enters its path, it signals with light or sound before a fast move. The machine does not need to be charming. It needs to be legible.

## Why Machines Still Fail at Work

Three limits recur across every application.

**The world is not the training ground.** Every robot meets conditions its designers did not anticipate, whether that is a new part, a wet floor, a different light or a person behaving unusually.

**Integration is the cost.** The robot is often a small fraction of the project. Fixtures, safety systems, software, training and maintenance are the rest, and they are where budgets overrun.

**Responsibility is unresolved.** When a machine injures someone, the question of who is liable — manufacturer, integrator, owner, operator — is answered by law and contract rather than by engineering, and the answer shapes what gets built. A machine whose failure has no clear owner tends not to be deployed.

## Problems

1. An industrial cell costs 150,000 and replaces two operators at 30,000 each per year. Compute the payback period, assuming 10% annual maintenance. What would make the investment fail?

2. A warehouse robot moves at 1.2 m/s and carries 500 kg. Estimate the kinetic energy at full speed and explain why the safety system must be designed around it.

3. A domestic vacuum robot has a 14.4 V, 2.5 Ah battery and draws 25 W on average. Estimate its runtime, and say what would change if it drew 40 W.

4. Name one task in your country that robots do not currently do and explain, in three sentences, whether the obstacle is technical, economic or social.

5. For the surgical robot described above, list three failure modes and, for each, the layer of protection you would expect to find.
