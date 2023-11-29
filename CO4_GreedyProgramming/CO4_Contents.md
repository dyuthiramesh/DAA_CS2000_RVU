# Greedy Design Technique

Greedy design technique constructs a solution to an optimization problem piece by piece through a sequence of choices that are:

- Feasible (satisfying the problem’s constraints)
- Locally optimal (best local choice among all feasible choices)
- Greedy (in terms of some measure)
- Irrevocable (once made cannot be changed on subsequent steps of the algorithm)

For most problems, it yields a globally optimal solution. For a few, it does not, but we are mostly interested in the former case in this class.

## Coin Change Problem

Solve this problem using the greedy technique.

### Coin Denominations:

1. {25, 10, 5, 1}, n = 48
2. {25, 10, 5, 1}, n = 30
3. {25, 10, 1}, n = 30

## Applications of Greedy Technique

1. Single source shortest path problem
2. Minimum spanning tree (MST)
3. Huffman codes
4. Simple scheduling problems

## Graph Concepts

- Simple graph
- Multi-graph
- Null graph
- Weighted graph
- Unweighted graph

**Min, Max Number of Edges in Simple Graph?**

### Minimum Spanning Tree

### Algorithm Prim(E, cost, n, t)

```python
Let (k, l) be an edge with min cost in E
min_cost = Cost[k, l]
t[1, 1] = k, t[1, 2] = l

for i = 1 to n
    if (cost[i, l] < cost[i, k]) then near[i] = l
    else near[i] = k

near[k] = near[l] = 0

for i = 2 to n-1
    let j be an index such that near[j] != 0 and cost[j, near[j]] is minimum
    t[i, 1] = j, t[i, 2] = near[j]
    min_cost = min_cost + cost[j, near[j]]
    near[j] = 0

for k = 1 to n do
    if near[k] != 0 and (cost[k, near[k]] > cost[k, j])
        then near[k] = j
```
## Prim's Algorithm (Using Min Heap)

```python
Algorithm Prim(G, cost, r)

for each vertex u ∈ G
{
    u.key = ∞
    u.π = NIL
}

r.key = 0
Q = G.vertices // build min-heap

while(Q != ∅)
{
    u = extract_min(Q)

    for each vertex v adjacent to u
    {
        if v ∈ Q and cost(u, v) < v.key
        {
            v.parent = u
            v.key = w(u, v)
        }
    }
}
```
### Build heap
- **Time complexity:** O(n)

### Extract min
- **Time complexity:** O(vlogv)

### Decrease key
- **Time complexity:** O(Elogv)

#### Time Complexity:

- **Unordered Array:** θ(V^2)
- **Min Heap:** θ(Elogv)

### Which Data Structure is Better Choice for Prim’s Algorithm?

Answer: It depends on the type of graph.

- Dense graph: θ(V^2)
- Sparse graph: θ(Elogv)

---

## Kruskal’s Algorithm
```
1. Sort all edges in increasing order of their edge weights.
2. Pick the smallest edge.
3. Check if the new edge creates a cycle or loop in a spanning tree.
4. If it doesn’t form the cycle, then include that edge in MST. Otherwise, discard it.
5. Repeat from step 2 until it includes |V| - 1 edges in MST.
```
#### Time Complexity:

- Sorting the edges and adding |v|-1 edges to the MST.
- **Time complexity:** θ(ElogE)

---

## Dijkstra’s Algorithm

### Single Source Shortest Path Problem

#### Relaxing an Edge (v,u):
- If d(u) > d(v) + C(v,u)
  - d(u) = d(v) + C(v,u)

```markdown
Algorithm Dijkstra(G,w, S)
{
    Initialize single source(G,S)
    S = ∅
    Q = G.v // build min-heap
    while Q != ∅
    {
        u = extract_min(Q)
        S = S ∪ {u}
        for each vertex v ∈ G.adj[u]
        {
            relax(u,v,w) // decrease key
        }
    }
}
```
**Time complexity:** θ(Elogv)
