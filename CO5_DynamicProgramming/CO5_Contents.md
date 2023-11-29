# Dynamic Programming

Dynamic Programming is a general algorithm design technique for solving problems defined by or formulated as recurrences with overlapping sub-instances (sub-problems).

### Difference between Divide and Conquer and Dynamic Programming

Programming means deciding to make a function call or look into the table.

**Main idea:**
- Set up a recurrence relating a solution to a larger instance to solutions of some smaller instances.
- Solve smaller instances once.
- Record solutions in a table.
- Extract solution to the initial instance from that table.

**Example: Fibonacci Numbers**

Recall definition of Fibonacci numbers:

\[ F(n) = F(n-1) + F(n-2) \]

\[ F(0) = 0 \]

\[ F(1) = 1 \]

Computing the nth Fibonacci number recursively (top-down):

```
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

## Bellman-Ford Algorithm

## Overview

The Bellman-Ford algorithm solves the single-source shortest path problem, even in the presence of negative weight cycles. Unlike Dijkstra’s algorithm, Bellman-Ford can handle graphs with negative weight edges and is capable of identifying the existence of negative weight cycles.

### Use Cases

- Finding shortest paths in graphs with negative weight cycles.
- Identifying the presence of negative weight cycles.

### Pseudo Algorithm

```markdown
Bellman-Ford(G, w, s)
{
    Initialize single source(G, s)
    
    for i = 1 to |V| - 1
    {
        for each edge (u, v) ∈ G.E
        {
            relax(u, v, w)
        }
    }

    for each edge (u, v) ∈ G.E
    {
        if (v.d > u.d + w(u, v))
            return False
    }

    return True
}
```
### Explanation
- Initialize single source(G, s): Set the distance of the source vertex s to 0 and all other vertices to infinity.
- Relaxation (relax): Update the distance estimates for vertices based on the current shortest paths.
- Main Loop: Repeat the relaxation step |V| - 1 times (where |V| is the number of vertices).
- Negative Weight Cycle Check: After the main loop, check for negative weight cycles. If any vertex's distance can be further reduced, a negative weight cycle exists.

**Time complexity:** O(EV), where E is the number of edges and V is the number of vertices

---

# Floyd’s Algorithm

## Problem Statement

Given a graph, find the shortest path between each pair of vertices.

- **Problem Type:** All-pair shortest path problem.
- **Input:** Weighted graph (weighted matrix).
- **Output:** Distance matrix.

### Overview

Floyd's algorithm is a dynamic programming approach to find the shortest paths between all pairs of vertices in a weighted graph.

### Pseudo Algorithm

```markdown
Algorithm FloydWarshall(graph):

    n = number of vertices in graph
    
    create a 2D array dist of size n x n
    
    // Initialize the distance array with the given graph
    for each vertex i in range(n):
        for each vertex j in range(n):
            dist[i][j] = graph[i][j]
            
    // Update the distance matrix using all vertices as intermediates
    for each vertex k in range(n):
        for each vertex i in range(n):
            for each vertex j in range(n):
                // If vertex k is on the shortest path from i to j, then update dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
```
#### Time Complexity
The time complexity of Floyd's algorithm is O(n<sup>3</sup>), where n is the number of vertices in the graph.