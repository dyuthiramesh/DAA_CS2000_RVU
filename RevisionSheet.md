| Algorithm                  | Objective                                | Time Complexity                           | Space Complexity                        |
|-----------------------------|------------------------------------------|-------------------------------------------|-----------------------------------------|
| Euclid's GCD algorithm      | Find the greatest common divisor         | O(log(min(a, b)))                        | O(1)                                    |
| Linear/Sequential Search    | Find an element in a list                | Best: O(1), Average: O(n), Worst: O(n)   | O(1)                                    |
| Binary Search               | Find an element in a sorted list         | Best: O(1), Average: O(log n), Worst: O(log n) | O(1)                                  |
| Selection Sort             | Sort a list                              | Best: O(n<sup>2</sup>), Average: O(n<sup>2</sup>), Worst: O(n<sup>2</sup>) | O(1)                                  |
| Bubble Sort                | Sort a list                              | Best: O(n), Average: O(n<sup>2</sup>), Worst: O(n<sup>2</sup>) | O(1)                                   |
| Merge Sort                 | Sort a list                              | Best: O(n log n), Average: O(n log n), Worst: O(n log n) | O(n)                                  |
| Quick Sort                 | Sort a list                              | Best: O(n log n), Average: O(n log n), Worst: O(n<sup>2</sup>) | O(log n)                               |
| Strassen’s Matrix Multiplication | Multiply two matrices               | O(n<sup>log<sub>2</sub>(7)</sup>)                             | O(n<sup>2</sup>)                                  |
| Insertion Sort             | Sort a list                              | Best: O(n), Average: O(n<sup>2</sup>), Worst: O(n<sup>2</sup>) | O(1)                                   |
| Depth First Search          | Traverse a graph in depth-first manner  | O(V + E)                                | O(V)                                    |
| Breadth First Search        | Traverse a graph in breadth-first manner | O(V + E)                                | O(V)                                    |
| Topological Sorting         | Order the vertices in a directed acyclic graph | O(V + E)                            | O(V)                                    |
| Prim's algorithm            | Find the Minimum Spanning Tree (MST)     | O((V + E) log V)                        | O(V + E)                                |
| Kruskal's algorithm         | Find the Minimum Spanning Tree (MST)     | O(E log V)                              | O(V + E)                                |
| Dijkstra's algorithm        | Find the Single Source Shortest Paths   | Best: O((V + E) log V), Worst: O((V + E) log V) | O(V + E)                               |
| Floyd-Warshall's algorithm   | Find All Pairs Shortest Paths           | O(V<sup>3</sup>)                                  | O(V<sup>2</sup>)                                  |
| Heap Sort                  | Sort a list using a heap                | Best: O(n log n), Average: O(n log n), Worst: O(n log n) | O(1)                                   |
| Travelling Salesperson Problem | Find the shortest possible route that visits each city exactly once and returns to the original city | NP-hard, no known polynomial-time solution | O(n!) (brute force) or O(n<sup>2</sup> * 2<sup>n</sup>) (dynamic programming) |
| The Knapsack Problem        | Optimize the selection of items with maximum total value without exceeding a given weight | NP-hard, various approaches             | O(n * W)                                |
