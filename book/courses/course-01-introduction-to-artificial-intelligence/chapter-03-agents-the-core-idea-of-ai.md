# Agents: The Core Idea of AI

> Course 1: Introduction to Artificial Intelligence - Chapter 3 of 10

## Opening

By the end of this chapter you can describe any AI system as an agent, list its sensors, actuators and performance measure, and say why the shape of its environment changes the design.

A thermostat on a wall senses the temperature of a room and switches a heater on or off. A self-driving car senses lane markings and turns a steering wheel. A spam filter senses the words of an email and moves the message to a folder. Three very different machines, one shared structure: something comes in, a decision is made, something goes out. That structure is called an **agent**, and it is the single most useful diagram in this entire book. When a robot project gets confusing — and it will — you can always fix the confusion by drawing the loop again and asking which arrow is broken.

## Big Picture

An agent is anything that senses its environment and acts on it. The environment is everything outside the agent. The loop is: the agent receives a **percept**, decides on an action, the environment changes, and a new percept arrives. The part that makes the decision is the **policy**: a rule, a table, a neural network or a search procedure that maps what the agent knows to what it does.

Designing an AI system, in this view, is choosing a policy that scores well. And "well" must be defined before you start, because the agent will optimise exactly what you measure, including the parts you did not mean. A cleaning robot rewarded for distance travelled will drive in circles all day. A delivery robot rewarded for speed will eventually hit a person. The performance measure is not paperwork. It is the steering wheel of the whole project.

## Key Words

- **Agent** - anything that senses its environment and acts on it.
- **Percept** - one reading of the environment, such as a camera frame or a temperature value.
- **Actuator** - the part that changes the world: a motor, a wheel, a heater, a display.
- **Policy** - the agent's rule for choosing an action from what it knows.
- **Rational agent** - an agent that chooses the action expected to score best, given what it knows and what it can do.
- **Performance measure** - the number that says how well the agent is doing its job.
- **PEAS** - a four-box description: Performance, Environment, Actuators, Sensors.

## The Explanation

### Step 1 - Draw the loop, then name the boxes

Start with the simplest intelligent-ish machine you own: a room thermostat. It has one sensor, a temperature probe. It has one actuator, a switch that powers the heater. It has a performance measure: keep the room comfortable without wasting electricity. And it has a policy, which is usually not "heat below 21 °C and stop at 21 °C". That would switch the heater on and off every few seconds, wearing out the relay.

Real thermostats use a **hysteresis band**: heat until 21.5 °C, then wait until the room falls to 20.5 °C before heating again. The policy is a small table:

| Temperature | Heater |
|---|---|
| Below 20.5 °C | On |
| Between 20.5 °C and 21.5 °C | Keep previous state |
| Above 21.5 °C | Off |

That table is a policy. It was designed by a human, it senses one number, and it has no memory beyond the previous state. It is still an agent, and once you can draw it this way, you can draw anything from a drone to a chat model the same way.

Now scale up. A hospital delivery robot that carries blood samples between wards has:

- **Performance:** deliveries per hour, zero collisions, zero lost samples, battery above 20% at all times.
- **Environment:** corridors, lifts, closing doors, staff, patients, trolleys, polished floors.
- **Actuators:** two drive wheels, a lift-call button, a screen, a speaker.
- **Sensors:** lidar, cameras, bumpers, wheel encoders, a battery monitor, a floor-level cliff sensor.

That is a **PEAS** description, and it is always the first page of a serious design document. Notice how much of the difficulty is visible already. The environment has people in it, which means it changes while the robot thinks.

### Step 2 - Read the environment before choosing a method

Environments differ in ways that decide which algorithm is even possible. Five properties matter most.

**Fully or partially observable.** In chess you see every piece. In a corridor you cannot see through a wall. Partial observability forces the agent to keep a memory of what it has seen and to reason about what it cannot see.

**Deterministic or stochastic.** A chess move has a known result. A wheel on a wet floor may slip. Stochastic environments push you towards probability rather than rules.

**Static or dynamic.** In a puzzle, nothing changes while you think. In traffic, the world moves while your program runs. A dynamic environment sets a hard time limit on every decision.

**Discrete or continuous.** A grid of squares has finitely many positions. A real corridor has infinitely many. Continuous spaces need different maths, which is why Courses 24 and 35 exist.

**Single-agent or multi-agent.** A robot alone in a warehouse chooses freely. A robot among people must predict what others will do, and they are predicting it too.

Here is the practical part. A fully observable, deterministic, static game can be solved by searching ahead. A partially observable, stochastic, dynamic street cannot. The first is a puzzle; the second is a robotics problem. Many student projects fail because a puzzle method is applied to a street.

### Step 3 - Climb the ladder of agent designs

Agent policies can be arranged from simple to complex. Each rung adds a capability and a cost.

**Rung 1 - Simple reflex.** If condition, then action. The thermostat. Fast, predictable, no memory. Fails the moment the condition is not enough to decide.

**Rung 2 - Model-based reflex.** Keep an internal picture of the world. A robot that remembers "I saw a chair here two seconds ago" can still avoid it when the chair is briefly hidden by a person. Adds memory, adds the risk of a stale model.

**Rung 3 - Goal-based.** Choose actions that lead towards a goal, using search or planning. A robot that plans a route to Room 12 rather than following a fixed wall. Adds planning, adds computation time.

**Rung 4 - Utility-based.** When several goals compete, score the outcomes and pick the best trade-off. A delivery robot that balances speed against battery and passenger comfort. Adds the hard question of what the numbers should be.

**Rung 5 - Learning.** Improve the policy from experience. The agent that adjusts its own behaviour when the floor changes from carpet to tile. Adds data requirements, adds the risk of learning the wrong thing.

Now take one machine through the ladder. A domestic vacuum robot:

| Rung | Policy | Behaviour |
|---|---|---|
| 1 Reflex | Bump, then turn | Bumps into furniture all day |
| 2 Model | Remember walls seen | Covers rooms in tidy lines |
| 3 Goal | Plan coverage pattern | Finishes a room in one pass |
| 4 Utility | Balance time, charge, noise | Cleans the kitchen first, charges before the bedrooms |
| 5 Learning | Adapt to the home | Learns where the sofa legs are, avoids them next time |

Each rung is more capable and harder to test. This is the oldest trade-off in engineering: capability against complexity. Choose the lowest rung that meets the performance measure. A reflex agent that meets the requirement is a better engineering answer than a learning agent that nearly does.

## Where It Goes Wrong

**Mistake 1 - Believing an agent must have a body.** A spam filter is an agent. Its actuators are "move to folder". *Fix:* use the PEAS boxes, not the presence of wheels.

**Mistake 2 - Skipping the environment description.** Students pick a reinforcement learning method for a deterministic puzzle, or a search method for a crowded corridor. *Fix:* write the five environment properties on one line before writing code.

**Mistake 3 - Measuring the wrong thing.** The performance measure shapes behaviour. Reward distance and you get circles. *Fix:* write the measure as a sentence a customer would sign, then add the constraint that must never be broken, such as "no contact with a person".

**Mistake 4 - Mixing up sensors and actuators.** A speaker is an actuator, not a sensor. A microphone is a sensor, not an actuator. *Fix:* ask which direction the energy flows. Into the agent: sensor. Out of the agent: actuator.

**Mistake 5 - Building rung 5 when rung 1 would pass.** A learning system is harder to debug, harder to certify and harder to explain. *Fix:* start at the lowest rung, measure, and climb only when the measure fails.

## Case Note

The first mass-market robot vacuum, launched in 2002, used a reflex policy. It moved in a straight line until it bumped something, then turned and continued. It had no map, no memory of where it had been, and no plan. By the standards of robot intelligence it was barely above a thermostat. It also sold in enormous numbers, because it met the performance measure that mattered to buyers: the floor was cleaner when it finished, at a price people would pay.

Later models climbed the ladder. They added memory of obstacles, then systematic coverage patterns, then mapping with a camera or a laser, then scheduling that prioritises rooms by how dirty they get. Each rung cost more to build and more to test, and each answered a complaint from real users rather than an ambition from an engineer.

The interesting part is where the ladder stopped being about cleaning. Once the robot had a map, it could also be asked to clean one room only, or to avoid a room, or to return to its dock from the far corner of the house. New capability created new expectations, which created pressure for the next rung.

This is the normal life cycle of an agent, and it is worth remembering when you design one. Start at the lowest rung that satisfies the measure. Add capability only when a real user has a real complaint that the current rung cannot answer. That discipline is why a machine with almost no intelligence became one of the most successful robots ever built, while many cleverer prototypes never left the laboratory.

## Mini-Lab

**You need:** paper and a pen.

**Do this:**
1. Draw the agent-environment loop for an automatic door at a supermarket. Label the percept, the policy, the actuator and the environment.
2. Write a PEAS description for a robot that waters plants in an office.
3. Classify the door's environment on all five properties: observable, deterministic, static, discrete, single-agent.
4. Now classify the plant robot's environment. Then try a self-driving car. Write down the moment the method that worked for the door stops working.

**What you should see:** each step up in environment difficulty rules out a whole family of methods. The door needs a reflex. The car needs memory, probability and planning at the same time.

**Why it matters:** most failed robotics projects chose a method that did not match the environment. You have now practised the check that catches this before the money is spent.

## Recap and Questions

**Three things to remember**

1. Every AI system is an agent: percepts in, actions out, a policy in the middle, a performance measure above.
2. Environment properties — observability, determinism, dynamics, discreteness, number of agents — decide which methods are even possible.
3. Climb the agent ladder only as far as the performance measure requires.

**Check yourself**

1. A lift is an agent. Write its PEAS boxes and classify its environment.
2. Why does partial observability force an agent to keep memory?
3. Your cleaning robot scores 99% on "area cleaned" but users complain. What did the performance measure leave out?

**One thing to try next**

Pick any appliance with a sensor in your home. Write its policy as a table, exactly as the thermostat was written above. You will find at least one place where the table has a gap the designer never noticed.
