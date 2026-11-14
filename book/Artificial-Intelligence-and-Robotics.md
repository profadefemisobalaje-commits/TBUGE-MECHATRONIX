# Artificial Intelligence and Robotics

### A Complete Four-Year Course in Plain English

**TBUGE Mechatronix - First Edition**

---

## Preface

This book contains a full four-year programme in artificial intelligence and robotics: 48 courses, 480 chapters, about 960,000 words. It was written for one reason. Most students who want to build intelligent machines meet two walls at the same time. The first wall is mathematics written for people who already understand it. The second wall is a pile of separate subjects — control, vision, learning, electronics, ethics — with nothing showing how they fit together.

This book removes both walls. Every idea is explained in plain English first, with a real example and real numbers. The mathematics arrives only after the reader can already see what it is for. And the courses are ordered so that each one uses what came before it, from "what does intelligence mean in a machine" in the first week to a defended final-year project at the end.

The course codes of the original syllabus (AI. 101, AI. 102 and so on) have been deliberately removed. In their place are plain course names and a simple running order: Course 1 to Course 48. A student should be able to open the table of contents and know what every course is about without decoding a numbering system.

## Who this book is for

- Students on a degree or diploma in AI, robotics, mechatronics, computer engineering or a related field.
- Teachers who need a clear, ordered explanation they can teach from.
- Self-taught makers who own a robot kit, a laptop, or neither, and want to understand the field properly.
- Engineers from other fields who need to talk to robotics teams without pretending.

You need secondary-school mathematics: fractions, percentages, a little algebra, the idea of a graph. You need no programming experience for Courses 1 and 2. From Course 3 onwards, examples use short Python, and a beginner can follow them by typing and running, not by memorising syntax.

## How the book is organised

The book follows an eight-semester programme:

| Stage | Courses | Focus |
|---|---|---|
| Year 1, Semester 1 | 1–6 | Foundations: AI, robots, learning, vision, language, control |
| Year 1, Semester 2 | 7–12 | Tools: algorithms, signals, embedded systems, interaction, neural networks, graphics |
| Year 2, Semester 1 | 13–18 | Systems: IoT, perception, ethics, autonomy, reinforcement learning, architecture |
| Year 2, Semester 2 | 19–24 | Movement and learning: mobile robots, AI for robots, fuzzy logic, deep learning, patterns, kinematics |
| Year 3, Semester 1 | 25–30 | Experience and nature: VR, cyber-physical systems, swarms, robot software, cognition, bio-inspiration |
| Year 3, Semester 2 | 31–36 | Applied intelligence: machine vision, intelligent control, multi-robot teams, localisation, planning, social robots |
| Year 4, Semester 1 | 37–42 | Advanced practice: evolution, robot ethics, robot learning, AI ethics, manipulation, perception |
| Year 4, Semester 2 | 43–48 | Mastery: navigation, path planning, simulation, robot vision, design, capstone project |

Every course is a self-contained block of about 20,000 words in ten chapters. Each chapter takes about three hours of study and follows the same eight-part shape:

1. **Opening** - what you will be able to do.
2. **Big Picture** - the one idea, in a paragraph anyone can follow.
3. **Key Words** - the four to six terms you need.
4. **The Explanation** - three steps from easy to hard, with worked examples and real numbers.
5. **Where It Goes Wrong** - the mistakes students actually make, and the fix for each.
6. **Case Note** - a true story from industry or research, and the lesson it carries.
7. **Mini-Lab** - something to do in under an hour, usually with no equipment.
8. **Recap and Questions** - three things to remember, three questions, one next step.

Each course also has a short introduction, and a review file with twelve questions, worked answers, three lab assignments, a project brief, a glossary and further reading.

Because the shape never changes, you always know where you are, and you can revise a whole course in an afternoon by reading only the Big Picture and Recap sections.

## How to read a chapter

Read it three times, and the three readings are short.

**First reading (20 minutes).** Read straight through without stopping. Do not take notes. Let the shape of the idea land.

**Second reading (60 minutes).** Now work. Do the worked example yourself on paper with the numbers covered. Attempt the three questions at the end before looking at anything else. If you get a question wrong, read the step it came from, not the whole chapter.

**Third reading (week later, 10 minutes).** Read only the Key Words and the Recap. If a term has gone cold, that is the one to revise. This is the reading that moves knowledge into long-term memory.

Do the mini-lab. Reading about a PID controller is not the same as watching a motor overshoot and settle. Every lab in this book was chosen so that it can be done with a laptop, a phone, paper, or the cheapest parts available — because the student who cannot afford a robot still deserves to learn robotics.

## A note on simple English

The language in this book is deliberately plain. Sentences are short. Every technical word is defined the moment it appears, in bold, and then used freely. Every number has a unit. Every formula is introduced by a sentence that says what it does before it says what it is.

This is not because the material is simple. It is because hard material explained in hard language teaches nothing. The full rules are in `03-style-guide.md`; the plan for writing the remaining courses is in `02-how-to-write-this-book.md`.

## The promise of the book

If you work through all 48 courses, you will be able to:

- explain how an intelligent system senses, decides and acts;
- build and train models, and know when to distrust them;
- program a robot to perceive, move, plan and manipulate;
- design a robot system that is safe, tested and honest about its limits;
- reason clearly about the ethical questions the work raises;
- and finish a substantial project of your own, documented and defended.

That is the promise. The rest of the book is how it is kept.


---

<!-- Generated by tools/booktool.py toc. Edit book/outline.json, not this file. -->

# Table of Contents

*Artificial Intelligence and Robotics: A Complete Four-Year Course in Plain English*

The book has **48 courses** and **480 chapters**. Every course is a self-contained block of about 20,000 words: a course introduction, 10 chapters of about 1,800 words each, and a review with assessment and glossary.

Each chapter follows the same eight-part shape, so you always know what is coming: Opening, Big Picture, Key Words, The Explanation, Where It Goes Wrong, Case Note, Mini-Lab, and Recap and Questions.


## Year 1 - Semester 1

### Course 1: Introduction to Artificial Intelligence

*Understand what AI is really doing, and build your first small intelligent program.*

1. What Intelligence Means in Machines
2. A Short History of Thinking Machines
3. Agents: The Core Idea of AI
4. Searching for Solutions
5. Knowledge, Rules and Reasoning
6. Learning from Data: A First Look
7. Uncertainty and Probability
8. Language, Vision and Sound: A First Look
9. AI Systems in the Real World
10. Limits, Risks and the Road Ahead

### Course 2: Robotics Fundamentals

*Know every main part of a robot and how those parts work together.*

1. What a Robot Is
2. The Parts of a Robot
3. Joints, Links and Degrees of Freedom
4. Actuators and Motors
5. Sensors and Signals
6. Power, Wiring and Electronics
7. Simple Robot Behaviour
8. Safety and Failure
9. Building and Testing Your First Robot
10. Robots in Industry and Daily Life

### Course 3: Machine Learning

*Train models that predict, classify and generalise, and know when to distrust them.*

1. Learning from Examples
2. Data: Collecting, Cleaning and Splitting
3. Measuring How Wrong a Model Is
4. Linear Models for Prediction
5. Classification and Decision Boundaries
6. Overfitting and Regularisation
7. Trees, Forests and Nearest Neighbours
8. Model Evaluation and Cross-Validation
9. Features and Pipelines
10. Deploying and Maintaining Models

### Course 4: Computer Vision

*Turn pixel numbers into useful information about objects, motion and depth.*

1. How Machines See
2. Images as Numbers
3. Filtering and Convolution
4. Edges, Corners and Features
5. Segmentation: Separating What Is in the Picture
6. Object Detection
7. Tracking Across Frames
8. Depth and 3D Vision
9. Recognition with Learned Features
10. Building a Vision Application

### Course 5: Natural Language Processing

*Make software that reads, understands and writes human language.*

1. Language as Data
2. Cleaning Text and Splitting It into Tokens
3. Words as Vectors
4. Language Models
5. Classifying Text
6. Extracting Information from Text
7. Machine Translation
8. Question Answering and Chat
9. Speech Interfaces
10. Evaluation, Bias and Safety in Language Systems

### Course 6: Control Systems

*Keep a real system on target using feedback, from a motor to a drone.*

1. What Control Means
2. Modelling a System
3. Open Loop and Closed Loop
4. Sensors, Actuators and Error
5. PID Control
6. Stability
7. Frequency Response
8. State Space Models
9. Digital Control
10. Control in Robots and Tuning Practice


## Year 1 - Semester 2

### Course 7: Data Structures and Algorithms

*Choose the right way to store and process data, and know the cost of each choice.*

1. Why Structure Matters
2. Arrays, Lists and Strings
3. Stacks and Queues
4. Hash Tables
5. Trees
6. Heaps and Priority Queues
7. Graphs
8. Sorting and Searching
9. Algorithm Complexity
10. Design Patterns for Robot Software

### Course 8: Digital Signal Processing

*Clean, measure and interpret the sensor and audio signals a robot lives on.*

1. Signals in the Real World
2. Sampling and Quantisation
3. The Frequency View
4. The Fourier Transform
5. Filters
6. Convolution and Correlation
7. Noise and Smoothing Sensor Data
8. Designing Digital Filters
9. Image and Audio Signals
10. Real-Time Signal Processing for Robots

### Course 9: Embedded Systems

*Program the small computers inside machines, where timing and memory are tight.*

1. What an Embedded System Is
2. Microcontrollers and Their Pins
3. Reading Sensors
4. Driving Actuators
5. Timers, Interrupts and Real Time
6. Communication Buses
7. Memory, Power and Reliability
8. Real-Time Operating Systems
9. Testing Embedded Code
10. From Prototype to Product

### Course 10: Human-Robot Interaction

*Design robot behaviour that people understand, trust and want to use.*

1. People Meeting Machines
2. Studying How People Use Robots
3. Communication Channels
4. Social Signals and Expression
5. Voice and Speech Interaction
6. Trust, Comfort and Anthropomorphism
7. Teleoperation and Shared Control
8. Designing an Interaction
9. Evaluating an Interaction
10. Field Studies and the Ethics of Use

### Course 11: Neural Networks

*Build and train networks from a single artificial neuron to a working deep model.*

1. From Neurons to Equations
2. The Perceptron
3. Layers and Activation Functions
4. Training by Gradient Descent
5. Backpropagation
6. Making Training Work
7. Regularisation and Dropout
8. Convolutional Networks
9. Recurrent and Sequence Networks
10. From Network to System

### Course 12: Computer Graphics

*Draw, light and animate 3D worlds on a screen, and use them to see inside a robot.*

1. The Graphics Pipeline
2. Points, Vectors and Transforms
3. Modelling 3D Objects
4. Cameras and Projection
5. Lighting and Shading
6. Textures and Materials
7. Rendering Techniques
8. Animation
9. Real-Time Graphics and the GPU
10. Graphics for Robot Simulation and Visualisation


## Year 2 - Semester 1

### Course 13: Internet of Things

*Connect many small devices into systems that sense, report and act together.*

1. What the Internet of Things Is
2. Devices, Sensors and Nodes
3. Networks for Small Devices
4. Protocols: MQTT, CoAP and REST
5. Edge, Fog and Cloud
6. Data Pipelines
7. Time, Synchronisation and Reliability
8. Security and Privacy
9. Dashboards and Applications
10. The Internet of Things for Robots

### Course 14: Robotic Perception

*Turn noisy sensor data into a reliable picture of the world around a robot.*

1. Perception as Inference
2. Sensor Models and Uncertainty
3. Camera Geometry
4. Lidar and Depth Sensing
5. Fusing Sensors
6. Detecting and Classifying Objects
7. Mapping the Environment
8. Tracking Moving Things
9. Perception for Manipulation
10. Building and Testing a Perception Stack

### Course 15: Ethics in AI and Robotics

*Recognise ethical problems early and handle them with clear, defensible reasoning.*

1. Why Ethics Comes First
2. Moral Frameworks in Plain Language
3. Bias and Fairness
4. Privacy and Data
5. Accountability and Responsibility
6. Transparency and Explainability
7. Safety and Risk
8. Autonomy and Human Control
9. Regulation and Standards
10. Applying Ethics in Practice

### Course 16: Autonomous Systems

*Understand how a machine senses, decides and acts with little or no human help.*

1. What Makes a System Autonomous
2. Levels of Autonomy
3. Sensing the World
4. Deciding What to Do
5. Planning and Acting
6. Navigation and Localisation
7. Safety Architectures
8. Human Oversight
9. Testing Autonomous Systems
10. Case Studies: Cars, Drones and Robots

### Course 17: Reinforcement Learning

*Train agents that improve by trying, failing and being rewarded.*

1. Learning by Trial and Error
2. Rewards and Returns
3. Markov Decision Processes
4. Dynamic Programming
5. Monte Carlo Methods
6. Temporal Difference Learning
7. Q-Learning and SARSA
8. Policy Gradients
9. Deep Reinforcement Learning
10. Practical Training and Pitfalls

### Course 18: Computer Architecture

*Know how processors, memory and buses work, and why it decides what AI can run.*

1. Inside a Computer
2. Numbers, Bits and Data Representation
3. The Processor and the Instruction Cycle
4. Pipelining
5. Memory Hierarchy and Caches
6. Input, Output and Buses
7. Instruction Sets
8. Parallelism and Multi-Core Computing
9. Accelerators for AI
10. Architecture Choices for Robots


## Year 2 - Semester 2

### Course 19: Mobile Robotics

*Make a wheeled or legged robot move, know where it is and go where you ask.*

1. Robots That Move
2. Wheels, Tracks and Legs
3. Kinematic Models of Mobile Robots
4. Odometry and Dead Reckoning
5. Sensors for Mobile Robots
6. Localisation
7. Mapping
8. Path Planning and Path Following
9. Obstacle Avoidance and Behaviour
10. Field Deployment

### Course 20: AI for Robotics

*Apply AI methods to the hard problem of acting correctly in the physical world.*

1. Where AI Meets the Physical World
2. Representing the Robot's World
3. Planning with AI
4. Learning for Control
5. Perception Meets Decision Making
6. Task and Motion Planning
7. Learning from Demonstration
8. Foundation Models for Robots
9. Integration Architectures
10. Evaluating AI on Real Robots

### Course 21: Fuzzy Logic

*Reason with degrees of truth instead of hard yes-or-no answers.*

1. Beyond True and False
2. Fuzzy Sets
3. Membership Functions
4. Fuzzy Rules
5. Inference
6. Defuzzification
7. Designing a Fuzzy Controller
8. Tuning and Testing
9. Fuzzy Logic with Other AI Tools
10. Case Studies in Machines

### Course 22: Deep Learning

*Understand and train modern deep models, including transformers, and deploy them.*

1. Why Depth Helps
2. Data and Compute
3. Training Deep Networks
4. Convolutional Architectures
5. Sequence Models
6. Attention and Transformers
7. Generative Models
8. Transfer Learning
9. Model Compression and Deployment
10. Deep Learning Projects

### Course 23: Pattern Recognition

*Find structure in data and decide which class a new sample belongs to.*

1. Finding Patterns
2. Features and Representations
3. Statistical Decision Theory
4. Bayesian Classification
5. Discriminant Functions
6. Clustering
7. Dimensionality Reduction
8. Patterns in Time and Sequences
9. Evaluation and Error Analysis
10. Pattern Recognition in Robotics

### Course 24: Robot Kinematics

*Compute exactly where a robot's arm or body will be, and how to reach a pose.*

1. Describing Position and Orientation
2. Rotation Matrices and Quaternions
3. Frames and Transforms
4. Forward Kinematics
5. Inverse Kinematics
6. Velocity and Jacobians
7. Singularities
8. Workspace and Reachability
9. Kinematics for Mobile and Parallel Robots
10. Kinematics in Practice


## Year 3 - Semester 1

### Course 25: Virtual Reality

*Build immersive 3D experiences, and use them for robot training and control.*

1. What Virtual Reality Is
2. Human Senses and Perception
3. Displays, Lenses and Optics
4. Tracking
5. Interaction and Controllers
6. 3D Content and Engines
7. Immersion and Comfort
8. Building a Virtual Reality Application
9. Virtual Reality for Robot Teleoperation and Training
10. Testing and Ethics in Virtual Reality

### Course 26: Cyber-Physical Systems

*Design systems where software and physical processes are tightly joined.*

1. The Physical and the Digital
2. Modelling Physical Processes
3. Sensing and Actuation Loops
4. Networking and Time
5. Embedded Computing in Cyber-Physical Systems
6. Verification and Validation
7. Security of Cyber-Physical Systems
8. Reliability and Fault Tolerance
9. Smart Grids, Factories and Cities
10. Robots as Cyber-Physical Systems

### Course 27: Swarm Robotics

*Get simple robots to achieve complex group behaviour with local rules.*

1. Many Simple Robots
2. Emergence and Self-Organisation
3. Local Rules and Global Behaviour
4. Communication in Swarms
5. Aggregation and Clustering
6. Foraging and Task Allocation
7. Formation and Flocking
8. Scalability and Robustness
9. Simulating Swarms
10. Real Swarm Robots and Applications

### Course 28: Robot Operating Systems

*Build a complete robot software system with nodes, topics, transforms and simulation.*

1. Why Robots Need Middleware
2. Nodes, Topics and Messages
3. Services and Actions
4. Packages and Workspaces
5. Launch Files and Parameters
6. Transforms and Time
7. Simulation
8. Visualisation and Debugging Tools
9. Building a Complete Robot Stack
10. Best Practices and Real Deployments

### Course 29: Cognitive Robotics

*Give robots knowledge, memory and reasoning that resemble human thinking.*

1. Machines That Know
2. Representing Knowledge
3. Reasoning and Planning as Thinking
4. Memory and Learning
5. Attention and Perception
6. Development and Embodiment
7. Language and Thought in Robots
8. Models of Human Cognition
9. Cognitive Architectures
10. Testing Cognitive Claims

### Course 30: Biologically Inspired Robotics

*Copy the best ideas from animals and plants to build better machines.*

1. Learning from Nature
2. Animal Movement and Locomotion
3. Legs, Fins and Wings
4. Muscles, Springs and Compliance
5. Sensing Like Animals
6. Neural Inspiration
7. Swarms, Colonies and Flocks
8. Soft Robotics
9. Bio-Inspired Control
10. Building and Evaluating Bio-Inspired Robots


## Year 3 - Semester 2

### Course 31: Machine Vision

*Build industrial vision systems that measure, inspect and guide machines.*

1. Industrial Vision Systems
2. Cameras, Lenses and Lighting
3. Calibration
4. Measurement and Inspection
5. Defect Detection
6. Code Reading and Alignment
7. Vision-Guided Motion
8. Speed, Repeatability and Accuracy
9. Integration on the Factory Floor
10. Case Studies and Maintenance

### Course 32: Intelligent Control Systems

*Combine control theory with learning, rules and optimisation to handle hard plants.*

1. From Control to Intelligent Control
2. Expert and Rule-Based Control
3. Fuzzy Control Systems
4. Neural Control
5. Learning-Based Control
6. Adaptive and Robust Control
7. Hierarchical and Hybrid Control
8. Optimisation-Based Control
9. Intelligent Control in Robots
10. Choosing and Validating a Controller

### Course 33: Multi-Robot Systems

*Coordinate several robots so they finish one task as a team.*

1. Several Robots, One Task
2. Coordination Basics
3. Communication Topologies
4. Task Allocation
5. Formation Control
6. Consensus and Distributed Decisions
7. Path Coordination and Collision Avoidance
8. Centralised versus Distributed
9. Simulation and Experimentation
10. Applications and Open Problems

### Course 34: Robot Localisation and Mapping

*Solve the chicken-and-egg problem of knowing where you are while drawing the map.*

1. The Chicken-and-Egg Problem
2. Probability for Localisation
3. Odometry and Motion Models
4. Range Sensing and Landmarks
5. Kalman and Particle Filters
6. Mapping with Known Poses
7. Simultaneous Localisation and Mapping
8. Loop Closure
9. Map Representations
10. Practical Localisation and Mapping Systems

### Course 35: Robotics Planning

*Turn a goal into a safe, feasible sequence of robot actions.*

1. What Planning Means for Robots
2. State Spaces
3. Search-Based Planning
4. Sampling-Based Planning
5. Trajectory Planning
6. Task Planning
7. Planning under Uncertainty
8. Multi-Robot and Dynamic Planning
9. Plan Execution and Recovery
10. Planning in Practice

### Course 36: Social Robotics

*Design robots that behave appropriately around people over weeks, not minutes.*

1. Robots Among People
2. Social Norms and Cues
3. Appearance and Design
4. Nonverbal Behaviour
5. Conversation and Companionship
6. Robots in Care, Education and Service
7. Cultural Differences
8. Measuring Social Acceptance
9. Long-Term Interaction
10. Responsible Social Robotics


## Year 4 - Semester 1

### Course 37: Evolutionary Robotics

*Let algorithms design robot bodies and brains by survival of the fittest.*

1. Design by Evolution
2. Encoding a Robot
3. Fitness and Selection
4. Genetic Algorithms
5. Evolving Controllers
6. Evolving Bodies
7. Co-Evolution and Novelty
8. Simulation versus Reality
9. Analysing Evolved Solutions
10. Case Studies

### Course 38: Robot Ethics

*Decide what a robot may do, who is responsible, and how to prove it was right.*

1. Ethics for Machines That Act
2. Agency and Autonomy
3. Harm, Safety and Liability
4. Deception and Anthropomorphism
5. Privacy in Robotic Systems
6. Military and Policing Robots
7. Care, Health and Work
8. Consent and Human Dignity
9. Rules, Codes and Certification
10. Designing Ethical Robots

### Course 39: Robot Learning

*Make robots improve with experience, demonstration and their own data.*

1. Robots That Improve with Experience
2. Learning from Demonstration
3. Imitation Learning
4. Self-Supervised Robot Learning
5. Reinforcement Learning on Real Robots
6. Representing Skills
7. Simulation-to-Reality Transfer
8. Learning with Limited Data
9. Safety in Learning Systems
10. Evaluating Robot Learning

### Course 40: AI Ethics

*Judge AI systems fairly, explain them, and govern them inside real organisations.*

1. Why AI Ethics Matters Now
2. Values, Norms and Law
3. Fairness and Discrimination
4. Privacy and Surveillance
5. Transparency and Explainability
6. Accountability and Governance
7. Misuse, Manipulation and Deepfakes
8. Labour, Economy and Society
9. Global Perspectives and Regulation
10. Building Ethical AI Practice

### Course 41: Robot Manipulation

*Give a robot arm the ability to grasp, move and assemble real objects.*

1. Arms, Hands and Tasks
2. Grasping
3. Kinematics for Manipulation
4. Dynamics and Forces
5. Force and Tactile Sensing
6. Motion Planning for Arms
7. Grasp Planning and Grasp Learning
8. Assembly and Contact Tasks
9. Mobile Manipulation
10. Benchmarking Manipulation

### Course 42: Robot Perception

*Build perception that is accurate enough, fast enough and honest about uncertainty.*

1. Perception for Action
2. Multi-Sensor Fusion
3. 3D Scene Understanding
4. Object Pose Estimation
5. Semantic and Instance Understanding
6. Tracking and Prediction
7. Active Perception
8. Perception for Human-Robot Interaction
9. Real-Time Constraints
10. Validating Perception Systems


## Year 4 - Semester 2

### Course 43: Robot Navigation

*Take a robot from a start point to a goal, safely, in a real and changing place.*

1. The Navigation Problem
2. Map Representations
3. Global Path Planning
4. Local Planning and Control
5. Obstacle Avoidance
6. Localisation for Navigation
7. Navigation in Dynamic Environments
8. Outdoor and Off-Road Navigation
9. Multi-Modal Navigation
10. Field Testing and Reliability

### Course 44: Robot Path Planning

*Compute good paths and smooth trajectories under real constraints.*

1. Paths, Routes and Trajectories
2. Graph Search Methods
3. Heuristic Search
4. Sampling-Based Planners
5. Optimisation-Based Planning
6. Kinodynamic Planning
7. Planning with Uncertainty and Risk
8. Smoothing and Trajectory Generation
9. Replanning and Recovery
10. Tools and Benchmarks

### Course 45: Robot Simulation

*Test robots in software before they touch metal, and transfer the results to reality.*

1. Why Simulate
2. Physics Engines
3. Building a Robot Model
4. Building a World
5. Sensors in Simulation
6. Simulating Contact and Friction
7. Simulation-to-Reality Transfer
8. Running Experiments at Scale
9. Validation and Metrics
10. Simulation in the Product Lifecycle

### Course 46: Robot Vision

*Make vision work on a moving, vibrating, sunlit robot in the real world.*

1. Vision on a Moving Robot
2. Camera Models and Calibration
3. Handling Motion and Blur
4. Stereo and Depth
5. Visual Odometry
6. Visual Simultaneous Localisation and Mapping
7. Onboard Object Detection
8. Vision for Manipulation and Navigation
9. Embedded Vision Implementation
10. Robustness and Field Testing

### Course 47: Robot Design

*Turn a need into a safe, buildable, affordable robot design.*

1. Design as a Process
2. Requirements and Constraints
3. Concept Generation
4. Mechanical Structure
5. Actuator and Transmission Selection
6. Electronics and Power
7. Software Architecture
8. Prototyping and Testing
9. Reliability, Safety and Cost
10. From Design to Delivered Robot

### Course 48: Capstone Design Project

*Plan, build, test and defend one complete AI and robotics project of your own.*

1. Choosing a Project
2. Defining Requirements
3. Literature and Prior Art
4. System Design
5. Building the Prototype
6. Testing and Iteration
7. Data, Logging and Evaluation
8. Writing the Report
9. Presenting and Demonstrating
10. From Project to Product or Research


---

## Back Matter

1. Master Glossary (every bold key word in the book, in one place)
2. Formula Sheet (the maths worth remembering, with plain-English notes)
3. Lab and Project Index
4. Answers to Check-Yourself Questions
5. Further Reading, by Course
6. Index


---



# Course 1: Introduction to Artificial Intelligence


---

# What Intelligence Means in Machines

> Course 1: Introduction to Artificial Intelligence - Chapter 1 of 10

## Opening

By the end of this chapter you can say what intelligence means in a machine, test that claim with a task and a number, and explain why "AI" keeps changing its meaning.

In 1997, a computer called Deep Blue beat the world chess champion. People said it was a great day for artificial intelligence. Ten years later, the same program running on a free phone app was described as "just a chess engine", not as intelligence at all. Nothing about the program had changed. Only our expectations had. This happens every few years, and it will happen to you too. It is the first thing you need to understand before you write a single line of AI code.

## Big Picture

Intelligence, in this book, is not a mysterious substance inside a head. It is a **behaviour**: the ability to choose actions that reach a goal, in situations you have not seen before. A calculator is fast but it never chooses. It does exactly what it is told. A self-driving car chooses — sometimes badly, but it chooses — and that difference is the whole subject.

When we say a machine is intelligent, we mean three things at once. It can **sense** something about the world. It can **decide** what to do. It can **act**, and then see what happened. Sensing, deciding and acting in a loop, in an uncertain world, is the core of every system in this book, from a robot arm to a language model.

This definition has a useful side effect. It makes intelligence something you can measure. If intelligence is behaviour, then you can build a test, run it, and count. You do not have to argue about whether the machine "really understands". You can ask a much better question: on this task, with this measure, how well does it do compared with a person, and compared with a stupid guess?

## Key Words

- **Intelligence** - the ability to choose actions that reach a goal in unfamiliar situations.
- **Artificial intelligence (AI)** - the study and construction of machines that sense, decide and act.
- **Agent** - anything that senses its world and acts on it. A robot is an agent. So is a spam filter.
- **Narrow AI** - a system that is good at one task and useless outside it.
- **General AI** - a system that can handle any task a person can. No such system exists today.
- **Baseline** - the score a stupid, simple method gets. Every intelligent result must be compared with it.
- **The AI effect** - the habit of calling a solved problem "not really AI" once it works.

## The Explanation

### Step 1 - Intelligence is behaviour you can see

Think of two people. One has memorised the bus timetable and recites it perfectly. The other has never seen the city, has no map, and is dropped in a strange street with a phone that has died. The first person is impressive. The second person finds their way home by asking, remembering landmarks and trying streets. Which one would you call intelligent?

Most people pick the second, because intelligence shows up when the situation is new. That is why the definition stresses *unfamiliar situations*. A system that works only on the exact data it was trained on has not shown intelligence. It has shown memory.

This gives us a practical test with three questions:

1. What can the system sense?
2. What actions can it choose from?
3. In how many *new* situations does it still reach the goal?

A chess engine senses the board and chooses a move. Inside chess it is extraordinary. Outside chess it cannot do anything, because its sensors and actions exist only on a board. That is **narrow AI**, and almost everything you will meet in this book is narrow.

### Step 2 - The same machine, a different name

AI has a strange habit: as soon as a problem is solved, we stop calling it AI.

Optical character recognition — turning a photo of text into typed letters — was a research triumph in the 1980s. Today it happens in your phone's camera app and nobody calls it AI. Route finding was a landmark of the 1960s. Today your maps app does it and you call it "the maps app". Speech recognition was a career's work. Today it is a small button.

This is **the AI effect**. There are two reasons for it. First, once we understand how something works, it stops feeling magical; it becomes engineering. Second, marketing language moves on to whatever is not yet solved, because that is where attention and money are.

The practical lesson: never accept the label "AI" as evidence of anything. Ask what the system senses, what it can do, and how it was tested. A system called "AI-powered" may be three rules in a spreadsheet. A system called "a sorting script" may contain a serious neural network.

### Step 3 - Measure it, or it means nothing

Suppose you build a filter that decides whether an email is spam. You test it on 1,000 emails and it is right 90% of the time. Is that good?

You cannot tell yet, because you do not know the **baseline**. Imagine that only 100 of the 1,000 emails are spam, and 900 are normal. A filter that says "not spam" to everything — a filter with no intelligence at all — is right 900 times out of 1,000. That is also 90%. Your clever filter has learned nothing that a brick could not do.

This is why the book insists on a baseline in every experiment. The baseline is the number a lazy method gets, and it is often shockingly high.

| Method | Correct out of 1,000 | Accuracy |
|---|---|---|
| Say "not spam" always | 900 | 90% |
| Say "spam" always | 100 | 10% |
| Your first filter | 900 | 90% |

Now look at the spam itself, not the whole pile. The filter catches 60 of the 100 spam emails and wrongly blocks 30 normal ones. In the spam group, it is right 60% of the time. In the normal group, it is right (900 − 30)/900 = 96.7% of the time. Those two numbers tell a completely different story from "90% accurate". A filter that misses 40 of every 100 spam emails, and blocks 30 real messages, would annoy most users.

So we never report one number. We report the score, the baseline, and the mistakes by type. Only then does "90%" mean anything.

A useful habit: when someone shows you a result, ask three questions. What is the baseline? What is the worst mistake this system can make? Who paid for the test? The third question is not cynicism. It is how you find out which cases were left out.

## Where It Goes Wrong

**Mistake 1 - Thinking AI means "like a human".** A system can be superhuman at one task and hopeless at everything else. Deep Blue beat a champion and could not tell you what a chair is. *Fix:* describe what the system does, not what it resembles. Say "a chess-playing program", not "a thinking machine".

**Mistake 2 - Trusting a single accuracy number.** As the spam example shows, 90% can mean "does nothing". *Fix:* always compute the baseline first, then split the errors by type.

**Mistake 3 - Confusing automation with intelligence.** A washing machine runs a fixed cycle. It senses almost nothing and chooses nothing. It is automatic, not intelligent. *Fix:* use the three questions — what does it sense, what can it choose, how does it do in new situations?

**Mistake 4 - Believing the field is new.** The questions were asked in the 1950s. Only the computing power and the data are new. *Fix:* read Chapter 2 before making claims about what is unprecedented.

**Mistake 5 - Letting the demo stand in for the product.** A video of a robot walking on a smooth floor says nothing about stairs, rain or mud. *Fix:* ask for the failure rate, on which data, measured by whom.

## Case Note

In 2016, a group of researchers asked a simple question about image classifiers: why did the model say "wolf"? They took a network that appeared to tell huskies from wolves with high accuracy and analysed which parts of each picture pushed the decision. The answer was uncomfortable. The network was not looking at the animal at all. It was looking at snow. Almost every wolf photograph in the dataset had been taken outdoors in winter, so "snow on the ground" predicted "wolf" almost perfectly. Husky photographs, mostly taken indoors or in summer, had no snow.

The model was accurate on the test set, because the test set was drawn from the same photographs with the same accidental shortcut. It would have failed on a wolf photographed in a desert, and it would have failed on a husky standing in snow. Nobody had checked, because the number looked good.

This is the clearest possible illustration of this chapter's definition. The system was not intelligent in any useful sense. It had found a correlation that happened to hold in one collection of pictures, and it would have broken the moment the situation changed, exactly as the definition in the Big Picture section predicts.

The lesson for your own work: whenever a model performs surprisingly well, ask what it could be using that you did not intend. Then design a test where that shortcut is unavailable. If performance collapses, you have found the shortcut, and you have learned more than a hundred more training examples would have taught you.

## Mini-Lab

**You need:** paper, a pen, and 20 short messages (or just the table below).

**Do this:**
1. Write down five "AI" systems you used this week. Next to each, fill three boxes: what it senses, what it chooses, what counts as its goal.
2. Mark each one narrow or general.
3. Imagine a test for the first one. Write the task, the measure, and a stupid baseline that uses no learning at all.
4. Predict the baseline score before you imagine the clever system's score. If your clever system does not clearly beat the baseline, your test is too easy.

**What you should see:** at least one system you thought was intelligent turns out to sense almost nothing, and at least one "boring" system — a maps app, a photo organiser — turns out to be doing serious sensing and choosing.

**Why it matters:** you have just done the first real job of an AI engineer. Not building a model. Deciding what would count as success.

## Recap and Questions

**Three things to remember**

1. Intelligence is behaviour: sensing, deciding and acting to reach a goal in new situations.
2. The AI effect means the label "AI" proves nothing. Look at the sensing, the actions and the testing.
3. A score without a baseline is not a result.

**Check yourself**

1. A program predicts tomorrow's weather correctly 70% of the time. What is the baseline, and why does it matter?
2. Give one system that is automatic but not intelligent, and one that is intelligent but not automatic. Explain the difference in one sentence each.
3. Your robot vacuum cleans 95% of the floor area it covers. Why is that number not the same as "cleans 95% of your home"?

**One thing to try next**

Take the last "AI" advertisement or news story you saw. Write its claim in the three-question form: what does it sense, what does it choose, how was it tested? You will be surprised how often one of the three boxes is empty.


---

# A Short History of Thinking Machines

> Course 1: Introduction to Artificial Intelligence - Chapter 2 of 10

## Opening

By the end of this chapter you can place any AI system on a timeline, name the idea it depends on, and explain why the field has repeatedly promised too much and delivered in narrow pieces.

In the summer of 1956, a small group of researchers met at Dartmouth College in the United States and wrote a proposal with a remarkable claim: that every feature of intelligence could, in principle, be described so precisely that a machine could simulate it. They expected the work to take a generation. Seventy years later, the work is still going, and the argument about how close we are has not settled. Knowing that story is not decoration. The same three ideas have been fighting for attention since the 1950s, and the argument you hear today is the same argument, with faster computers.

## Big Picture

The history of AI is a repeating loop of four steps: a big promise, real success on narrow problems, a wall where the method runs out of power, and a pivot to a new idea. Three main ideas have taken turns at the front: **rules**, **learning**, and **scale**. Rules say: write down what an expert knows and let the machine follow the rules. Learning says: give the machine examples and let it find the pattern. Scale says: make the network and the data enormous and let the pattern find itself.

Each idea worked brilliantly inside its limits and failed outside them. Each time a wave broke, journalists wrote that AI was finished. Each time, the field quietly kept the useful parts and moved on. Today's systems are not a replacement for the old ideas; they are rules, learning and scale stacked on top of each other. When you debug a modern robot, you will usually find all three in the same program.

## Key Words

- **Turing test** - a test of machine intelligence by conversation, proposed by Alan Turing in 1950.
- **Symbolic AI** - AI built on written rules and symbols, dominant from the 1950s to the 1980s.
- **Expert system** - a program holding a specialist's rules, used in medicine and industry in the 1970s and 1980s.
- **AI winter** - a period of lost funding and lost interest after a wave of promises failed.
- **Connectionism** - the idea that intelligence comes from many simple connected units, the root of neural networks.
- **Deep learning** - neural networks with many layers, trained on large data, dominant since about 2012.

## The Explanation

### Step 1 - The dream and the test (1936-1956)

The story starts with mathematics, not machines. In 1936, Alan Turing described a machine that could compute anything computable by following simple steps on a tape. That gave people a precise meaning for "a procedure a machine can carry out". Once you have that, the question "can a machine think?" stops being poetry and becomes engineering.

Turing's 1950 paper, *Computing Machinery and Intelligence*, did something clever. Instead of defining thinking, he replaced the question with an experiment. Put a person, a machine and a judge in separate rooms. Let the judge type questions to both. If the judge cannot reliably tell which is which, said Turing, we have no good reason to deny the machine intelligence.

That move — replace a hard philosophical question with a testable one — is the pattern of the whole field. It is also the source of endless argument, because a machine can pass the test by being good at conversation without understanding anything, which is roughly what happened seventy years later.

In 1956 the Dartmouth workshop gave the field its name: artificial intelligence. The proposal was confident, the results were thin, and the field was born anyway.

### Step 2 - The rule years, and the first winter (1956-1993)

The first generation believed that intelligence was manipulation of symbols. If you can write down what a doctor knows, you can build a program that diagnoses. This produced real, useful systems: MYCIN advised on bacterial infections in the 1970s and sometimes matched human specialists. Companies built **expert systems** for insurance, mining and factory planning, and for a while the market was enormous.

There were two problems. First, the rules were expensive. A single expert system needed hundreds of rules, each one argued over by specialists, and the rules interacted in ways nobody predicted. Second, the systems had no common sense. A medical system could reason about infections but not notice that a patient was pregnant unless someone had written a rule for it.

The technical blow came earlier. In 1969, Marvin Minsky and Seymour Papert published *Perceptrons*, a careful analysis showing that a simple single-layer network could not compute even the logical function "exclusive or" — a case where the answer is yes if either input is yes, but not both. The result was read, unfairly but widely, as proof that the connectionist approach was dead. Funding for neural networks collapsed; rule-based work continued.

The commercial collapse came in the late 1980s. Expert systems ran on expensive special computers, and when ordinary desktop machines caught up, the economics vanished overnight. Around 1987 the market for those machines crashed. This period is now called the first **AI winter**.

The lesson people took away was "AI overpromises". The lesson the field actually learned was subtler: a method can be correct and still be too expensive to scale.

### Step 3 - The learning years and the deep years (1986-today)

While the rule-based wave was freezing, a different idea was warming up. In 1986, a group of researchers popularised a practical method for training multi-layer neural networks called **backpropagation**. You will meet it properly in Course 11. Its importance here is historical: it removed the objection of 1969. Networks could now learn things a single layer could not represent.

The 1990s shifted attention from hand-written rules to statistics. Instead of asking an expert what the rules are, collect data and estimate the probabilities. This was less glamorous and far more reliable, and it worked in speech, in handwriting, and in credit scoring. In 1997, Deep Blue beat Garry Kasparov at chess using fast search and hand-tuned evaluation, not learning — a triumph of the rules-and-search tradition at the very moment the statistical tradition was taking over.

Then came **scale**. In 2009 researchers released ImageNet, a dataset of over a million labelled photographs. In 2012, a deep network called AlexNet won the ImageNet competition by a large margin, using graphics processors built for video games to train a network with millions of parameters. The pattern was set: bigger networks, more data, more computing power. In 2016, AlphaGo beat a top human player at Go, a game everyone had said was years away. In 2017, a paper called *Attention Is All You Need* introduced the **transformer**, an architecture that handles sequences in parallel. In 2022, chat models built on transformers reached the public and made the argument about AI a household topic.

Notice what did not happen: the old ideas did not die. Chess engines still search. Rule systems still run factories and aircraft. Learning sits on top of both. The history is not a series of replacements. It is a series of additions.

| Period | Dominant idea | Typical success | Typical failure |
|---|---|---|---|
| 1956-1975 | Symbols and search | Puzzles, games, simple proofs | Real-world messiness |
| 1975-1987 | Expert rules | Medicine, configuration, planning | Cost, brittleness, common sense |
| 1987-2012 | Statistical learning | Speech, handwriting, recommendation | Needs labelled data |
| 2012-today | Deep learning at scale | Vision, language, games | Data hunger, opacity, cost |

## Where It Goes Wrong

**Mistake 1 - "AI is brand new".** The ideas are old. *Fix:* date the idea, not the product. A chat model is a 2017 architecture trained on decades-old learning theory.

**Mistake 2 - Reading a winter as a death.** Winters were funding winters, not idea winters. *Fix:* ask what survived each winter. Backpropagation survived the 1970s and won in the 2010s.

**Mistake 3 - Treating a benchmark win as a capability.** Winning a game is not general skill. *Fix:* ask what the benchmark leaves out. A Go program does not know that stones are physical objects.

**Mistake 4 - Believing the current wave cannot fail.** Every wave looked permanent from inside. *Fix:* name the wall. For deep learning, the walls are data, energy, reliability and trust.

**Mistake 5 - Repeating the promise cycle in your own project.** "We will have a general robot in six months" is the Dartmouth proposal again. *Fix:* promise a task, a measure and a date. Then test the measure.

## Case Note

MYCIN was a rule-based system built at Stanford in the 1970s to advise doctors on bacterial infections of the blood. It asked questions, weighed evidence, and recommended an antibiotic. In blind evaluations it performed about as well as human specialists, and better than some junior doctors. It had roughly 600 rules, each argued over by clinicians, and it could explain its reasoning by listing the rules it had used.

It was never used routinely in hospitals.

The reasons were not about accuracy. Doctors did not want to type answers to long lists of questions while a patient waited. The system ran on specialised hardware that most hospitals did not own. Nobody was sure who would be legally responsible if its advice caused harm. And the knowledge base would have needed constant maintenance by experts who had other jobs.

Every one of those obstacles is still with us, in a new form. Today's systems are faster and easier to talk to, but integration, liability, maintenance and trust decide adoption exactly as they did in 1976. This is why Course 1 keeps insisting that a model is not a system, and why Chapter 9 spends its whole length on the chain around the model.

The historical lesson is worth stating plainly: the field has repeatedly produced technology that worked in the laboratory and failed in the world. The failures were rarely mathematical. They were about the human and organisational ground the system had to stand on.

## Mini-Lab

**You need:** paper, a pen, and a ruler.

**Do this:**
1. Draw a horizontal line and mark the years 1940, 1960, 1980, 2000, 2020.
2. Place these on the line: Turing's paper (1950), Dartmouth (1956), the perceptron book (1969), MYCIN (1970s), the expert-system crash (1987), backpropagation (1986), Deep Blue (1997), ImageNet (2009), AlexNet (2012), AlphaGo (2016), transformers (2017), public chat models (2022).
3. Above the line, write the dominant idea at each point: rules, learning, or scale.
4. Below the line, write one wall that the dominant idea hit.

**What you should see:** the walls come roughly every fifteen to twenty years, and each new wave starts by fixing the wall of the last one.

**Why it matters:** you can now predict the shape of the next argument. When someone says a new method will solve everything, ask which wall it removes, and which wall it creates.

## Recap and Questions

**Three things to remember**

1. The field moves in a loop: promise, narrow success, wall, pivot.
2. Rules, learning and scale are additions, not replacements. Modern systems stack all three.
3. Winters were about funding and cost, not about ideas being wrong.

**Check yourself**

1. Why did the 1969 result on perceptrons damage neural network research so much, given that it was a narrow mathematical point?
2. What did the expert-system crash of 1987 teach the field about hardware?
3. Name one thing today's large models cannot do that a rule-based expert system could do in 1980.

**One thing to try next**

Find a news article about AI from five years ago and one from this month. Compare the promises. Write one sentence describing the wall that the older article did not see coming.


---

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


---

# Searching for Solutions

> Course 1: Introduction to Artificial Intelligence - Chapter 4 of 10

## Opening

By the end of this chapter you can turn a problem into states and moves, solve it with breadth-first and depth-first search, and explain why a good guess makes search dramatically faster.

In 1997, the chess program Deep Blue looked at roughly two hundred million positions per second, and still could not look far enough ahead to be sure of winning. It won because it searched cleverly, not because it searched everything. This is the oldest trick in artificial intelligence: do not try every possibility, try the possibilities that look promising. Before you can do the clever version, you need to see the plain version, because every planner in this book — including the ones inside a robot arm — is built on the same four moving parts.

## Big Picture

A search problem is a map of situations and moves. A **state** is a snapshot of the situation. An **action** moves you from one state to another, at some cost. A **goal test** says whether a state is the one you want. Solving the problem means finding a path of actions from the start to a goal.

Search algorithms differ in the order they explore. Breadth-first search explores in rings, nearest first, which finds the shortest path but needs a lot of memory. Depth-first search dives down one branch until it is stuck, which needs little memory but may take a terrible route. Adding a **heuristic** — an estimate of the distance remaining — lets the search ignore most of the map and still find the best path, provided the estimate never lies by more than the truth. That last condition is the whole theory of A*, and you can check it on paper.

## Key Words

- **State** - a complete snapshot of the situation at one moment.
- **Initial state** - where the search begins.
- **Goal test** - a check that says whether a state is a goal.
- **Action** - a move from one state to another, with a cost.
- **Path cost** - the total cost of the actions taken to reach a state.
- **Frontier** - the set of states discovered but not yet explored.
- **Heuristic** - an estimate of the cost still to go, usually written h(n).

## The Explanation

### Step 1 - Describe the problem in five lines

Every search problem is written the same way. Once you have the five lines, most of the work is done.

1. **States.** What is a snapshot? For a warehouse robot: its grid cell, for example (row, column).
2. **Initial state.** Where it starts: (0, 0).
3. **Actions.** What it can do: up, down, left, right.
4. **Goal test.** Is this the delivery bay? Is the cell (7, 5)?
5. **Path cost.** What each move costs: 1 per cell, or 2 for a cell with a ramp.

Take a small warehouse, eight columns wide and six rows tall, with a shelf block in the middle. The robot starts at (0, 0) and must reach (7, 5). If the shelf block occupies columns 3 to 4 and rows 1 to 4, the straight line is blocked, and the shortest route is 12 moves.

This description is a **graph**. States are nodes, actions are edges, costs are edge weights. Every search algorithm in this chapter is a way of walking a graph. That is why Course 7 (Data Structures and Algorithms) and this chapter share so much machinery.

### Step 2 - Two ways to walk: rings or dives

**Breadth-first search (BFS)** keeps a queue of states: first in, first out. It explores all states at distance 1, then all at distance 2, and so on. Because it finishes each ring before starting the next, the first time it reaches the goal it has found the path with the fewest moves.

**Depth-first search (DFS)** keeps a stack: last in, first out. It follows one branch to the end, then backs up. It uses far less memory and may find *a* path quickly, but the path may be long and ugly.

The difference is dramatic once the map grows. Suppose each state has 10 possible actions (a **branching factor** of 10) and the solution is 6 moves deep.

- BFS may need to hold about 10⁶ = 1,000,000 states in memory at the deepest ring. At 100 bytes per state, that is 100 MB.
- DFS needs about 6 × 10 = 60 states, a few kilobytes.

So DFS wins on memory by a factor of sixteen thousand, and BFS wins on quality. This trade-off — memory against optimality — appears again and again in robotics, where a planner has milliseconds and a few megabytes.

A cheap improvement is **iterative deepening**: run DFS with a depth limit of 1, then 2, then 3, until the goal is found. It uses DFS memory but finds the shortest path like BFS. It repeats work, but the repeated work is small compared with the last ring, so the total cost is only slightly worse than BFS.

### Step 3 - Add a guess and watch the map shrink

Now give the search a **heuristic**: a guess at the remaining distance. For a grid with no obstacles, the straight-line distance in cells is a good guess. For the cell (0, 0) heading to (7, 5), the guess is the number of steps if nothing were in the way: 7 + 5 = 12 moves.

**A\*** keeps the frontier ordered by f(n) = g(n) + h(n), where g is the cost already paid and h is the estimate still to pay. It always expands the state with the smallest estimated total.

On a grid with the shelf block, A* typically expands a narrow band of cells between start and goal instead of the whole rings. In this small warehouse, BFS may expand 40 or more states; A* often expands about 15. On a realistic 200 × 200 map the difference is not a factor of three, it is a factor of thousands, and it is the difference between a robot that plans in 5 ms and one that stalls for 2 s.

The condition that makes A* trustworthy is **admissibility**: h must never overestimate the true remaining cost. Straight-line distance never overestimates, because you cannot travel less than the straight line. If h overestimates on some cells, A* may return a path that is not the shortest, and it will do so silently — the worst kind of failure, because the output looks fine.

A simple check you can do by hand: on a small map, run A*, then run BFS, and compare the path costs. If A* is worse, your heuristic is lying somewhere.

| Algorithm | Memory | Shortest path? | Needs heuristic? | Typical use |
|---|---|---|---|---|
| Breadth-first | High | Yes | No | Small maps, few moves |
| Depth-first | Low | No | No | Existence checks, mazes |
| Iterative deepening | Low | Yes | No | Games with time limits |
| A* | Medium | Yes, if h is admissible | Yes | Route planning, robot motion |

## Where It Goes Wrong

**Mistake 1 - Forgetting the visited set.** Without a record of visited states, the search can loop forever between two states. *Fix:* keep a set of visited states and skip duplicates.

**Mistake 2 - Confusing depth with cost.** In a grid where some cells cost 2, the path with the fewest moves may not be the cheapest. BFS counts moves; Dijkstra and A* count cost. *Fix:* decide which one the problem actually asks for.

**Mistake 3 - A heuristic that overestimates.** Multiplying the straight-line distance by 1.2 to "encourage" the search makes it faster and wrong. *Fix:* test the heuristic on a small map against BFS.

**Mistake 4 - Searching a space that is too big.** A robot arm with six joints at 0.1° resolution has more states than there are atoms in a room. *Fix:* reduce the resolution, or use sampling-based planning (Course 35).

**Mistake 5 - Ignoring the time budget.** A perfect plan that arrives 3 seconds late is useless for a robot avoiding a person. *Fix:* always measure planning time, not just path length.

## Case Note

Deep Blue beat Garry Kasparov in a six-game match in 1997, winning 3.5 to 2.5. Its strength came from two things working together: special-purpose hardware that could examine about 200 million chess positions per second, and an evaluation function that scored a position by counting material, king safety, pawn structure and dozens of other features. The evaluation was tuned with the help of strong human players.

The search was fast but not deep by human standards. In the middle game it looked ahead roughly six to eight moves, sometimes more with extensions. Kasparov could look further in the lines that mattered to him, because he could tell which lines mattered. The machine could not tell; it compensated by looking at everything.

That is the honest picture of search in AI. Machinery buys breadth. Heuristics buy direction. When you have neither, you have nothing. When you have both, you can beat a world champion in a narrow world with exact rules.

The same pattern repeats in every planner in this book. A robot arm planning a motion does not consider every possible trajectory; it uses a heuristic, usually distance in joint space, to throw most of them away. A warehouse robot uses a distance estimate to avoid exploring the whole map. The algorithm is almost never the clever part. The estimate is.

It is also worth noting what Deep Blue could not do. It could not recognise a chess board in a photograph, could not explain its moves in words a beginner would understand, and could not play any other game. Narrow, in the precise sense of Chapter 1.

## Mini-Lab

**You need:** paper, a pen, and a 6 × 6 grid you draw yourself.

**Do this:**
1. Draw a 6 × 6 grid. Mark the start at bottom-left and the goal at top-right. Blacken five cells as walls, leaving a route through.
2. Run BFS by hand. Number each cell with the number of moves from the start, ring by ring.
3. On a fresh copy, run DFS by hand, always trying up, then right, then down, then left. Count how many cells you visit before reaching the goal.
4. On a third copy, run A* using the Manhattan distance as h, and count the cells you expand.
5. Compare the three counts.

**What you should see:** BFS numbers form neat rings; DFS wanders into a dead end and back; A* expands a small number of cells near the straight line. All three find a path; only two find the shortest.

**Why it matters:** you have now seen with your own hand why heuristics matter, and why the choice of search order is an engineering decision, not a detail.

## Recap and Questions

**Three things to remember**

1. A search problem is five lines: states, start, actions, goal test, path cost.
2. BFS finds the shortest path and needs memory; DFS needs little memory and may return a poor path.
3. A* is only as good as its heuristic, and the heuristic must never overestimate.

**Check yourself**

1. In a grid where all moves cost 1, is A* with h = 0 the same as any other algorithm you met? Which one?
2. Why does iterative deepening use less memory than BFS but still find the shortest path?
3. A warehouse planner returns a path of cost 14 when the true shortest is 12. What is the most likely cause?

**One thing to try next**

Write the five-line description for a problem you solved today without thinking — finding a seat in a crowded room, or packing a bag. Then decide whether a person solving it uses breadth-first or A*.


---

# Knowledge, Rules and Reasoning

> Course 1: Introduction to Artificial Intelligence - Chapter 5 of 10

## Opening

By the end of this chapter you can write facts and rules in a form a computer can use, trace a chain of reasoning forwards and backwards, and say where rule-based systems break.

A hospital receptionist follows a short list of rules. If a patient has chest pain, call the emergency team immediately. If a patient has a fever and a cough, send them to the respiratory clinic. If neither applies, book a normal appointment. Nobody calls that list "artificial intelligence", yet it is exactly the kind of knowledge that powered the first great commercial wave of AI. Expert systems in the 1980s held thousands of such rules and gave advice on infections, insurance and factory faults. Learning why they worked, and why they stopped, is the fastest way to understand what knowledge actually is.

## Big Picture

A rule-based system has two parts. The **knowledge base** holds facts and rules, written in a form the machine can read. The **inference engine** applies the rules to the facts and produces new facts, over and over, until it reaches a conclusion or runs out of things to do.

The appeal is honesty. Every conclusion can be traced back to the exact rules that produced it, which is why expert systems were trusted in medicine and banking. The weakness is equally clear: the system knows only what someone wrote down. It has no common sense, no ability to notice that a rule does not apply today, and no way to say "I am not sure". Rule-based reasoning gives certainty, and certainty is exactly what the messy real world rarely offers.

## Key Words

- **Knowledge base** - the store of facts and rules.
- **Fact** - a statement known to be true, such as "patient 12 has a fever".
- **Rule** - an if-then statement linking conditions to conclusions.
- **Inference** - the process of deriving new facts from old ones.
- **Forward chaining** - start from the facts and apply rules until nothing new appears.
- **Backward chaining** - start from the question and work back to the facts that would prove it.
- **Conflict resolution** - the rule for deciding which of several applicable rules fires first.

## The Explanation

### Step 1 - Write facts and rules so a machine can check them

A fact is a short statement with a name and arguments:

```
fever(patient12).
cough(patient12).
age(patient12, 34).
```

A rule has a head (the conclusion) and a body (the conditions):

```
urgent(X) :- fever(X), cough(X), age(X, A), A > 60.
```

Read the arrow as "if". If X has a fever, and X has a cough, and X is older than 60, then X is urgent. The variable X stands for any patient. This notation is called a **logic program**, and it is old, small and still useful.

Now add a second rule:

```
respiratory(X) :- fever(X), cough(X).
```

Notice the overlap: every patient who matches the urgent rule also matches the respiratory rule. That is not a bug. It is the normal state of a knowledge base, and it is why you need a policy for conflicts.

The third piece is the **conflict resolution** rule. A simple and defensible policy: specific rules beat general rules, so a patient who matches the urgent rule is sent to emergency even though they also match the respiratory rule. Write that policy down, because a system whose behaviour depends on the order in which rules happen to be stored is a system nobody can explain.

### Step 2 - Reason forwards or backwards

**Forward chaining** starts with what you know and pushes until nothing new can be derived. It is **data-driven**: new information arrives, and you ask what follows.

Take a patient with fever, cough and age 34. Apply the respiratory rule: respiratory(patient12) is now true. Apply the urgent rule: the age condition fails, so nothing. Conclusion: respiratory clinic, not emergency. Two rules checked, one fact added, done.

**Backward chaining** starts with a question and works back. The question is "is patient 12 urgent?" The engine looks for a rule whose head is `urgent(X)`. It finds the one above and sets three sub-goals: fever, cough, age over 60. Fever: true. Cough: true. Age over 60: false because the patient is 34. The answer is no, and the engine can show the exact path that produced it.

Backward chaining is efficient when there are many rules and few questions, because it ignores everything unrelated to the question. Forward chaining is efficient when facts keep arriving and you want to keep conclusions up to date, which is the normal situation in monitoring.

| | Forward chaining | Backward chaining |
|---|---|---|
| Starts from | Known facts | The question |
| Style | Data-driven | Goal-driven |
| Good when | Facts arrive continuously | Few questions, many rules |
| Typical use | Monitoring an alarm system | Diagnosis, configuration |

### Step 3 - Accept the wall: certainty is not enough

The rule above says a 61-year-old with fever and cough is urgent. Fine. Now change one word: what if the patient is 60 years and 11 months? The rule is silent. What if the fever is 37.9 °C and the rule says 38.0? Silent again. Real knowledge does not have sharp edges, and rules do.

Three walls stop rule-based systems:

1. **The knowledge acquisition wall.** Each rule needs an expert to state it, argue for it, and test it. A system with 4,000 rules has millions of possible interactions, and nobody can read them all.
2. **The common-sense wall.** The system does not know that a person cannot be in two places, that water is wet, or that a patient who is asleep cannot answer questions. Everything must be written down.
3. **The uncertainty wall.** Rules are true or false. The world is usually "probably". Pushing probability through rules is possible, but it quickly becomes heavy — which is why Chapter 7 and Course 21 exist.

Modern systems answer these walls with combinations. A rule layer handles the parts that must be auditable, such as "never open the door while the robot is moving". A learned model handles the parts that are fuzzy, such as "is that a person or a coat stand". The engineer's job is to decide which part of the problem belongs to which layer.

## Where It Goes Wrong

**Mistake 1 - Rules that overlap with no priority.** Two rules both apply and the system behaves differently on different runs. *Fix:* write an explicit conflict-resolution policy and test it with overlapping cases.

**Mistake 2 - No defaults.** The system has nothing to say when a value is missing, so it silently treats "unknown" as "false". *Fix:* model unknown as its own state and decide what the system should do.

**Mistake 3 - Sharp thresholds on smooth quantities.** A temperature rule that triggers at exactly 38.000 °C produces a cliff in behaviour. *Fix:* use hysteresis or fuzzy rules (Course 21).

**Mistake 4 - A knowledge base that nobody maintains.** Rules written in 1995 describe a hospital in 1995. *Fix:* give the knowledge base an owner, a review date and a test set of cases that must still pass.

**Mistake 5 - Explaining the trace instead of the reason.** A system that prints forty rule firings has not explained itself. *Fix:* store a natural-language reason with each rule and show the three or four that mattered.

## Case Note

In the 1980s, the computer company Digital Equipment Corporation used an expert system called XCON to configure its VAX computers. A customer order might specify dozens of components, and the components had to fit together physically, electrically and in software. Human specialists took hours and sometimes made expensive mistakes. XCON took minutes and, by the company's own estimate, saved tens of millions of dollars a year.

For a while, XCON was the flagship of a whole industry. Then the trouble started. Each new product line needed new rules. Each rule interacted with rules written years earlier by people who had left. The knowledge base grew into the thousands of rules, and every change risked breaking a configuration nobody had tested. Maintaining it became a specialist job in itself, and the system slowly became a liability rather than an asset.

The system never became wrong. It became expensive to keep right, which in business is the same thing.

There are three lessons here, and they are the reason this chapter treats maintenance as a first-class problem. First, knowledge has a shelf life; products change and rules rot. Second, the interactions between rules grow much faster than the number of rules, so a large knowledge base is a large testing problem. Third, the people who understand the rules must stay involved, because a knowledge base with no owner is a rumour with a database.

Modern systems have the same shape, whether the knowledge is in rules or in weights. Someone must own it, test it, and retire it. Ask any vendor of an "AI solution" who that person will be in your organisation. If the answer is vague, you have found the real cost.

## Mini-Lab

**You need:** paper and a pen, or any text editor.

**Do this:**
1. Write six facts about a broken laptop: it does not turn on, the charger is plugged in, the charger light is off, the battery was flat yesterday, the socket works, the cable is new.
2. Write five rules that could lead to a diagnosis, using the if-then form.
3. Run forward chaining by hand. Number each fact as it is derived.
4. Now ask "is the charger faulty?" and run backward chaining. Count how many facts you had to touch.
5. Deliberately add a rule that contradicts another. Decide which should win, and write down why.

**What you should see:** backward chaining touches fewer facts, forward chaining produces a fuller picture, and the contradiction forces you to make a policy decision that no amount of code can make for you.

**Why it matters:** this is the exact structure of every safety rule in robotics. "If a person is within 0.5 m, stop." You have now built and traced one.

## Recap and Questions

**Three things to remember**

1. A knowledge base is facts plus rules; inference is what turns one into the other.
2. Forward chaining is data-driven, backward chaining is goal-driven, and the choice depends on how the question arrives.
3. Rules give certainty and traceability, and they break on common sense, maintenance and uncertainty.

**Check yourself**

1. A rule says "if battery below 10%, return to dock". The battery sensor fails and reports nothing. What does a naive system do, and what should it do?
2. Give one task in a hospital where a rule is the right tool and one where it is the wrong tool.
3. Why does a 4,000-rule system become hard to test even if every rule is individually correct?

**One thing to try next**

Write the three rules you would put in a robot that shares a corridor with people, choosing only rules whose violation would be unacceptable. Then notice how much of the rest of the behaviour those rules do not cover.


---

# Learning from Data: A First Look

> Course 1: Introduction to Artificial Intelligence - Chapter 6 of 10

## Opening

By the end of this chapter you can train a simple classifier on a small table of examples, test it honestly, and explain why a model that scores perfectly may still be useless.

Imagine a maintenance team with a year of records: for each week, the vibration of a pump motor, its temperature, and whether the pump failed in the following month. Nobody wrote a rule for predicting failure. The data itself contains the pattern, if there is one. This is the shift that changed AI after the 1990s: instead of asking an expert to state the rules, we show the machine hundreds of examples and let it find them. You can do the same thing by hand, with twelve rows and a pencil, and understand it better than most people who call a library and hope.

## Big Picture

**Machine learning** fits a rule from examples rather than from instructions. Each example has **features** — the numbers you measure — and a **label** — the answer you want to predict. The learner produces a **model**: a compact rule that maps features to labels.

The only thing that matters is whether the model works on examples it has never seen. That is called **generalisation**, and it is the whole game. A model can score 100% on the data it learned from and fail completely on new data, because it memorised the examples instead of the pattern. This is **overfitting**, and it is the most common failure in applied machine learning. The cure is simple and non-negotiable: hide some data before you start, train on the rest, and only ever judge the model on the hidden part.

## Key Words

- **Feature** - a measurable input, such as vibration in mm/s.
- **Label** - the answer you want to predict, such as "failed" or "did not fail".
- **Training set** - the examples the model learns from.
- **Test set** - examples held back and used only for judging.
- **Model** - the rule the learner produces.
- **Generalisation** - doing well on examples the model has never seen.
- **Overfitting** - fitting the training examples so closely that new examples fail.

## The Explanation

### Step 1 - Build a table of examples

Learning starts with a table. Rows are examples, columns are features, and the last column is the label.

| Pump | Vibration (mm/s) | Temperature (°C) | Failed within a month? |
|---|---|---|---|
| 1 | 1.2 | 41 | No |
| 2 | 1.8 | 43 | No |
| 3 | 2.1 | 45 | No |
| 4 | 2.6 | 47 | No |
| 5 | 3.1 | 49 | No |
| 6 | 3.4 | 52 | Yes |
| 7 | 3.6 | 51 | Yes |
| 8 | 4.0 | 55 | Yes |
| 9 | 4.4 | 58 | Yes |
| 10 | 4.8 | 60 | Yes |

Ten rows is tiny, but it is enough to see the method. Look at the vibration column: below about 3.4 mm/s, every pump survived. Above 3.4, every pump failed. There is a clean gap between 3.1 and 3.4.

The first model you should always try is the simplest possible one:

```
if vibration > 3.25 mm/s then "will fail" else "will not fail"
```

That is a **threshold model** with one parameter, 3.25, chosen as the midpoint of the gap. It has two numbers' worth of complexity and it may be right. Before reaching for anything fancier, check whether a straight line already solves the problem. In real industry, a surprising share of useful predictive maintenance is a threshold on one sensor.

### Step 2 - Try a second method and compare

A second simple method is **nearest neighbour**: to predict a new pump, find the most similar row in the training table and copy its label. If a new pump has vibration 3.5 mm/s and temperature 50 °C, the nearest row is pump 6 (3.4, 52, Yes), so predict "Yes".

Nearest neighbour has an attractive property: it needs no training at all, it just stores the data. It has two weaknesses. It stores everything, so memory grows with the dataset. And it is easily fooled by a feature that is measured on a large scale. If temperature were given in hundredths of a degree and vibration in whole mm/s, "nearest" would be decided almost entirely by temperature. This is why features are almost always scaled before comparison, a habit you will meet again in Course 3.

Now compare both methods on the same test. Hold back pumps 3, 5, 8 and 9. Train on the other six, then predict the four:

| Held-back pump | True label | Threshold prediction | Nearest neighbour prediction |
|---|---|---|---|
| 3 (2.1, 45) | No | No | No |
| 5 (3.1, 49) | No | No | No |
| 8 (4.0, 55) | Yes | Yes | Yes |
| 9 (4.4, 58) | Yes | Yes | Yes |

Both methods get 4 out of 4. So which is better? With four test cases, neither result means much — the difference between 4/4 and 3/4 is one example, well within luck. This is the honest conclusion, and writing it down is part of the skill. Small tests produce large uncertainties, and you must say so.

### Step 3 - Judge with a confusion matrix, not one number

A single accuracy number hides the kind of mistake. A **confusion matrix** shows both.

For a failure-prediction model there are two mistakes, and they are not equal. A **false alarm** means you service a healthy pump: it costs money and time. A **missed failure** means a pump dies in service: it costs production, and possibly safety. You must decide the trade-off before you tune the model.

Take a larger test of 100 pumps, 10 of which really fail. The model predicts 14 failures. Of those, 8 are real and 6 are false alarms. It misses 2 real failures.

| | Model says fail | Model says fine |
|---|---|---|
| Actually failed (10) | 8 | 2 |
| Actually fine (90) | 6 | 84 |

Accuracy is (8 + 84) / 100 = 92%. Precision — of the ones we flagged, how many were real — is 8 / 14 = 57%. Recall — of the real failures, how many did we catch — is 8 / 10 = 80%.

A system with 57% precision sends six healthy pumps to the workshop for every eight real problems. A maintenance manager will stop using it within a month, no matter what the accuracy says. Lowering the threshold to catch all ten failures would raise recall to 100% and probably drop precision further, flooding the team with false alarms.

There is no free choice here. There is only a decision about which mistake you can live with, made with the people who own the consequences. That decision is engineering, and it is yours to force into the open.

## Where It Goes Wrong

**Mistake 1 - Testing on the training data.** The model scores 100% and everyone is happy until it meets a new pump. *Fix:* split the data before you look at it, and never touch the test set during development.

**Mistake 2 - Leakage.** A feature secretly contains the answer, such as a "repair date" column that is only filled after a failure. *Fix:* ask of every column, "would I know this at prediction time?"

**Mistake 3 - Ten rows and a big claim.** A model trained on ten examples is a hypothesis, not a result. *Fix:* report the number of examples beside every score.

**Mistake 4 - Ignoring class imbalance.** When 95% of cases are "fine", a model that always says "fine" is 95% accurate and worthless. *Fix:* report precision and recall, and compare with the always-fine baseline.

**Mistake 5 - Tuning on the test set.** Trying twenty settings and keeping the best test score means the test set has become training data. *Fix:* keep a third set, the validation set, for tuning.

## Case Note

In 2008, Google launched Flu Trends, a service that estimated the level of influenza in a region from the volume of flu-related search queries. It was a genuine research success. In the United States, its estimates matched official surveillance data closely, and it reported them about two weeks earlier, because people search before they see a doctor.

Then it drifted. For several seasons, including the 2012–13 flu season, it substantially overestimated the number of cases. Some estimates suggested it was out by more than a factor of two. The reasons were ordinary: Google changed its search suggestions, people's search habits changed, media coverage changed what people typed. The model had been fitted to a world that no longer existed.

The most instructive part is the method. The model's search terms had been selected by checking how well they fitted past flu data. That is a mild form of using the test data for training: the terms were chosen partly because they matched the very seasons used to judge them. When new seasons arrived, the apparent success did not continue. The service was discontinued in 2015.

This is why the pump example in this chapter hides four rows before you choose a threshold. It is why the book insists on a test set that you do not touch, and on monitoring after launch. The pattern you find in data is the pattern of that data, and the world moves. A model is a hypothesis about the future that must be checked against the future.

## Mini-Lab

**You need:** paper and a pen.

**Do this:**
1. Copy the ten-pump table, but hide the labels of pumps 2, 5, 7 and 10.
2. Choose a threshold using only the visible six rows. Write down how you chose it.
3. Predict the four hidden pumps. Then uncover the labels and score yourself.
4. Build the confusion matrix for those four predictions.
5. Repeat with a threshold 0.5 mm/s higher. Which pumps change? Which mistake got worse?

**What you should see:** moving the threshold trades one kind of mistake for the other. There is no setting that removes both, which is the lesson.

**Why it matters:** every medical test, fraud detector and safety alarm you will ever build has this same trade-off, and someone must own it.

## Recap and Questions

**Three things to remember**

1. Learning fits a rule from examples; the only score that matters is on data the model has never seen.
2. Always try the simplest model first — often a single threshold is enough.
3. Accuracy hides the kind of mistake. Report precision and recall, and name the mistake you can live with.

**Check yourself**

1. Why is a 100% training score a warning sign rather than good news?
2. In the pump example, which mistake is more expensive? Argue both sides in one sentence each.
3. Your model has 95% accuracy and 20% recall. What does that mean in plain words?

**One thing to try next**

Find a dataset you already own — a spreadsheet of expenses, a fitness app history — and predict one column from another using a threshold you choose by eye. Then check it on rows you hid first. The surprise is the lesson.


---

# Uncertainty and Probability

> Course 1: Introduction to Artificial Intelligence - Chapter 7 of 10

## Opening

By the end of this chapter you can reason with uncertain evidence, update a belief when new information arrives, and explain why a 99% accurate test can still be wrong most of the time it fires.

A robot in a warehouse is told there is a box ahead. Its distance sensor says 1.2 m. The sensor is good, but not perfect: sometimes it reads short when the floor is shiny. Does the robot stop? A rule cannot answer, because the sensor has not given a fact. It has given evidence. Almost everything a robot receives is evidence, not fact, and the mathematics for turning evidence into belief is probability. This chapter gives you the one formula you will use for the next forty courses.

## Big Picture

Probability is a way of writing down how strongly you believe something. Belief starts from what you already knew — the **prior** — and is updated by new evidence using **Bayes' rule**. The update is not a guess; it is arithmetic.

The key insight is that evidence is only meaningful compared with how often it happens by chance. A smoke alarm that goes off during cooking is not strong evidence of fire, because it goes off during cooking often. A smoke alarm that goes off at 3 a.m. in a hotel is strong evidence, because that is rare. Bayes' rule is simply the discipline of comparing those two rates. Once you have it, you will spot bad reasoning in newspapers, medical leaflets and AI marketing for the rest of your life.

## Key Words

- **Uncertainty** - the state of not knowing something for certain.
- **Probability** - a number from 0 to 1 saying how likely an event is; 0 is impossible, 1 is certain.
- **Prior** - the belief before seeing new evidence.
- **Likelihood** - how probable the evidence is if the hypothesis is true.
- **Posterior** - the updated belief after seeing evidence.
- **Base rate** - how common the condition is in the population.
- **Bayes' rule** - the formula for turning a prior and a likelihood into a posterior.

## The Explanation

### Step 1 - Treat sensor readings as evidence

Start with the simplest possible statement: the sensor is right 90% of the time. That gives two numbers that engineers call the **sensitivity** and the **false positive rate**, and they are not the same thing.

- If a box is there, the sensor says "box" 90% of the time. (Sensitivity 0.9)
- If no box is there, the sensor says "box" anyway 10% of the time. (False positive rate 0.1)

Now the critical question that everyone forgets: how often is there actually a box? In a busy aisle, maybe 1 in 10 readings has a real box. This is the **base rate**, and without it the other two numbers mean nothing.

Suppose 1,000 readings: 100 real boxes, 900 empty stretches. The sensor catches 90 of the boxes. It also raises 10% × 900 = 90 false alarms. So when the sensor says "box", there are 90 true and 90 false — a 50% chance. A "90% accurate sensor" has produced a reading that is right half the time.

That is not a paradox. It is arithmetic, and it is why robots use several sensors instead of trusting one.

### Step 2 - Update belief with Bayes' rule

Bayes' rule in words: the belief after the evidence is proportional to the belief before it, multiplied by how well the evidence fits.

```
P(box | reading) = P(reading | box) × P(box) / P(reading)
```

Fill in the numbers above. P(reading | box) = 0.9. P(box) = 0.1. The total probability of a "box" reading is the true ones plus the false ones: 0.9 × 0.1 + 0.1 × 0.9 = 0.09 + 0.09 = 0.18.

So P(box | reading) = 0.09 / 0.18 = 0.5.

The belief went from 0.1 before the reading to 0.5 after it. That is a big jump, and it is still not enough to stop a forklift. This is exactly right: one sensor moved the belief, and did not settle the question.

Now add a second, independent sensor with the same rates. Run Bayes again with 0.5 as the new prior:

P(box | second reading) = (0.9 × 0.5) / (0.9 × 0.5 + 0.1 × 0.5) = 0.45 / 0.5 = 0.9.

Two readings, each 90% reliable on its own, produce a 90% belief. Three would take it above 97%. This is **sensor fusion**, and the arithmetic you just did by hand is the core of Course 14.

### Step 3 - Choose actions under uncertainty, not certainties

A robot never gets to act on perfect knowledge. It gets to act on a belief, and the right action depends on the cost of being wrong.

Suppose the robot can stop (cost: 2 seconds of delay) or continue (cost: a collision, which is unacceptable). With a 0.5 belief, continuing is reckless. With a 0.97 belief, stopping wastes time. Somewhere between, there is a threshold, and that threshold is set by the consequences, not by the probability alone.

You can compute a simple version. Let the delay cost be 2 units and a collision cost 1,000 units. Continuing has expected cost 1,000 × (1 − p). Stopping has expected cost 2. Continue only when 1,000 × (1 − p) < 2, that is, when p > 0.998. A 99.8% belief is needed before moving, which sounds extreme and is exactly why robots slow down near people rather than trusting a single reading.

This one calculation explains a design habit you will see everywhere in robotics: safety systems lower the robot's speed and increase its sensing when uncertainty rises. They do not argue with the probability. They change the physics.

## Where It Goes Wrong

**Mistake 1 - Ignoring the base rate.** "The test is 99% accurate" sounds decisive until you learn the condition affects 1 in 10,000 people. *Fix:* always ask how common the thing is before believing a positive result.

**Mistake 2 - Treating dependent evidence as independent.** Two cameras on the same bracket, both blinded by the same sun, are not two independent readings. *Fix:* ask what could fool both at once.

**Mistake 3 - Reporting a probability without a decision rule.** "There is a 30% chance of a person" is not an instruction. *Fix:* pair every probability with the action threshold it triggers.

**Mistake 4 - Confusing "probable" with "frequent".** A single event, such as this specific bridge failing, has no long-run frequency. Probability here is a degree of belief, and that is fine, as long as you say so.

**Mistake 5 - Overconfidence from a model.** A neural network that outputs 0.99 is not necessarily right 99 times in 100. *Fix:* measure calibration on held-out data before trusting a confidence number.

## Case Note

In the early hours of 29 March 2019, a Boeing 737 MAX crashed shortly after take-off, killing all 157 people on board. It was the second crash of the type in five months. Investigators found that a software system had been repeatedly pushing the aircraft's nose down, driven by a single angle-of-attack sensor feeding it incorrect data. The system had no independent cross-check of that sensor, and the pilots had not been told it existed.

The engineering lesson is not "software is dangerous". It is narrower and more useful: a decision built on one noisy measurement, with no second source and no way for a human to see the disagreement, will eventually act on a false reading. Bayes' rule tells you the fix in advance. Two independent readings take a 50% belief to 90%. A third takes it to 97%. The cost of the extra sensor is small next to the cost of a wrong decision.

Whenever you design a system that acts on evidence, ask three questions. How reliable is each source? Are the sources independent? Can a human see what the system believes and why? The first two are arithmetic. The third is design, and it is the one that saves lives.

## Mini-Lab

**You need:** paper, a pen, and a calculator.

**Do this:**
1. A factory alarm has sensitivity 0.95 and a false positive rate of 0.05. A fault occurs in 2% of production runs.
2. Imagine 10,000 runs. How many have a fault? How many true alarms? How many false alarms?
3. Compute P(fault | alarm) with Bayes' rule.
4. Now improve the sensor so the false positive rate drops to 0.01. Recompute.
5. Decide: above what belief would you stop the line, if stopping costs 1,000 units and a missed fault costs 50,000?

**What you should see:** the base rate matters as much as the sensor quality, and halving the false alarm rate changes the answer more than improving sensitivity would.

**Why it matters:** this is the arithmetic behind every alarm, every safety interlock and every "the AI is 99% confident" claim you will meet.

## Recap and Questions

**Three things to remember**

1. Sensors give evidence, not facts. Belief = prior updated by likelihood.
2. The base rate decides whether a positive result is impressive or ordinary.
3. Independent evidence multiplies belief; dependent evidence does not. Actions follow costs, not probabilities alone.

**Check yourself**

1. A test is 99% sensitive with a 1% false positive rate. One person in 1,000 has the condition. Roughly what is P(condition | positive)?
2. Why are two cameras on the same bracket weaker evidence than two cameras at opposite ends of the robot?
3. Your robot is 60% sure a doorway is clear. What else do you need before deciding to pass through it?

**One thing to try next**

Take any screening test you have read about — a medical test, a spam filter, a fraud check — and find its sensitivity, its false positive rate and the base rate. If any of the three is missing, you now know the claim cannot be judged.


---

# Language, Vision and Sound: A First Look

> Course 1: Introduction to Artificial Intelligence - Chapter 8 of 10

## Opening

By the end of this chapter you can explain in plain terms how machines handle pictures, speech and text, and why the same three ideas keep appearing in all three.

Show a photograph to a person and they see a kitchen: a kettle, a mug, a window, light from the left. A computer receives a grid of numbers, each number saying how bright one tiny square is. Nothing in those numbers says "kettle". Turning numbers into meaning is the task of vision. Speech is a wave that must become letters, and text is a sequence of symbols with grammar and ambiguity. Three different inputs, three different problems, and yet the same methods keep working. Seeing that pattern early will save you years.

## Big Picture

All three problems begin the same way: raw input becomes numbers, numbers become **features** — small, useful summaries such as edges, pitch patterns or word frequencies — and features become decisions. The older approach had engineers design the features by hand. The modern approach learns them from data, which is what deep learning does.

The second shared idea is **context**. A word means something different depending on its neighbours. A pixel means something different depending on the pixels around it. A sound means something different depending on the sounds before it. Every modern advance in vision, speech and language has come from handling context better. When you meet a new architecture in Course 22, ask what context it is capturing.

## Key Words

- **Pixel** - one tiny square of an image, holding brightness or colour.
- **Feature** - a small summary of the raw data that is useful for a decision.
- **Token** - a small unit of text, usually a word or part of a word.
- **Embedding** - a list of numbers that represents a word or token.
- **Waveform** - the shape of a sound signal over time.
- **Spectrogram** - a picture of sound showing which frequencies are present at each moment.
- **Context** - the surrounding data that changes the meaning of the current piece.

## The Explanation

### Step 1 - Vision: from brightness to meaning

An image is a grid of pixels. A small grey image might be 640 × 480 = 307,200 pixels. Each pixel holds a number from 0 to 255, where 0 is black and 255 is white. A colour image has three such grids, one each for red, green and blue.

The first useful feature is an **edge**: a place where brightness changes sharply. You can find edges with a simple operation that compares each pixel with its neighbours. Edge detection is old, reliable, and still the first step in industrial vision systems that measure a part to a hundredth of a millimetre.

The second step is to group edges into shapes, and the third is to name the shapes. Older systems did this with hand-written rules: if there are two vertical edges 0.2 m apart and a horizontal edge on top, call it a door. That works until the door is open, or the light changes, or the wall is the same colour as the door.

Modern systems learn the grouping. A **convolutional network** (Course 11) learns which combinations of edges matter, starting with edges, then corners and textures, then parts of objects, then whole objects. The remarkable thing is that nobody writes those stages down. They emerge from examples.

The numbers here matter. A 640 × 480 colour image holds about 921,600 numbers. A single decision — "is there a person here?" — must compress that into one number. That compression is why features exist, and why a badly chosen feature makes the problem impossible no matter how clever the classifier.

### Step 2 - Sound: from pressure to words

A microphone measures air pressure many thousands of times a second. At 16,000 samples per second, one second of speech is 16,000 numbers. That is not a useful starting point, because the same word said louder or slower produces completely different numbers.

The trick is to look at frequency. A **spectrogram** breaks the sound into short slices — say 25 ms each, with a 10 ms step — and records how much energy is present at each frequency in each slice. One second of speech becomes about 100 slices of, say, 128 frequency values: a 100 × 128 picture of the sound. Speech recognition then becomes image recognition, and the methods described above apply.

This is why speech systems improved so much when deep learning arrived. The problem was never really about sound; it was about recognising patterns in a picture of sound once you had made the picture.

The same numbers give you an intuition for cost. Processing audio at 16 kHz means 16,000 samples per second, times 2 bytes, times 3600 seconds: about 115 MB for one hour of raw audio. A spectrogram of the same hour is much smaller, which is one reason edge devices compute it first.

### Step 3 - Language: from tokens to meaning

Text is a sequence of characters, which become **tokens**. A token is often a word or part of a word: "robotics" might become "robot" + "ics". A typical English sentence of 20 words might become 25 tokens.

Each token is mapped to an **embedding**: a list of numbers, usually a few hundred long, chosen so that words used in similar ways end up close together. "Torque" and "force" end up nearer each other than "torque" and "banana". Nobody assigns these positions by hand; they are learned from enormous amounts of text.

Then comes context, and this is where language is hardest. Consider these three uses of one word:

- "The bank raised its interest rate."
- "We sat on the bank of the river."
- "Bank left at the next junction."

A system that gives each word one fixed meaning must fail on at least two of these. A system that reads the whole sentence can tell them apart. Modern language models do this by letting each token look at the other tokens around it and adjust its representation, a mechanism called **attention**. That single idea, published in 2017, is the basis of the systems people now call "AI".

## Where It Goes Wrong

**Mistake 1 - Forgetting how much data a pixel or a sample is.** Students underestimate storage and compute by orders of magnitude and then wonder why the robot's processor melts. *Fix:* compute the numbers before choosing hardware.

**Mistake 2 - Treating one modality as ground truth.** A language model can describe a scene it has never seen; a camera cannot read a label on a box behind a shelf. *Fix:* combine modalities, and say which one is authoritative for which claim.

**Mistake 3 - Confusing fluency with understanding.** A model that writes confident prose may still be wrong about the world. *Fix:* test on facts, not on style.

**Mistake 4 - Training on one accent, one lighting condition, one writing style.** Performance collapses on everyone else. *Fix:* collect data that looks like the real users, including the awkward cases.

**Mistake 5 - Ignoring latency.** A vision model that takes 500 ms per frame cannot control a robot arm moving at 1 m/s. *Fix:* measure the full pipeline, from sensor to decision.

## Case Note

In 2018, a team of researchers showed that small changes to a few pixels could make an image classifier give a completely wrong answer with high confidence. The changes were invisible to people: the picture still looked like a panda to you, while the network saw a gibberish pattern and said "gibbon" with 99% confidence.

The lesson is not that vision does not work. Vision works extremely well on the data it was trained on. The lesson is that a network's confidence is a number produced by arithmetic, not a report on reality. There is no guarantee that the features it learned are the features you had in mind.

This is why serious systems combine a learned model with a check that does not share its weaknesses: a second sensor, a rule that refuses impossible outputs, or a human in the loop for high-stakes decisions. When you build a vision or language system, write down what could fool it. Then design the check before the failure happens.

## Mini-Lab

**You need:** a phone with a camera, or any image editor, and paper.

**Do this:**
1. Take a photo of a simple object on a plain background. Open it in any editor and zoom until you can see individual pixels.
2. Find an edge. Write down the approximate brightness of the pixels on each side — for example, 60 on the left and 180 on the right.
3. Estimate the size of the image in pixels: width × height × 3 for colour. Write the total.
4. Now cover the object with a cloth and repeat. Ask: which features changed, and which stayed the same?
5. In one sentence each, write what a rule-based system and a learned system would each get right and wrong on this pair of images.

**What you should see:** the edge numbers differ by a large jump, which is why edges are easy to find. The cloth changes almost everything, which is why hand-written rules are brittle.

**Why it matters:** you have connected a photograph to the numbers a network actually sees, which is the first step towards building one.

## Recap and Questions

**Three things to remember**

1. Images, sound and text all become numbers, then features, then decisions.
2. Sound is turned into a picture (a spectrogram) so that audio tools and vision tools become the same tools.
3. Context is what separates meaning from symbols, and attention is how modern systems handle it.

**Check yourself**

1. Why is a spectrogram more useful than raw audio samples for recognising a word?
2. A 1920 × 1080 colour image has how many numbers? Why does that matter for a robot with 512 MB of memory?
3. Give one task where a camera is better evidence than text, and one where text is better.

**One thing to try next**

Record yourself saying the same sentence loudly and softly, then look at the waveform in any free audio editor. The shapes will be different in height and similar in pattern. That difference is exactly why systems work on frequency, not amplitude.


---

# AI Systems in the Real World

> Course 1: Introduction to Artificial Intelligence - Chapter 9 of 10

## Opening

By the end of this chapter you can describe the whole life of an AI system — from problem framing to retirement — and name the parts that fail after the model has been trained.

A team builds a defect detector for a factory. The model is excellent: it finds 97% of faulty parts in testing. Six months after launch, the line manager asks for it to be switched off. The camera housing had slowly filled with dust, the lighting was replaced with a different colour temperature, and the model was quietly flagging one part in five as defective, so operators were overriding it constantly, and eventually they stopped looking. The model was never the problem. Everything around the model was. Most AI projects that fail, fail here: not in the maths, but in the space between the maths and the world.

## Big Picture

A working AI system is a chain, and the model is one link. The chain runs: a real problem worth solving, data that represents the world the system will meet, a model trained and tested honestly, an integration that delivers decisions in time, monitoring that notices when the world drifts, and people who know when to override the machine.

Every link has a cost, a failure mode and an owner. The most common mistake in student projects, and in industry, is to spend 90% of the effort on the model and 10% on the chain. The ratio that works is closer to the reverse. This chapter gives you the vocabulary to plan the whole chain, so that your project does not become the defect detector that got switched off.

## Key Words

- **Problem framing** - turning a vague wish into a task with an input, an output and a measure.
- **Data drift** - the real-world data slowly changing away from the training data.
- **Latency** - the time from input to decision.
- **Error budget** - the mistakes a system is allowed to make, by type.
- **Integration** - connecting the model to sensors, actuators, software and people.
- **Monitoring** - watching a live system for drift, errors and silent failure.
- **Human in the loop** - a person who can review or override a decision.

## The Explanation

### Step 1 - Frame the problem before choosing the model

A wish is not a task. "Use AI to improve quality" cannot be built, tested or priced. A framed problem can:

> Detect scratches longer than 2 mm on the painted surface of part X, with a camera at the end of the paint line, and raise an alarm within 200 ms of the part passing the camera. Miss no scratch longer than 5 mm. Accept up to two false alarms per thousand parts.

Notice what the framing added: the object, the defect definition, the sensor, the time limit, the error budget and the acceptable false alarm rate. Every one of those is a decision that changes the design. Without them, you cannot tell success from failure.

Write the framing on one page, and get the person who owns the line to sign it. This single act prevents most later disputes. If a requirement cannot be measured, it is not a requirement, it is a hope.

### Step 2 - Build the chain, not just the model

The model is trained on labelled images. The chain around it has five more parts.

**Sensing.** Is the camera fixed, or does it vibrate? Is lighting controlled? A model trained under one lamp and deployed under another is a model trained on the wrong problem.

**Pre-processing.** Cropping, resizing, colour correction. Every one of these must be identical at training time and at run time. A mismatch here is one of the most common silent failures in deployed vision.

**Inference.** How long does one prediction take? If it is 300 ms and the requirement is 200 ms, the model is unusable no matter how accurate. Measure on the real hardware, not a laptop with a graphics card.

**Decision.** The model outputs a probability. Something must turn that into an action, using a threshold chosen from the error budget. A probability of 0.4 means nothing until someone decides what 0.4 triggers.

**Feedback.** How do operators report a mistake? That report is the only way the system improves, and the only way anyone learns that the world has changed.

| Link | Typical failure | Cheap check |
|---|---|---|
| Sensing | Lighting change, dust | Reference part photographed hourly |
| Pre-processing | Resize mismatch | Log the exact input tensor size |
| Inference | Too slow on real hardware | Time 1,000 predictions on the target |
| Decision | Threshold set for accuracy, not cost | Recompute with the real cost ratio |
| Feedback | No way to report a miss | One button, counted weekly |

### Step 3 - Plan for the day after launch

A model's accuracy is measured on data from the past. The future is different. Paint colours change, a new supplier sends parts with a different surface, the camera ages, the season changes the light through the window.

**Data drift** is the slow divergence of live data from training data. You cannot see it in the model, because the model will keep producing confident answers. You see it in the distribution of inputs, in the rate of alarms, and in operator complaints.

The practical defences are unglamorous:

- Log a sample of every input and every output. Without logs, there is nothing to investigate.
- Track the alarm rate weekly. A sudden doubling is a signal, even if accuracy has not been measured yet.
- Keep a small, freshly labelled set from each month, and score the model on it. This is the only honest measure of current performance.
- Set a review date and a retirement plan. Every model has a useful life, and pretending otherwise is how systems rot.

The factory detector had no logs, no weekly alarm-rate chart and no owner. Each of those would have caught the problem within a week.

## Where It Goes Wrong

**Mistake 1 - Optimising the model and ignoring the deadline.** A 99% accurate model that answers in 2 s is worse than a 94% model that answers in 20 ms when the line moves. *Fix:* put latency in the requirements, then measure it on target hardware.

**Mistake 2 - Training on clean data, deploying in a dirty world.** *Fix:* include the ugly cases in the training set — dust, glare, motion blur, partial occlusion.

**Mistake 3 - No baseline in production.** Nobody knows what the system replaced, so nobody can tell whether it helps. *Fix:* measure the old process for two weeks before switching.

**Mistake 4 - Automating a bad process.** A model that speeds up a broken workflow makes the breakage faster. *Fix:* fix the process first; automate second.

**Mistake 5 - No human override.** An operator who cannot correct the machine will eventually unplug it. *Fix:* design the override first, and count how often it is used.

## Case Note

Hospitals in several countries have deployed sepsis-alert systems that watch patient records and warn clinicians when a patient may be developing sepsis, a fast-moving and often fatal condition. Some of these systems reduced deaths; others were ignored and became background noise.

The difference was rarely the model. Where the alert arrived inside the workflow — on the screen the nurse was already looking at, with a suggested next step — it changed behaviour. Where it arrived as a separate dashboard, or fired so often that clinicians learned to dismiss it, it changed nothing.

The lesson generalises to every robot and every AI product. A prediction is not a decision, and a decision is not an action. Between the model and the outcome sit attention, trust, timing and workload. If you ignore those, you have built a very accurate system that nobody uses. Ask early: who receives this output, at what moment, and what will they do differently because of it?

## Mini-Lab

**You need:** paper and a pen, and one person to interview if possible.

**Do this:**
1. Pick a task in your school, home or workplace that someone does by hand and might be automated.
2. Write the one-page framing: input, output, measure, time limit, error budget, who signs off.
3. Draw the six links of the chain and write the biggest failure risk for each.
4. Estimate the latency allowed. Then think of three ways the world could drift away from your training data.
5. Ask one person who would use the system what they would do differently because of it. If they cannot answer, stop and reframe.

**What you should see:** the framing takes longer than expected, and the answers change the design. That is the point.

**Why it matters:** this is the difference between a coursework demo and a system that survives contact with reality.

## Recap and Questions

**Three things to remember**

1. A system is a chain: problem, data, model, integration, monitoring, people. The model is one link.
2. Frame the problem with a measure, a time limit and an error budget before choosing any method.
3. Drift is normal. Log, monitor and refresh, or the system will quietly fail.

**Check yourself**

1. Your detector finds 99% of defects in the lab and 80% on the line. Name three likely causes.
2. Why is an error budget more useful than a single accuracy target?
3. What would you log on day one, and why would you regret not logging it?

**One thing to try next**

Write the one-page framing for a robot you would like to build. Then show it to someone who is not an engineer. If they can tell you what the robot will and will not do, the framing is good enough to start.


---

# Limits, Risks and the Road Ahead

> Course 1: Introduction to Artificial Intelligence - Chapter 10 of 10

## Opening

By the end of this chapter you can name the real limits of today's AI, describe the risks that matter, and plan the next four years of your own study with a clear map.

In 2016, a self-driving car failed to see a white lorry crossing a brightly lit road, and the driver, who was not watching, was killed. The sensors worked. The software worked, in the sense that it ran without error. The system had never been shown that combination of a white object against a bright sky at that angle, and it had no fallback for not knowing. That gap — between a system that performs well on average and a system that is trustworthy at the edge — is where the whole field now lives. This chapter is about that gap, and about how the next 47 courses close it.

## Big Picture

Today's AI is powerful, narrow and fragile in specific, predictable ways. It is powerful because scale plus learning works: given enough examples, machines find patterns people cannot write down. It is narrow because those patterns do not transfer outside the data. It is fragile because it fails on inputs unlike anything it has seen, and it fails confidently.

The risks follow directly. A system that fails confidently is dangerous where failure is expensive: medicine, driving, weapons, hiring, policing. A system trained on the past carries the past's biases. A system that optimises a measure will find the cheapest way to satisfy the measure, including ways nobody intended.

None of this is a reason to stop. It is a reason to build with three habits: know the limits, measure at the edges, and keep a human able to see and stop what is happening.

## Key Words

- **Brittleness** - failing badly on inputs slightly different from training data.
- **Distribution shift** - the live world drifting away from the training data.
- **Bias** - a systematic error that disadvantages a group or a situation.
- **Causality** - knowing that one thing makes another happen, not just that they occur together.
- **Alignment** - making a system pursue what its designers actually intended.
- **Accountability** - a named person or organisation responsible for a system's effects.
- **Edge case** - a rare input at the boundary of normal operation.

## The Explanation

### Step 1 - Know what the methods cannot do

Four limits are worth memorising, because you will meet them in every course.

**Limit 1: pattern is not cause.** A model that sees ice-cream sales rise with drowning deaths has found a real pattern and the wrong story. The cause is summer. Models trained on correlation will happily recommend an action that does nothing, or makes things worse.

**Limit 2: the training data is the world, as far as the model knows.** Change the camera, the accent, the dialect, the lighting, the demographic, and performance can fall off a cliff. The model has no way to notice that it is now outside its experience.

**Limit 3: no common sense.** A language model can write a perfect recipe and suggest putting the pan in the fridge to cool the sauce. Large amounts of text do not automatically produce an understanding of physics, time or embarrassment.

**Limit 4: confidence is not calibrated.** A network's 0.99 output is a number produced by arithmetic. Unless you have measured calibration on held-out data, it tells you nothing about the chance of being right.

For each limit, there is an engineering response: use causal experiments where decisions matter, test on shifted data, add rule-based checks for physical impossibilities, and calibrate confidence before anyone acts on it.

### Step 2 - Name the risks in the language of consequences

Risks are easier to handle when they are specific. Consider four categories.

**Safety.** A robot that misjudges a person's position can injure them. The response is a safety layer that does not depend on the learned model: physical bumpers, force limits, speed reduction near people, and an emergency stop that always works.

**Fairness.** A hiring model trained on ten years of decisions by people who favoured one group will reproduce that favour, with the added authority of mathematics. The response is to measure outcomes by group, to ask whether the label is even the right thing to predict, and to keep a human decision-maker accountable.

**Privacy.** Cameras in public and private spaces, microphones in homes, and records that never expire. The response is to collect less, keep it for less time, and be explicit with the people affected.

**Power.** The concentration of capability in a few organisations, and the use of automated systems to make decisions about people who cannot contest them. The response is governance: audit, appeal, transparency and law. You will meet all of this again in Courses 15, 38 and 40.

A useful discipline: for each risk, write the harm, who bears it, and who can prevent it. If the answer to the third question is "nobody", the design is not ready.

### Step 3 - Plan your own path through the next 47 courses

You now know what intelligence means in a machine, where the idea came from, how an agent is structured, how it searches, reasons, learns from data and handles uncertainty, how it sees and hears, and how systems succeed or fail in the real world.

The rest of the book builds the machine, piece by piece:

- **Courses 2–6** give you the physical body, the learning tools, the eyes, the language and the control loop.
- **Courses 7–12** give you the engineering skills: algorithms, signals, embedded code, interaction design, neural networks, graphics.
- **Courses 13–18** connect machines to the world and to each other, and start the ethical conversation properly.
- **Courses 19–24** make robots move, learn, reason with degrees of truth, and compute their own geometry.
- **Courses 25–30** add immersive interfaces, physical-digital systems, teams of robots, software architecture, cognition and biology.
- **Courses 31–36** turn all of it into dependable industrial and social systems.
- **Courses 37–42** push into advanced practice: evolution, ethics as design, learning on real hardware, manipulation, perception.
- **Courses 43–48** finish with navigation, planning, simulation, design and your own capstone project.

A study plan that works: read one chapter in the morning, do the mini-lab in the afternoon, and answer the three questions aloud a week later. Do not read three chapters in one day and none for a month. The book is built for steady repetition, and so is your memory.

## Where It Goes Wrong

**Mistake 1 - Assuming a good average means a safe edge.** *Fix:* test the odd cases on purpose, and report worst-case performance beside the average.

**Mistake 2 - Treating the model as the whole system.** *Fix:* draw the chain from Chapter 9 and give every link an owner.

**Mistake 3 - Believing a confident output.** *Fix:* calibrate the confidence, and never let a single number authorise an irreversible action.

**Mistake 4 - Skipping the ethics because "we are only engineers".** *Fix:* write the harm list. You are the last person who can still change the design cheaply.

**Mistake 5 - Learning tools without learning judgement.** A student who can call a deep learning library but cannot frame a problem will build the wrong thing faster. *Fix:* practise framing, measuring and questioning, which is what this course has been about.

## Case Note

In 2018, a woman in Arizona was struck and killed by a self-driving test vehicle. Investigations found that the software had detected an object but had repeatedly changed its classification — vehicle, other, bicycle — and its predicted path, and the system's design did not give it a way to treat "an unknown object in the road" as a reason to slow down. The safety driver was looking away.

The technical lesson is precise: uncertainty about *what* an object is must not stop the system from acting on *where* it is. A good design slows for anything solid on the road, whatever its label, because the cost of being wrong is not symmetrical.

The wider lesson is about culture. The system had a safety driver because someone had judged the technology not yet ready. That judgement was right, and the safeguard failed because a human was asked to stay vigilant for hours with nothing to do. Vigilance is not a safety system. Engineering is.

## Mini-Lab

**You need:** paper, a pen, and one willing person.

**Do this:**
1. Choose an AI system you use weekly.
2. Write its four limits: where it confuses pattern with cause, where its data is narrow, where it lacks common sense, where its confidence may be uncalibrated.
3. Write one harm it could cause, who bears that harm, and who could prevent it.
4. Design one check that does not depend on the model — a rule, a second sensor, or a human review.
5. Explain the check to your willing person in 60 seconds. Ask them to repeat it back.

**What you should see:** the check is easy to design once the harm is named, and hard to explain if it is vague. Clarity is the test.

**Why it matters:** this is the habit that separates an engineer people trust from one they do not.

## Recap and Questions

**Three things to remember**

1. Today's AI is powerful on average, narrow by design, and fragile at the edges — and it fails confidently.
2. Confidence must be calibrated, and any irreversible action needs a check that does not depend on the model alone.
3. Ethics is design work. The cheapest moment to prevent harm is before the system exists.

**Check yourself**

1. Why is "the model was 99% accurate" not a defence after an accident?
2. What is the difference between a pattern and a cause, and why does it matter for decisions?
3. Name one thing you personally will not build, and the reason in one sentence.

**One thing to try next**

Write a one-page "limits and risks" note for the project you would most like to build. Keep it. In four years, when you build that project for your capstone, read it first.
