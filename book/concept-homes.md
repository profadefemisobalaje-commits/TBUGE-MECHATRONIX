# Concept Homes: Where Each Idea Is Taught Properly

With 48 courses, the same idea will come up many times. Readers notice when the same thing is explained twice in different words, and they lose trust. The rule is simple:

> **Every concept has one home course.** That course explains it fully. Every other course mentions it in one sentence and points back.

When you want to explain something, check this list first. If the concept already has a home, write a pointer instead of a paragraph. Add a new line whenever you create a new home.

## Foundations

| Concept | Home | Taught elsewhere as |
|---|---|---|
| Intelligence as behaviour; the AI effect; baselines | Course 1, ch. 1 | Course 15 (fairness of measures) |
| History of AI waves | Course 1, ch. 2 | Course 40, ch. 1 |
| Agents, PEAS, environment properties | Course 1, ch. 3 | Course 16, ch. 1; Course 29, ch. 9 |
| Search: BFS, DFS, A*, heuristics | Course 1, ch. 4 | Course 35 (robot planning); Course 44 (path planning) |
| Rules, inference, chaining | Course 1, ch. 5 | Course 32, ch. 2 (rule-based control) |
| Supervised learning basics, train/test split | Course 1, ch. 6 | Course 3 (full treatment) |
| Probability, Bayes' rule, base rates | Course 1, ch. 7 | Course 14, ch. 2 (sensor models); Course 34, ch. 2 |
| Images, spectrograms, tokens, embeddings | Course 1, ch. 8 | Course 4, ch. 2 (images as numbers); Course 5, ch. 3 (word vectors) |
| System chain, drift, monitoring | Course 1, ch. 9 | Course 45, ch. 9 (validation); Course 31, ch. 10 (maintenance) |
| Limits and risks overview | Course 1, ch. 10 | Course 40 (full treatment) |

## Bodies and motion

| Concept | Home | Taught elsewhere as |
|---|---|---|
| Robot anatomy, degrees of freedom | Course 2, ch. 2–3 | Course 47, ch. 4 |
| Motors, gearboxes, drivers | Course 2, ch. 4 | Course 47, ch. 5 |
| Sensors and signal conditioning | Course 2, ch. 5 | Course 8 (signal processing) |
| Rotation matrices, quaternions, transforms | Course 24, ch. 1–3 | Course 28, ch. 6 (tf); Course 46, ch. 2 |
| Forward and inverse kinematics, Jacobians | Course 24, ch. 4–6 | Course 41, ch. 3 (arms) |
| Wheeled kinematics, odometry | Course 19, ch. 3–4 | Course 34, ch. 3 |
| Dynamics and forces | Course 41, ch. 4 | Course 45, ch. 2 (physics engines) |

## Perception

| Concept | Home | Taught elsewhere as |
|---|---|---|
| Pixels, filtering, convolution | Course 4, ch. 2–3 | Course 8, ch. 6; Course 22, ch. 4 |
| Edges, corners, features | Course 4, ch. 4 | Course 31, ch. 4 |
| Segmentation and detection | Course 4, ch. 5–6 | Course 42, ch. 5 |
| Camera models and calibration | Course 14, ch. 3 | Course 31, ch. 3; Course 46, ch. 2 |
| Lidar, depth, stereo | Course 14, ch. 4 | Course 46, ch. 4 |
| Sensor fusion | Course 14, ch. 5 | Course 42, ch. 2 |
| Visual odometry and visual SLAM | Course 46, ch. 5–6 | Course 34, ch. 7 |
| Industrial inspection and measurement | Course 31 | Course 42, ch. 9 |

## Learning

| Concept | Home | Taught elsewhere as |
|---|---|---|
| Loss functions, overfitting, regularisation | Course 3, ch. 3, 6 | Course 22, ch. 3; Course 23, ch. 9 |
| Trees, forests, nearest neighbours | Course 3, ch. 7 | Course 23, ch. 5 |
| Cross-validation, evaluation | Course 3, ch. 8 | Course 42, ch. 10 |
| Neural networks, backpropagation | Course 11, ch. 1–5 | Course 22 (depth); Course 39 (robot learning) |
| Deep architectures, attention, transformers | Course 22, ch. 4–6 | Course 5, ch. 4 (language models) |
| Reinforcement learning, MDPs, Q-learning | Course 17 | Course 39, ch. 5 (on real robots) |
| Imitation and demonstration learning | Course 39, ch. 2–3 | Course 20, ch. 7 |
| Fuzzy sets and fuzzy control | Course 21 | Course 32, ch. 3 |
| Evolutionary methods | Course 37 | Course 30, ch. 6 (neural inspiration) |

## Systems and society

| Concept | Home | Taught elsewhere as |
|---|---|---|
| Control loops, PID, stability | Course 6 | Course 32 (intelligent control); Course 41, ch. 4 |
| Digital filters and sampling | Course 8 | Course 2, ch. 5 (practice) |
| Microcontrollers, interrupts, RTOS | Course 9 | Course 26, ch. 5 |
| Middleware, nodes, topics | Course 28 | Course 45, ch. 3 (simulation models) |
| IoT protocols and edge computing | Course 13 | Course 26, ch. 4 |
| Autonomy levels and safety architectures | Course 16 | Course 38, ch. 3 |
| SLAM, localisation, mapping | Course 34 | Course 19, ch. 6–7; Course 46, ch. 6 |
| Task and motion planning | Course 35 | Course 44 (paths); Course 20, ch. 6 |
| Multi-robot coordination | Course 33 | Course 27 (swarms) |
| Human-robot interaction methods | Course 10 | Course 36 (social robots) |
| VR displays, tracking, comfort | Course 25 | Course 45 (simulation) |
| Ethics frameworks and governance | Course 40 | Course 15 (applied); Course 38 (robots) |

## How to add a home

1. Choose the course where the concept is used most deeply, not the one where it first appears.
2. Write the full explanation there, with a worked example.
3. Add a row to this table.
4. In every other course, write one sentence and the pointer: "We met overfitting in Course 3, Chapter 6. Here we only need one fact from it: …"
