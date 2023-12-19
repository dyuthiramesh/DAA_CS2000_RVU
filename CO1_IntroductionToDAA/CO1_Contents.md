# Algorithm Basics

## What is an Algorithm?

An algorithm is a sequence of unambiguous instructions for solving a problem. It aims to obtain the required output for any legitimate input in a finite amount of time.

## Representing Algorithms

Algorithms can be represented in various forms, including unambiguity, clarity, and finiteness. There can be several algorithms to solve a single problem.

## Historical Perspective

- **Muhammad ibn Musa al-Khwarizmi** – A 9th-century mathematician.

- **Euclid’s Algorithm** – Used to find the Greatest Common Divisor (GCD) of two numbers.

## Euclid's Algorithm

**Description 1:**
- Input: Two non-negative integers `m` and `n`.

- Output: GCD of `m` and `n`.


Step 1: If n = 0, return m and stop; otherwise, go to Step 2

Step 2: Divide m by n and assign the value of the remainder to r

Step 3: Assign the value of n to m and the value of r to n. Go to Step 1.


**Algorithm Euclid(m,n):**

Input: Two nonnegative, not-both-zero integers m and n

Output: Greatest common divisor of m and n
```
while n ≠ 0 do
  r ← m mod n
  m ← n
  n ← r
return m
```

## Consecutive Integer Checking Algorithm

**Algorithm:**

Step 1: Assign the value of min{m, n} to t.

Step 2: Divide m by t. If the remainder is 0, go to Step 3; otherwise, go to Step 4.

Step 3: Divide n by t. If the remainder is 0, return t as the answer and stop; otherwise, proceed to Step 4.

Step 4: Decrease the value of t by 1. Go to Step 2.


## Problem-Solving Strategies

- Understanding the problem description
- Asking questions and raising concerns
- Solving cases manually
- Choosing between exact or approximate problem solving

## Algorithm Design Techniques

- Brute force
- Divide and conquer
- Decrease and conquer
- Transform and conquer
- Greedy approach
- Dynamic programming
- Space and time tradeoffs
- Iterative improvement
- Backtracking
- Branch and bound

## Analysis of Algorithms

- Evaluating time and space efficiency
- Identifying more efficient algorithms
- Lower bounds and optimality

## Important Problem Types

- Sorting
- Searching
- String processing
- Graph problems
- Combinatorial problems
- Geometric problems
- Numerical problems

## Sorting Algorithms

Examples of sorting algorithms:
- Selection sort
- Bubble sort
- Insertion sort
- Merge sort
- Heap sort

## Searching Algorithms

- Sequential search
- Binary search

## String Processing

- Text strings: letters, numbers, and special characters
- String matching: searching for a given pattern in a text

## Graph Problems

- Modeling real-life problems using graphs
- Graph traversal algorithms
- Shortest-path algorithms

## Fundamental Data Structures

- List
- Array
- Linked list
- Stack
- Queue
- Priority queue/heap
- Graph
- Tree and binary tree
- Set and dictionary

## Linear Data Structures

### Arrays

- Contiguous memory storage
- Direct access using index
- Useful for storing sequences of items

### Linked List

- Nodes with data and pointers
- Singly linked list (next pointer)
- Doubly linked list (next + previous pointers)

## Stacks and Queues

**Stacks:**
- LIFO (Last In, First Out) order
- Operations: push and pop

**Queues:**
- FIFO (First In, First Out) order
- Operations: enqueue and dequeue

## Priority Queue and Heap

- Priority queues implemented using heaps
- Associated with keys/priorities
- Operations: finding the highest priority, deleting highest priority, inserting new element