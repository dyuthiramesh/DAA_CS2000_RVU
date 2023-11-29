# Decrease & Conquer

## Decrease-and-Conquer

- Reduce problem instance to a smaller instance of the same problem.
- Solve the smaller instance.
- Extend the solution of the smaller instance to obtain a solution to the original instance.

### Example

- Problem of size n
- Solve for n - 1 (or n - constant factor)
- Repeat the above until the problem is reduced to something trivial (n = 1 or n = 0).

Can be implemented using either iteration or recursion.

## Divide and Conquer VS Decrease and Conquer

**Decrease and Conquer**

- Involves reducing the problem into 1 sub-problem.

**Divide and Conquer**

- Reduces the problem into several subproblems.

## 3 Types of Decrease and Conquer

1. Decrease by a constant (usually by 1):
   - Insertion sort
   - Graph traversal algorithms (DFS and BFS)
   - Topological sorting

2. Decrease by a constant factor (usually by half):
   - Binary search and bisection method

3. Variable-size decrease:
   - Euclid’s algorithm

## Insertion sort algorithm

```
Algorithm InsertionSort(A):
    for i = 1 to n-1:
        temp = A[i]
        j = i-1
        while (j>=0 and A[j] > temp):
            A[j+1] = A[j]
            j = j-1
        A[j+1] = temp
```

### Insertion Sort Examples

**Example 1:** 9 6 5 0 8 2 7 1 3

**Example 2:** 89 45 68 90 29 34 17

## Analysis of Insertion Sort

### Time Efficiency

- Best case: Ω(n)
- Worst case: O(n^2)
- Average case: Θ(n^2)

### Space Complexity

- O(1)

### Stability

- Yes

---
## Graph Traversal

Many problems require processing all graph vertices (and edges) in a systematic fashion.

Graph traversal algorithms:

- Breadth-first search (BFS)
- Depth-first search (DFS)

Note that these algorithms are exhaustive search algorithms.

## BFS & DFS Introduction

### Terminology

- Visited
- Explored

### Algorithm BFS(v)

```
u = v
visited[v] = 1
Repeat
  for all vertices w adjacent to u do
    if visited[w] == 0
      add w to q
      visited[w] = 1
  If q is empty then return
  Deque element from q and assign it to u
```

```
Algorithm BFT(G,v)
{
for i = 1 to v do
  visited[i] = 0
for i=1 to v do
  if visited[i] == 0:
    BFS(i)
}
```

# Space and Time Efficiency

**Adjacency Matrix:**
- Time Complexity: O(V^2)

**Adjacency List:**
- Time Complexity: O(E + V)
- Space Complexity: O(V)

## Difference between Search and Traversal

- **Search:** Looking for a specific node or vertex.
- **Traversal:** Visiting all nodes/vertices in a graph or tree.

## BFS for Graph Connectivity

Yes, BFS can be used to find whether a graph is connected or not.

---

# Depth First Search

## Recursive Algorithm

```
Algorithm DFS(v)
{
    visited[v] = 1
    for each vertex w adjacent to v do
    {
        if visited[w] == 0 then
            DFS(w)
    }
}

Algorithm DFT(G,v)
{
    for i = 1 to v do
        visited[i] = 0
    for i = 1 to v do
        if visited[i] == 0
            DFS(i)
}
```

### Space and Time Efficiency
#### Adjacency Matrix Representation
If the graph is represented using an adjacency matrix:
- Time Complexity: O(V^2)
#### Adjacency List Representation
If the graph is represented using an adjacency list:
- Time Complexity: O(E + V)

Space Complexity: O(V)

BFS and DFS Forest in Directed Graphs
For BFS forest:

Tree edges
Cross edges
For DFS forest:

Tree edges
Back edges
For a directed graph (digraph), DFS forest will have:

Tree edges
Back edges
Forward edges
Cross edges

---

## Topological Sorting

In a directed graph or digraph, DFS forest will have tree edges, back edges, forward edges, and cross edges.

If a DFS forest of a digraph has no back edges, the graph is a Directed Acyclic Graph (DAG).

Topological Sort of a DAG:

A linear ordering of all its vertices.
For every directed edge (u, v), u appears before v in the ordering.
If the digraph contains a cycle, no linear ordering is possible.

Topological Sort Algorithm (DFS-Based):
```
Algorithm Topological_Sort(G)

Call DFS(G) to compute finish time for each vertex.

As each vertex is finished, insert it onto the beginning of the linked list.

Traverse nodes in the linked list.
```

Topological Sort Algorithm (Source Removal Technique):
```
Algorithm Topological_Sort_Source_Removal(G)

Step 1: Find in-degree of each vertex.

Step 2: Identify a source in the graph (remaining graph), which is a vertex with in-degree = 0, delete it along with all its outgoing edges from it and enqueue it to Queue. (If there are many source vertices, break the tie arbitrarily)

Step 3: Repeat steps 1 and 2 until all vertices are removed.

The order in which vertices are deleted is the solution to the topological sorting problem.

The ordering is different compared to Topological ordering using DFS.
```

### Time & Space Efficiency of Topological Sorting:

DFS-based topological sorting:

Space complexity – O(V)
Time complexity – O(E + V) (adjacency list), O(V^2) (adjacency matrix)
Source removal technique:

Space complexity – O(V)
Time Complexity – O(E + V) (adjacency list), O(V^2) (adjacency matrix)

---

## Binary Search (Decrease by a Constant Factor)

Binary Search is an algorithm for searching a key in a sorted array.

Input: Sorted array of elements, key K.

It works by comparing a search key K with the array’s middle element.

If they match, the algorithm stops; otherwise, the same operation is repeated recursively.

For the first half, if K < A[m], and for the second half if K > A[m].

```
Algorithm BinarySearch(A, low, high, Key)

// Input: An array sorted in ascending order, Key value
// Output: Index of the array element that is equal to Key, otherwise -1

if (low > high)
    return -1

mid = floor((low + high) / 2)

if Key == A[mid]
    return mid
else if Key < A[mid]
    return BinarySearch(A, low, mid - 1, Key)
else
    return BinarySearch(A, mid + 1, high, Key)
```
Time and Space Efficiency:
- Space Complexity: O(1)
- Time complexity: O(log2n)

Recurrence relation: 
T(n) = T(n/2) + 1; n > 1
1 ; n = 1

---

## Fake Coin Problem

This problem belongs to decrease by a constant factor.

Objective: To identify a fake coin among the given set of n identical coins.

Fake coin is the one which weighs more or less when compared to other coins. (Assume the fake coin weighs less)

The basic idea to solve this problem is to divide n coins into 2 piles(partitions) of floor(n/2) each, leaving one coin extra if n is odd.

Weigh two piles on a weighing scale to see any difference in weight.

If the piles weigh the same, the coin put aside is the fake coin.

Example:

Number of coins,

n = 9 (odd)
N = 8 (even)

Recurrence relation:
T(n) = T(n/2) + 1; n > 1
1 ; n = 1