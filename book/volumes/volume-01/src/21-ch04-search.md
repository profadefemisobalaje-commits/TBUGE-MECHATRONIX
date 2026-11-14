# Search: The First Real Trick

At two in the morning, in a distribution centre outside Rotterdam, a robot the size of a dining table receives an order: collect a pallet from aisle 14 and bring it to bay 3. The building is 120 metres long and 60 wide. Between the robot and the pallet stand forty steel racks, a charging station, two parked forklifts and a puddle nobody has logged. The robot cannot see the pallet from where it stands. It has a map, a plan, and about eighty milliseconds in which to commit to a first move.

What happens in those eighty milliseconds is not learning, and it is not reasoning about meaning. It is search: the systematic exploration of possible sequences of moves until one is found that reaches the goal. Search is the oldest technique in artificial intelligence that still works exactly as advertised, and it is the backbone of every planner in this book, from a warehouse robot choosing a route to a robot arm choosing a path through a cluttered bench.

## Five Lines That Define a Problem

Every search problem, however large, is described in the same five lines. Getting these lines right is most of the work.

**The states.** What is a snapshot of the situation? For the warehouse robot, a state is its cell on a grid: row and column.

**The start.** Where the search begins: cell (0, 0), the charging bay.

**The actions.** What the robot can do from a state: move one cell up, down, left or right.

**The goal test.** A question with a yes or no answer: are we at cell (7, 5)?

**The path cost.** What each move costs. One per cell is simple, but a ramp might cost two because it is slower, and a wet patch might cost three because the robot must slow down.

Notice that the description contains no algorithm at all. It is a description of the world, and once you have it, several algorithms can be pointed at it. This separation matters, because it means you can change your method later without rewriting your model of the world.

The description is also a **graph**: states are nodes, actions are edges, costs are edge weights. That is why search and data structures share so much machinery, and why the volumes on algorithms and on robot planning return to this chapter.

## Rings and Dives

The simplest search, **breadth-first**, explores in rings. It looks at all states one move away, then all states two moves away, and so on. Because it finishes each ring before starting the next, the first time it reaches the goal it has found the path with the fewest moves.

Breadth-first keeps a queue — first in, the first out — of states discovered but not yet explored. That queue is called the **frontier**, and it is the only bookkeeping the algorithm needs.

**Depth-first** uses the same idea with one change: it keeps a stack instead of a queue, so the most recently discovered state is explored next. It dives down one branch until it hits a dead end, then backs up and tries another. It finds *a* path quickly and uses very little memory, but the path it finds can be long and strange.

The difference becomes brutal as the map grows. Suppose each state has ten possible actions and the solution is six moves deep.

- Breadth-first may need to hold about a million states in memory at the deepest ring it touches. At 100 bytes each, that is 100 MB.
- Depth-first needs roughly 60 states, a few kilobytes.

Sixteen thousand times less memory, at the cost of a path that may be three times longer. This trade-off — memory against quality — is the first genuine engineering decision in the subject, and it recurs in every robot planner you will meet.

There is a cheap way to have most of both. **Iterative deepening** runs depth-first with a limit of one move, then two, then three, until it finds the goal. It uses depth-first memory but finds the shortest path, because the first depth at which the goal appears is its distance. It repeats work, but the repeated work is small compared with the final ring, so the total is only slightly worse than breadth-first and the memory saving is enormous.

## The Guess That Saves a Shift

Search that knows nothing about direction is called blind, and blind search wastes almost all its time. On the warehouse map, breadth-first explores cells behind the robot with the same enthusiasm as cells in front of it.

Give it a **heuristic** — a guess at the distance still to go — and the picture changes. For a grid without obstacles, the number of moves between two cells if nothing were in the way is a good guess, and it is easy to compute: the difference in rows plus the difference in columns. Engineers call this the Manhattan distance, after the city grid that inspired it.

The algorithm that uses such a guess is called **A-star**, published by Peter Hart, Nils Nilsson and Bertram Raphael in 1968. It orders the frontier by a single number, f, which is the sum of g, the cost already paid to reach a state, and h, the estimate of the cost still to come. It always expands the state with the smallest estimated total.

Work through a small case. The robot is at (0, 0); the goal is (7, 5); a block of shelves occupies columns 3 and 4, rows 1 to 4.

- From the start, h is 7 + 5 = 12 moves. g is 0, so f is 12.
- Its neighbours have g = 1. The one moving right has h = 6 + 5 = 11, so f = 12. The one moving up has h = 7 + 4 = 11, also f = 12.
- Breadth-first would eventually expand about forty cells. A-star expands roughly fifteen, all of them within a narrow band between start and goal, because every cell far from that band has a large h and waits at the back of the queue.

On a realistic 200 by 200 map the difference is not a factor of three. It is a factor of thousands, and it is the difference between a planner that answers in five milliseconds and one that stalls for two seconds while the forklifts wait.

### The condition that makes the guess safe

A-star is guaranteed to find the shortest path only if the heuristic never overestimates the true remaining cost. That property is called **admissibility**, and straight-line distance has it, because you cannot travel less than the straight line.

Break it and the failure is silent. Multiply every estimate by 1.2 to “encourage” the search toward the goal, and A-star will sometimes return a path that is not the shortest, while reporting success. No error appears. No warning is printed. The robot simply takes a slightly worse route, forever, and nobody knows.

The test is easy and rarely done: on a small map, run A-star and run breadth-first, and compare the path costs. If A-star is worse, the heuristic is lying somewhere. Ten minutes of checking on a toy problem is worth more than a week of tuning on the real one.

| Method | Memory | Shortest path? | Needs a guess? | Typical use |
|---|---|---|---|---|
| Breadth-first | High | Yes | No | Small maps, few moves |
| Depth-first | Low | No | No | Existence checks, mazes |
| Iterative deepening | Low | Yes | No | Games with a time limit |
| A-star | Medium | Yes, if the guess is safe | Yes | Route planning, motion planning |

## The Price of Looking Ahead

Every search has a budget, and the budget is almost always time. The number of states grows exponentially with depth: with a branching factor of 10, depth 6 gives a million states, depth 8 gives a hundred million, and depth 10 gives ten billion. No amount of cleverness changes that curve. Cleverness only changes how much of the curve you have to touch.

This is why practical systems do three things at once. They use heuristics to avoid most of the graph. They prune branches that cannot possibly beat the best path found so far — a technique called branch and bound, and, in two-player games, alpha-beta pruning. And they stop when the clock runs out and return the best answer so far, rather than the perfect answer too late.

That last habit is worth adopting early. In a robot, a good plan that arrives in time is worth more than a perfect plan that arrives after the collision.

## A Machine That Looks Ahead

Deep Blue, which we met in the history chapter, is the most famous demonstration of search under a deadline. Its strength came from two components working together: special-purpose hardware that examined roughly two hundred million positions per second, and an evaluation function that scored a position by counting material, king safety, pawn structure and dozens of other features, tuned with the help of strong human players.

In the middle game it looked ahead only six to eight moves, sometimes more where the position was forced. Garry Kasparov could look further in the lines that mattered, because he could tell which lines mattered. The machine could not tell, so it looked at everything it could reach in the time available.

That is the honest picture of search in artificial intelligence. Machinery buys breadth. Heuristics buy direction. With neither, you have nothing; with both, you can beat a world champion inside a world with exact rules. And note what Deep Blue could not do: it could not recognise a chessboard in a photograph, explain a move to a beginner, or play any other game. It was, in the terms of the first chapter, extremely intelligent inside an extremely small box.

## Problems

1. Draw a six by six grid. Mark the start at the bottom left and the goal at the top right. Blacken five cells as walls, leaving a route.

2. On three copies of the grid, trace breadth-first search, depth-first search, and A-star with the Manhattan distance. Number each cell as you expand it. Record three things for each: the path, its cost in moves, and the number of cells expanded.

3. Suppose each cell also has a cost of 1, except two cells on a ramp, which cost 3. Which of your three traces still returns the cheapest path? Explain the answer in one sentence.

4. A warehouse planner returns a path of 14 moves when the shortest is 12. What is the most likely cause, and what single test would confirm it?

5. Write the five-line description for a problem you solved today without thinking: finding a seat in a crowded room, or packing a bag. Then decide whether you searched in rings, dived, or used a guess.
