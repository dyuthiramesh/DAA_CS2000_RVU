# Limitations of Algorithmic Power

## Motivation

Which of the following do you think is easy to prove, given a problem P:

1. It is possible to solve problem P?
2. It is not possible to solve problem P by anyone?

## NP Completeness Theory

### Problem Types

#### Problem Types Cont.

### Example

- Shortest path problem - O(Elogv)
- Euler’s Tour - O(E)
- Hamiltonian cycle - O(n!)
- Travelling Sales Person problem - O(n<sup>2</sup>.2<sup>n</sup>)

### Travelling Sales Person (TSP) problem

Given Graph G = (V, E), consider each vertex represents a city. Find the shortest tour such that each vertex is visited exactly once except the starting vertex.

### Hamiltonian Cycle

Given Graph G = (V, E), consider each vertex represents a city. Find a tour such that each vertex is visited exactly once except the starting vertex.

### Brute Force Approach

What is the time complexity?

### Dynamic Programming: Optimal substructure

#### Optimal substructure:

A problem is said to have an optimal substructure property if an optimal solution can be constructed from optimal solutions to its subproblems.

### TSP: Dynamic Programming Approach

# Limitations of Algorithmic TSP: Dynamic Programming Approach

The Traveling Salesman Problem (TSP) using Dynamic Programming can be expressed through the following recursion:

```markdown
T(1, {2,3,4}) = min{(1,2) + T(2, {3,4}), (1,3) + T(3, {2,4}), (1,4) + T(4, {2,3})}
T(2, {3,4}) = min{(2,3) + T(3, {4}), (2,4) + T(4, {3})}
T(3,{2,4}) = min{(3,2) + T(2, {4}), (3,4) + T(4, {2})}
T(4, {2,3}) = min{(4,2) + T(2, {3}), (4,3) + T(3, {2})}
T(3,{4}) = (3,4) + T(4, Φ)
T(4,{3}) = (4,3) + T(3, Φ)
T(2,{4}) = (2,4) + T(4, Φ)
T(4,{2}) = (4,2) + T(2, Φ)
T(2,{3}) = (2,3) + T(3, Φ)
T(3,{2}) = (3,2) + T(2, Φ)
```

**Recurrence relation:**
\[ T(i, S) = \min_{j \in S} \left\{ (i,j) + T(j, S - \{j\}) \right\}; \quad S \neq \emptyset \]

\[ T(i, 1); \quad S = \emptyset \]

**Recursion Tree**

**Time Complexity Analysis**

- **Number of subproblems:** \( (n-1)2<sup>n-2</sup> \)
- **Time complexity:** \( O(n<sup>2</sup> 2<sup>n</sup>) \)
- **Space Complexity:** \( O((n-1)2<sup>n-2</sup>) \)

**What do you think is special about this problem compared to other problems that we discussed?**

# Knapsack Problem

Given a knapsack (bag) having

- a capacity \( m \),
- number of objects \( n \),
- each object weight (\( w \)) and
- corresponding profits (\( p \)).

The objective is to fill the bag/knapsack with the objects such that the profit is maximum.

**Example**

**Greedy Programming**

Greedy about profit

Greedy about weight

Greedy about profit/weight ratio

**Algorithm Greedy_Knapsack(m, n, w, p)**

```
for i=1 to n do
    compute pi/wi

sort objects in non-increasing order of p/w

for i=1 to n do
    if (m > 0 and wi <= m)
        m = m - wi
        p = p + pi
    else
        break

if m > 0
    p = p + pi(m/wi)
```

# Limitations of Algorithmic Power

## Dynamic programming based solution

Before DP, can we think of a brute force algorithm for this?

How many subproblems are possible?

### Recurrence relation
```
\[ KS(i, W) = \max \{ p_i + KS(i-1, W - w_i), \ KS(i-1, W) \}, \quad w_i \leq W \]

\[ KS(i-1, W) ; \quad w_i > W \]

\[ 0 ; \quad i=0 \ \text{or} \ W=0 \]
```
### Example

```
Algorithm Knapsack()
{
    // INPUT: {w1, w2, w3, …., wn}, C, {p1, p2, p3, …, pn}
    // OUTPUT: T[n, c]
    for i=0 to C do
        T[0, i] = 0

    for i=0 to n do
        T[i, 0] = 0

    for j=1 to C do
        if w_i <= j and T[i-1, j-w_i] + p_i > T[i-1, j] then
            T[i, j] = p_i + T[i-1, j-w_i]
        else
            T[i, j] = T[i-1, j]
}
```

# Limitations of Algorithmic Power

## Time and Space Complexity Analysis

### Brute Force Approach:

- **Space Complexity:** O(2<sup>n</sup>)
- **Time Complexity:** O(2<sup>n</sup>)

### Bottom-up Dynamic Programming:

- **Space Complexity:** O(nW)
- **Time Complexity:** O(nW)

**Which approach do you think is efficient in terms of both space and time efficiency and why?**

# Tackling Difficult Combinatorial Problems

There are two principal approaches to tackling difficult combinatorial problems (NP-hard problems):

1. Use a strategy that guarantees solving the problem exactly but doesn’t guarantee to find a solution in polynomial time.
2. Use an approximation algorithm that can find an approximate (sub-optimal) solution in polynomial time.

## Exact Solution Strategies

1. **Exhaustive search (brute force):**
   - Useful only for small instances.
  
2. **Dynamic programming:**
   - Applicable to some problems (e.g., the knapsack problem).
  
3. **Backtracking:**
   - Eliminates some unnecessary cases from consideration.
   - Yields solutions in reasonable time for many instances but worst case is still exponential.

## Backtracking

1. **Construct the state-space tree:**
   - Nodes: partial solutions
   - Edges: choices in extending partial solutions

2. **Explore the state space tree using depth-first search:**
   - "Prune" nonpromising nodes.
   - DFS stops exploring subtrees rooted at nodes that cannot lead to a solution and backtracks to such a node’s parent to continue the search.

## Example: n-Queens Problem

Place n queens on an n-by-n chess board so that no two of them are in the same row, column, or diagonal.

### State-Space Tree of the 4-Queens Problem

```
Algorithm Nqueens(Board[n][n], col)
{
    if col >= n // all queens are arranged
        return True
    
    for i 🡨 1 to n do
        if isSafe(Board, i, col)
            board[i][col] = 1
            
            if Nqueens(board, col + 1)
                return True
    
            board[i][col] = 0

    return False
}
```
## Problem Types

### Decision Problems

**Optimization Problem**

#### Decision Problem Examples:

1. **TSP (Traveling Salesman Problem):**
   - Given a graph G, find the shortest path covering all the vertices exactly once.
   - Decision Problem: Is there any shortest path covering all vertices that is of length at most K? (Answer Yes/No)

2. **0/1 Knapsack Problem:**
   - Given C (capacity), P (profit), W (weight), find the solution that makes the maximum profit.
   - Decision Problem: Is there any solution whose profit is at least K? (Answer Yes/No)

#### Key Points to Remember

- If the optimization problem is tractable (easy), then the decision problem of it is also tractable.
- If the decision problem is intractable (hard), then its optimization problem is intractable.

### Verification Algorithm

- Given a graph, decision problem, and an instance to verify.
- Example: Given the graph A-B-C-D-A, does this graph have a Hamiltonian cycle?

## P, NP Problems

- **P (Polynomial):** Set of all decision problems for which there is a polynomial time algorithm to solve it.
- **NP (Nondeterministic Polynomial):** Set of all decision problems for which there is a polynomial time verification algorithm.

### Examples:

- **P Problems:** Given a graph, is there an MST (Minimum Spanning Tree) with cost at most 10.
- **NP Problems:** TSP, 0/1 Knapsack Problem

### Is P = NP or not?

- Most researchers believe that P ⊂ NP.
- To prove P = NP or not:
  - If all problems in NP-P can be solved in polynomial time, then P != NP.
  - Show at least one problem in NP-P cannot be solved in polynomial time.

## Polynomial Time Reduction

- A problem A is polynomial time reducible to a problem B if:
  - Every instance α of A can be transformed to some instance β of B in polynomial time.
  - Answer to 'α' is yes if and only if the answer to 'β' is yes.

### Example:

- **Problem A:** Given n Boolean variables with values x1, x2, x3, …, xn, does at least one variable have the value True?
- **Problem B:** Given n integers i1, i2, i3, …, in, is max(i1, i2, i3, …, in) > 0

## NP-Hard & NP - Complete

- If every problem in NP can be polynomial time reducible to a problem A, then A is called an NP-Hard problem.
- If A is in NP and it is NP-Hard, then problem A is called NP-Complete.
