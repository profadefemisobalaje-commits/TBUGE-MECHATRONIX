# The Anatomy of an Agent

A thermostat is a poor thing to call intelligent, and yet almost everything that deserves the name is built the same way. Something measures the world. Something decides what to do about it. Something changes the world. The measurement comes back, and the cycle repeats. The thermostat does this with a single temperature and a switch. A self-driving car does it with a dozen sensors and a steering wheel. The difference is in the size of the loop, not in its shape.

This chapter gives that shape a name and a set of boxes, because a surprising number of confused arguments about artificial intelligence are really arguments about which box is being discussed. When someone says a robot “decided” to do something, ask what it sensed, what it could have chosen instead, and how it knew the outcome. Usually one of the three is missing, and the sentence collapses.

## A Box on the Wall

Take the thermostat seriously for a minute, because it is the smallest complete example of the thing this book is about.

It has a temperature sensor, a switch that turns the heating on or off, and a target. The naive policy is to heat whenever the room is below the target and stop when it reaches it. That policy works in theory and fails in practice, because real rooms have thermal mass and real sensors have noise: the heating clicks on and off every few seconds, and the relay that does the switching wears out within a season.

So thermostats use a band. Heat until the room reaches 21.5 °C. Then do nothing until it falls to 20.5 °C, and heat again. Inside the band, the heater keeps whatever state it had. Written as a table, the policy looks like this:

| Temperature | Heater |
|---|---|
| Below 20.5 °C | On |
| 20.5 °C to 21.5 °C | Keep previous state |
| Above 21.5 °C | Off |

Three lines, one number sensed, one actuator, no memory beyond the previous state. That is an agent. It is not intelligent in any interesting sense, but it is complete: it senses, it decides, it acts, and it has a goal it can miss. Once you can see the thermostat as an agent, you can see a factory robot or a chat assistant the same way, and the questions you ask about them become much sharper.

## Four Boxes and a Loop

The standard description of an agent has four parts, and the acronym for them is PEAS: **P**erformance measure, **E**nvironment, **A**ctuators, **S**ensors. It is worth the ninety seconds it takes to memorise, because it is the first page of every serious design document you will ever write.

Take a delivery robot in a hospital. It carries blood samples between wards, uses lifts, and shares corridors with staff, patients and trolleys.

**Performance.** Deliveries per hour. Zero collisions with people. Zero lost or mislabelled samples. Battery never below 20% at the end of a shift. Those four are not the same kind of number: one is a rate to maximise, two are constraints that must never be violated, and one is a condition for the machine to finish its day. Writing them as a flat list and pretending they are interchangeable is the most common error in the whole design.

**Environment.** Corridors with polished floors, lifts with closing doors, people who move unpredictably, trolleys left in the way, and the occasional spill. The robot's world is not a diagram. It is a building with a cleaning schedule.

**Actuators.** Two drive wheels, a lift-call button, a screen, a speaker.

**Sensors.** A laser scanner, cameras, bumpers, wheel encoders, a battery monitor, and a downward sensor that notices when the floor has stopped being a floor.

Now something useful happens. The PEAS description tells you what the hard part will be before you write a line of code. The environment has people in it, which means the world changes while the robot is deciding. The performance measure contains constraints that must never be violated, which means the decision procedure needs a safety layer that does not depend on the main decision procedure. The actuators include a speaker, which means the robot is expected to explain itself to humans, which is a design commitment, not a feature.

## Worlds Have Shapes

Two agents with the same sensors can need completely different algorithms, because their environments differ in ways that decide what is possible.

**Fully or partially observable.** In chess you can see every piece. In a corridor you cannot see through a wall. Partial observability forces memory and inference: the agent must keep a picture of what it has seen and reason about what it cannot see.

**Deterministic or stochastic.** A chess move has a known result. A wheel on a wet floor may slip. Stochastic environments push you from rules towards probability, which is the subject of the sixth chapter.

**Static or dynamic.** In a puzzle, the world waits while you think. In traffic, it does not. Dynamism puts a deadline on every decision, and a deadline changes the kind of algorithm you can use.

**Discrete or continuous.** A grid has finitely many squares. A real corridor has infinitely many positions. Continuous spaces need different mathematics, which is why the volumes on kinematics and planning exist.

**Single-agent or multi-agent.** A robot alone in a warehouse chooses freely. A robot among people must predict what the people will do, knowing that they are predicting it too.

Here is the practical consequence, and it is worth writing on a card. A fully observable, deterministic, static game can be solved by searching ahead. A partially observable, stochastic, dynamic street cannot. The first is a puzzle. The second is robotics. A great many student projects fail because a puzzle method has been aimed at a street.

## The Ladder

Agent designs can be arranged from simple to complex, and each rung adds a capability at a cost.

At the bottom is the **reflex agent**: if this, then that. The thermostat. Fast, predictable, and helpless the moment the condition does not contain enough information to decide.

Above it is the **model-based agent**, which keeps an internal picture of the world. A robot that remembers a chair was there two seconds ago can still avoid it when a person walks between the robot and the chair. The cost is memory, and the new risk is a stale model: the robot confidently avoiding a chair that was moved.

Above that is the **goal-based agent**, which chooses actions by planning a route to a goal instead of following a fixed rule. This is where search enters, and it is the subject of the next chapter.

Above that is the **utility-based agent**, which weighs competing goals and picks the best trade-off. A delivery robot that balances speed against battery life and passenger comfort is doing this. The hard part is not the algorithm; it is deciding what the numbers should be.

At the top sits the **learning agent**, which improves its own policy from experience. A vacuum robot that adapts to a new flat, or a language model that is trained on more text, belongs here.

The cheapest illustration of the ladder is the domestic vacuum robot. The first mass-market model, launched in 2002, was a reflex agent: it drove in a straight line until it bumped something, turned, and carried on. It had no map, no memory and no plan. It also sold in enormous numbers, because it met the measure that mattered to buyers — the floor was cleaner when it finished, at a price people would pay. Later models added memory of obstacles, then systematic coverage patterns, then mapping with a camera or a laser, then scheduling that cleaned the rooms that got dirty most often. Each rung cost more to build, more to test and more to explain, and each answered a complaint from a real user.

That is the correct order of operations, and it is the opposite of the order that excites engineers. Start at the lowest rung that satisfies the measure. Climb when a real person has a real complaint. A reflex agent that meets the requirement is a better engineering answer than a learning agent that nearly does.

## The Measure Bites Back

There is a trap at the centre of all of this, and it deserves its own section because it has ruined more systems than any algorithm.

The agent will optimise exactly what you measure, including the parts you did not mean. Reward a cleaning robot for distance travelled and it will drive in circles all day, because circles are excellent for distance. Reward a delivery robot for speed and it will eventually hit someone, because people are slow. Reward a support chatbot for the length of its answers and it will learn to be tedious.

Economists call the general phenomenon Goodhart's law: when a measure becomes a target, it ceases to be a good measure. The engineering version is blunter. The performance measure is the steering wheel of the project, and if you attach it to the wrong shaft, the vehicle goes where the shaft points.

The defence is not to write a better number. It is to write the measure as two things: something to maximise, and something that must never happen. “Deliver more samples per hour, and never make contact with a person” is harder to game than “maximise efficiency”, because the second clause cannot be traded away for the first.

## Things to Try

1. Write a PEAS description for a lift. It senses calls from floors, carries people, and has a goal. Then classify its environment on the five properties. Which one makes the lift's problem easier than it first appears?

2. Classify these three environments, then name the method each rules out: a chess position, a hospital corridor, a warehouse with twenty robots and one human supervisor.

3. The thermostat policy above has a gap. What happens if the temperature sensor fails and reports nothing at all? Write the missing line of the table, and decide whether “do nothing” is safer than “heat”.

4. Think of a system you use that was clearly designed around the wrong measure. Describe the measure it appears to optimise, the measure its users care about, and what a better pair of clauses would look like.
