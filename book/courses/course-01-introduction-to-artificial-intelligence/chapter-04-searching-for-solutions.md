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
