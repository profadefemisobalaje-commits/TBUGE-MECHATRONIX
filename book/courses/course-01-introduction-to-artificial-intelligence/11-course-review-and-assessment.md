# Course 1: Review, Assessment and Glossary

## Part A - Twelve review questions

Answer each in plain English, in no more than 120 words. Suggested answers follow the questions.

1. Define intelligence as this book uses the term, and give one example of a system that is fast but not intelligent.
2. Why does the AI effect make the label "AI" unreliable as evidence of capability?
3. A model scores 93% accuracy. What three numbers do you need before you can judge it?
4. Write a PEAS description for an automatic lawn mower.
5. Name the five properties of an environment and explain which one rules out simple reflex agents.
6. Why does breadth-first search need so much more memory than depth-first search?
7. What does it mean for a heuristic to be admissible, and what happens if it is not?
8. Give one task where a rule-based system is a better choice than a learned model, and say why.
9. Explain, without using the word "overfitting", why a model that scores 100% in training may fail in use.
10. A test is 95% sensitive, has a 5% false positive rate, and the condition affects 1 in 1,000 people. Is a positive result strong evidence? Explain.
11. Why can a vision system be fooled by a change that a person cannot see?
12. Name two limits of today's AI and one engineering response to each.

### Suggested answers

1. Intelligence is the ability to choose actions that reach a goal in unfamiliar situations. A calculator is fast and never chooses; it does exactly what it is told.
2. Once a problem is solved, we stop calling it AI and call it engineering, so the label follows novelty, not capability. Ask what the system senses, chooses and how it was tested.
3. The baseline score of a trivial method, the number of examples, and the mistakes split by type (precision and recall, or a confusion matrix).
4. Performance: lawn covered, no injuries, battery managed. Environment: garden, slopes, toys, pets, weather. Actuators: drive wheels, blade motor. Sensors: bumpers, lift sensor, camera or boundary wire, battery monitor.
5. Fully or partially observable, deterministic or stochastic, static or dynamic, discrete or continuous, single or multi-agent. Dynamism rules out reflex agents, because the world changes while the agent decides. Partial observability also rules them out, because they have no memory.
6. BFS must keep every state in the current ring so it can generate the next ring. The ring size grows exponentially with depth, while DFS keeps only one path.
7. Admissible means the heuristic never overestimates the true remaining cost. If it overestimates, A* may return a path that is not the shortest, and it does so without warning.
8. Any task with auditable safety requirements, such as "never open the door while moving", or diagnosis with a small, stable, expert-agreed rule set. Rules can be read, checked and traced by a human.
9. Because the model has memorised the particular examples it was shown instead of the general pattern. When a new example arrives, the memorised details do not help.
10. Not strong. In 100,000 people, 100 have the condition: 95 true positives. Of the 99,900 without it, 5% give 4,995 false positives. So a positive result is right about 95 in 5,090, under 2%.
11. Because the network uses whatever features reduce error on its training data, and those need not be the features a person uses. A tiny change can flip the answer while leaving the picture unchanged to human eyes.
12. Pattern is not cause — respond with controlled experiments before acting. No common sense — respond with rule-based checks that reject physical impossibilities. Brittleness — respond with testing on shifted data and a safety layer that does not depend on the model.

## Part B - Three lab assignments

**Lab 1: The search trace (10%)**
Choose a 6 × 6 grid with five walls. Produce, by hand, three traces: breadth-first, depth-first and A* with Manhattan distance. For each, report the path, the path cost, and the number of states expanded. Write 200 words explaining which one you would put in a robot with 64 kB of memory and why.

**Lab 2: The hand-built classifier (15%)**
Collect or invent 20 examples with two features and one label. Hide four before you start. Build a threshold rule using only the visible sixteen. Report the confusion matrix on the hidden four, and write 200 words on which mistake is more expensive and why.

**Lab 3: The probability calculation (15%)**
A door sensor has sensitivity 0.92 and a false positive rate of 0.08. Doors are actually open in 15% of readings. Compute the probability a door is open given one positive reading. Then compute it given two independent positive readings. Write 200 words on how many readings you would require before letting a robot pass through.

Each lab is marked on three things, equally weighted: the correctness of the numbers, the clarity of the explanation, and whether the conclusion matches the numbers.

## Part C - Mini project (30%)

Write a two-page framing of a real problem that an AI system could address. It must contain:

1. The problem in one sentence, with the person who suffers from it.
2. The input, the output and the measure of success.
3. The time limit and the error budget, split by type of mistake.
4. The six links of the system chain, each with its biggest failure risk.
5. Three risks in the language of consequences: the harm, who bears it, who can prevent it.
6. One check that does not depend on the learned model.

Two pages, plain English, no jargon that is not defined. A project that cannot state its error budget is not ready, and will be returned unmarked.

## Part D - Glossary of key terms

- **Agent** - anything that senses its environment and acts on it.
- **AI effect** - calling a solved problem "not really AI".
- **A\*** - search ordered by cost so far plus estimated cost to go.
- **Base rate** - how common a condition is in the population.
- **Baseline** - the score a trivial method gets.
- **Bias** - a systematic error that disadvantages a group or situation.
- **Brittleness** - failing badly on inputs unlike the training data.
- **Confusion matrix** - a table of predictions against true labels.
- **Data drift** - live data slowly diverging from training data.
- **Embedding** - a list of numbers representing a token.
- **Error budget** - the mistakes a system is allowed to make, by type.
- **Feature** - a measurable input used by a model.
- **Generalisation** - doing well on data the model has not seen.
- **Heuristic** - an estimate of the cost still to go.
- **Inference** - deriving new facts from known ones.
- **Overfitting** - fitting training data so closely that new data fails.
- **PEAS** - Performance, Environment, Actuators, Sensors.
- **Percept** - one reading of the environment.
- **Policy** - the agent's rule for choosing an action.
- **Precision** - of the cases flagged, the fraction that were real.
- **Recall** - of the cases that were real, the fraction flagged.
- **Spectrogram** - a picture of sound showing frequency over time.
- **Token** - a small unit of text used by a language model.

## Part E - Further reading

- Turing, A. M. (1950). *Computing Machinery and Intelligence*. The paper that replaced a philosophical question with a test.
- Russell, S. and Norvig, P. *Artificial Intelligence: A Modern Approach*. The standard reference; use it for depth after each chapter here.
- Wooldridge, M. *An Introduction to Multiagent Systems*. Clear treatment of agents and environments.
- Goodfellow, I., Bengio, Y. and Courville, A. *Deep Learning*. For Courses 11 and 22; the early chapters are readable now.
- Sutton, R. and Barto, A. *Reinforcement Learning: An Introduction*. Free online; the first three chapters pair well with Course 17.
- National Transportation Safety Board reports on automated vehicle crashes. Dry, precise, and the best source of real failure cases.
