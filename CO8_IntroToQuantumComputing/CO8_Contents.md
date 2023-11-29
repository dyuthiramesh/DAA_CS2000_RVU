# Introduction to Quantum Computing
[Material prepared by Q-Pulse: Quantum Computing Club, RV University]

---

# What is Quantum Computing?

Quantum computing is a new way of doing computations by harnessing the principles of quantum mechanics. Unlike classical computers that use bits, which can be either 0 or 1, quantum computers use qubits, which can exist in multiple states simultaneously. This allows quantum computers to explore many possibilities at once, offering the potential to solve certain problems much faster than traditional computers. While still in early stages, quantum computing holds promise for tackling complex problems in fields like cryptography and optimization.

Quantum computing is driven by the distinctive capabilities of qubits, the quantum equivalent of classical bits. Qubits leverage quantum superposition, allowing them to exist in multiple states simultaneously, and entanglement, which creates interconnected relationships among qubits. This unique behavior enables quantum computers to explore many solutions at once, thereby exponentially speeding up the processing.

## But why Quantum Computing?

### Some interesting concepts of Quantum Computing

- **Schrodinger’s Cat:**
  It is a simple thought experiment in physics. Suppose you put a cat into a box with poison and close it. Now the cat can either eat the poison and die or not eat the poison and be alive. But you don’t know the outcome until you have opened the box to observe, right? So until your observation, the cat can both be dead or alive, i.e., it is in a superposition of both being alive and dead.

- **Quantum Superposition:**
  Quantum superposition is the ability of quantum particles to exist in multiple states simultaneously until a measurement is made. Superposition enables quantum computers to perform parallel computations on multiple possibilities simultaneously, potentially providing a significant speedup for certain algorithms.

- **Quantum Tunneling:**
  Quantum tunneling is a phenomenon where particles, like electrons, can pass through barriers that classical physics predicts they shouldn't be able to cross. This happens because of the probabilistic nature of quantum mechanics, allowing particles to exist on both sides of the barrier simultaneously.

- **Quantum Entanglement:**
  Quantum entanglement occurs when two particles become correlated in such a way that the state of one particle becomes directly linked to the state of the other, even when separated by large distances. This connection is established during a quantum interaction, where the quantum states of the particles become entwined, leading to a shared quantum state. Changes to the state of one entangled particle instantaneously affect the state of the other, a phenomenon that challenges classical intuitions about the independence of distant objects in quantum physics.

- **Quantum Teleportation:**
  Quantum teleportation is a process that allows the transfer of quantum information between two distant particles. By entangling two particles and measuring the state of one, the information is instantaneously conveyed to the other, regardless of the physical distance between them. This doesn't involve the actual physical movement of particles.

### Quantum computing's potential impact on problem-solving:

- **Factorization:**
  Quantum computers have shown promise in solving integer factorization problems exponentially faster than classical computers. This has implications for breaking widely-used encryption algorithms, such as RSA, which rely on the difficulty of factoring large numbers.

- **Optimization Problems:**
  Quantum computing is well-suited for solving optimization problems, where the goal is to find the best solution among a large number of possibilities. This can have applications in areas such as logistics, finance, and materials science.

- **Simulation of Quantum Systems:**
  Quantum computers are naturally suited for simulating quantum systems, which is challenging for classical computers. This has applications in understanding molecular and chemical interactions, leading to advancements in drug discovery, materials science, and other fields.

## Why Quantum Computing is better than Classical Computing?

- **Machine Learning:**
  Quantum computing has the potential to enhance machine learning algorithms, particularly in areas like linear algebra and optimization. Quantum machine learning may offer advantages in training complex models and processing large datasets.

- **Cryptography:**
  While quantum computing poses a threat to classical cryptographic methods, it also opens the door to new cryptographic techniques based on quantum principles. Quantum key distribution is an example where quantum mechanics is used to secure communication channels.

### QUANTUM ADVANTAGES IN THINGS YOU HAVE ALREADY LEARNED

- **In Dynamic Programming:**
  Algorithms like the Bellman-Ford algorithm are commonly used to solve the Shortest Path problem. Quantum computing could potentially provide a speedup for certain instances of the Shortest Path problem by leveraging quantum parallelism. One quantum algorithm that shows promise for solving optimization problems, including certain instances of the Shortest Path problem, is the Quantum Approximate Optimization Algorithm (QAOA).

- **In Graphs (Prim's and Kruskal's Algorithms):**
  Quantum computing has the potential to offer advantages over classical computing for certain types of problems, and the Minimum Spanning Tree (MST) problem is no exception. Classical algorithms for finding the Minimum Spanning Tree include Prim's algorithm and Kruskal's algorithm.

### IN MINIMUM SPANNING TREE (MST)

- **Parallel Exploration:**
  Quantum computers can explore multiple possibilities simultaneously due to the principles of superposition. Q-MST could potentially explore different spanning tree configurations at the same time, allowing for a more efficient search for the optimal solution.

- **Quantum Advantage:**
  Quantum computing could potentially provide advantages for the MST problem through algorithms that leverage quantum parallelism. One such algorithm is the Quantum Minimum Spanning Tree (Q-MST) algorithm, which is designed to find the MST using quantum principles.

### Searching Using Quantum Computing

One of the most famous quantum algorithms that demonstrates the power of quantum computing in searching is Grover's algorithm. Grover's algorithm provides a quadratic speedup over classical algorithms for unstructured search problems. In a classical search, you would need to check N/2 items on average to find the desired one in an unsorted database of N items. Grover's algorithm, on the other hand, can achieve the same task using approximately √N steps, significantly reducing the time complexity. The basic idea behind Grover's algorithm is to use quantum superposition and interference to amplify the probability amplitude of the correct solution while suppressing the amplitudes of incorrect solutions. This allows the algorithm to converge more quickly to the correct solution.

### Deterministic Algorithms

Deterministic algorithms are a class of algorithms that produce the same output for a given set of inputs every time they are run. In other words, their behavior is entirely predictable and consistent.

1. **Binary Search Algorithm:**
   Given a sorted list, the binary search algorithm locates a specific value by repeatedly dividing the search interval in half.

2. **Merge Sort Algorithm:**
   A sorting algorithm that divides the input list into smaller sub-lists, sorts these sub-lists, and then merges them to produce a sorted output.

3. **Dijkstra's Algorithm:**
   Used to find the shortest path from a starting node to all other nodes in a weighted graph.

4. **Euclidean Algorithm:**
   A method for finding the greatest common divisor of two numbers by repeatedly applying the property that the greatest common divisor of two numbers does not change if the smaller number is subtracted from the larger number.

### Non-Deterministic Algorithms

Non-deterministic algorithms differ from deterministic algorithms in that they incorporate randomness or make choices that are not fully predictable. These algorithms might exhibit different behaviors or outcomes when executed multiple times, even with the same input and under the same conditions.

1. **Monte Carlo Algorithm:**
   This type of algorithm uses random sampling or random number generation to find approximate solutions for problems where finding an exact solution is difficult or infeasible.

2. **Las Vegas Algorithm:**
   These algorithms use randomization to find an optimal solution. They have a probabilistic guarantee of correctness, meaning they always provide the correct answer if the algorithm terminates.

### QUANTUM COMPUTING FOR NP HARD PROBLEMS

Quantum computing offers potential advantages in dealing with NP-hard problems due to its ability to handle certain types of computational challenges more efficiently than classical computers. Here's an overview of how quantum computing might impact NP-hard problems and the implications for the (P = NP) problem:

1. **Quantum Superposition and Parallelism:**
   Quantum computers use quantum bits (qubits) that can exist in multiple states simultaneously due to superposition. This enables quantum computers to process various possibilities concurrently. For some problems, this parallelism can be leveraged to explore multiple solutions simultaneously, potentially speeding up the search for solutions.

2. **Quantum Entanglement:**
   Entanglement in quantum computing allows qubits to be correlated and influence each other's states instantaneously over long distances. This property might allow quantum computers to solve certain problems that involve interconnected variables more efficiently than classical computers.

3. **Quantum Algorithms:**
   Quantum algorithms, such as Shor's algorithm, Grover's algorithm, and others, have demonstrated potential efficiency in solving specific problems that are considered hard for classical computers. For instance, Shor's algorithm can factor large integers exponentially faster than the best-known classical algorithms, posing a potential threat to RSA encryption.

### CAN P=NP BE SOLVED?

**P = NP and Quantum Computing:**
The question of whether (P = NP) is unresolved, and quantum computing's impact on solving (P = NP) is uncertain. If it were proven that (P = NP), quantum computers would solve NP problems in polynomial time, rendering NP problems as easy to solve as verifying the solution. However, quantum computing alone might not directly resolve the (P = NP) question. While quantum algorithms can solve specific problems efficiently, proving (P = NP) requires a different approach — a rigorous mathematical proof showing that every problem for which a solution can be quickly verified can also be solved quickly. Even if quantum computing offers solutions to certain NP problems, it doesn't necessarily prove or disprove (P = NP).

In conclusion, while quantum computing shows promise in solving certain NP-hard problems more efficiently than classical computers, its implications for the resolution of the (P = NP) question are uncertain, and the direct impact on the P vs. NP problem remains an open and challenging area of research in computational complexity theory.
