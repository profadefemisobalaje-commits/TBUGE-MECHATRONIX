# Joints, Degrees of Freedom and Workspace

Two robots can have the same number of joints and behave nothing alike. One can reach around a corner, one cannot; one can hold a tool at any angle, one can only point. The difference is not power or precision. It is geometry, and geometry can be counted.

This chapter gives you the counting. It is a small piece of mathematics with an unusual power: it tells you, before you build anything, how many independent motions a mechanism has, and therefore whether it can do the task you have in mind.

## Two Kinds of Joint

A joint is a connection that allows some relative motion and forbids the rest. Robots use a small vocabulary of them.

A **revolute** joint allows rotation about one axis: a door hinge, an elbow, a wheel on an axle. It is by far the most common, because bearings are cheap, precise and long-lived.

A **prismatic** joint allows sliding along one axis: a drawer, a telescopic mast, a linear actuator. It is common in gantries and 3D printers, less common in arms because linear bearings are bulkier than rotary ones for the same load.

A **spherical** joint allows rotation about three axes, like a shoulder. It is hard to build with precision, so robots usually make one from three revolute joints with their axes meeting at a point, which behaves like a ball joint but can be driven.

A **cylindrical** joint allows rotation and sliding about the same axis. A **planar** joint allows two translations and one rotation. A **free** joint allows everything, which is what happens when the gripper lets go.

Each joint type allows a certain number of independent motions, and that number is called its **freedom**: one for revolute and prismatic, three for spherical, and so on.

## Counting Freedom

The number of independent motions a whole mechanism can make is its **degrees of freedom**, usually written DOF. A rigid body floating in space has six: three translations and three rotations. Each joint removes some of those and leaves the rest.

The standard formula for a spatial mechanism is

> DOF = 6 × (number of links − 1) − sum over joints of (6 − freedom of that joint)

The subtraction of one link accounts for the ground, which is fixed. A planar mechanism, where everything moves in one plane, uses 3 instead of 6.

Test it on three examples.

**A two-link planar arm.** Three links (ground, upper arm, forearm) and two revolute joints. DOF = 3 × (3 − 1) − 2 × (3 − 1) = 6 − 4 = 2. Two joints, two freedoms. Obvious, and the formula agrees.

**A four-bar linkage.** Four links and four revolute joints, all planar. DOF = 3 × (4 − 1) − 4 × (3 − 1) = 9 − 8 = 1. Push one link and the rest follow; there is exactly one motion. This is why four-bars are used as mechanisms rather than as robots.

**A six-axis industrial arm.** Seven links including ground, six revolute joints. DOF = 6 × (7 − 1) − 6 × (6 − 1) = 36 − 30 = 6. Six joints, six freedoms, and the tool can be placed at any position and orientation inside the workspace. This is why six is the magic number in industrial robotics: fewer than six cannot reach every pose, and more than six is redundant, which is useful but complicated.

The formula has a famous failure. It gives the freedom of the *mechanism*, not of a given *pose*. Some poses are **singular**: configurations in which two joints line up and the mechanism loses a freedom in practice even though the count says otherwise. A six-axis arm at full stretch cannot move further outward, and a two-link arm with the elbow straight cannot move along the line of the arm. Every robot has singularities, and every robot program must avoid them. The volumes on kinematics return to this with the tools to compute them.

## Serial and Parallel

The joints of most robots are arranged in a chain, one after another, from base to tool. This is a **serial** mechanism: an arm, a leg, a crane. Its advantages are reach and dexterity; its disadvantages are that every joint carries the weight of everything beyond it, and every link's flexibility adds to the error at the tip.

A **parallel** mechanism connects the base to the platform with several chains at once. The Stewart platform, used in flight simulators and some machining centres, has six legs and six degrees of freedom. Its advantages are stiffness and accuracy for a given mass, because loads are shared and errors do not stack. Its disadvantages are a small workspace and a geometry that is difficult to design around.

| | Serial | Parallel |
|---|---|---|
| Structure | One chain, base to tool | Several chains, base to platform |
| Workspace | Large relative to size | Small relative to size |
| Stiffness | Lower; errors accumulate | Higher; loads shared |
| Typical use | Arms, legs, cranes | Simulators, precision stages, some machine tools |

The choice is a geometry decision, not a fashion. A robot that must reach into a car body needs the workspace of a serial arm. A machine that must hold a tool rigidly to a micron needs the stiffness of a parallel one.

## Reach and Workspace

The **workspace** is the set of all positions the tool can reach. For a two-link planar arm with lengths L1 and L2, it is the region between two circles: an outer radius of L1 + L2, an inner radius of the absolute difference between them. If the links are 0.4 m and 0.3 m, the tool can reach anything from 0.1 m to 0.7 m from the base, inside the swept area.

That inner hole is not a technicality. It means the arm cannot reach its own shoulder, which is fine for a welding robot and fatal for a machine that must place a part at the base. Designers fill the hole with a seventh joint, a different shoulder geometry, or a turning table that brings the work to the robot.

For a six-axis arm the workspace is a complicated, doughnut-like volume that is usually published as a diagram in the manual. Two numbers matter more than the shape: the maximum reach, and the payload at maximum reach. The first is geometry. The second is torque, and it is the subject of the next part of this volume.

## Wrist, Singularity and the Sixth Joint

In a six-axis arm, the first three joints usually decide where the tool is, and the last three decide which way it points. The last three are called the wrist, and in most industrial arms their axes meet at a single point, which makes the mathematics of orientation tractable and the mechanics of the wrist compact.

A spherical wrist has a characteristic weakness, and it is worth understanding because it causes real production problems. When the second wrist axis lines up with the first, two of the three rotations do the same thing, and the arm loses a degree of freedom in practice. The controller must then rotate one joint extremely fast to achieve a small change in orientation, or it must refuse the motion. Machinists call the region around this configuration a singularity, and programmers learn to keep the tool away from it.

The consequences are measurable. A wrist error of one degree, on a tool 0.5 m from the wrist centre, moves the tool by 0.5 × 0.0175 = 8.7 mm. Near a singularity, the geometry amplifies small commands into large joint motions, and the error grows the same way. A program that runs perfectly at the centre of the workspace can produce a wild swing at the edge of it, and the same program can behave differently on two machines of the same model if their zero offsets differ by a fraction of a degree.

The sixth joint has one more job that is easy to overlook: it sets the roll of the tool. A gripper that must approach a part from the side needs the roll to be free regardless of how the arm is positioned, and a task that ignores roll will work in half the reachable space and fail mysteriously in the other half. When a robot program behaves inconsistently across a workspace, the first thing to check is not the control loop but the orientation of the tool frame.

## Problems

1. Count the degrees of freedom of a planar mechanism with five links and five revolute joints. Then draw one and check whether the count matches your intuition.

2. A three-link planar arm has links of 0.3 m, 0.25 m and 0.15 m. What is the outer radius of its workspace and what is the inner radius?

3. A six-axis arm has six joints. Explain in one sentence why a task that only needs position, not orientation, might still use six.

4. A robot must place a component at a point 50 mm from the centre of its own base. Its two-link arm has links of 0.35 m and 0.30 m, so the inner radius is 0.05 m. Is the task possible? What would you change?

5. Find a picture of an industrial robot and count its joints. Then decide whether it is serial or parallel, and what its workspace probably looks like.
