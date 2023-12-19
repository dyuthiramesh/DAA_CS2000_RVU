# Transform & Conquer

## Outline

1. **Introduction to Transform & Conquer**
    - Transform & Conquer is a problem-solving paradigm that involves transforming a problem into a more convenient or simpler form before solving it. This often includes changing the problem representation or reducing it to a known problem.

2. **Heap**
    - **Max-heap – Array Representation**
        - A max-heap is a binary tree where the value of each node is greater than or equal to the values of its children. It is represented using an array.
    - **Build Heap**
        - **Max_heapify Algorithm**
        - **Extract_max Operation**
        - **Increase_key Operation**

3. **Transform and Conquer**
    - This group of techniques solves a problem by various transformations:
        - To a simpler/more convenient instance of the same problem (instance simplification)
            - *Example:* Checking if all elements are distinct (element uniqueness)
        - To a different representation of the same instance (representation change)
            - *Example:* Transforming a maximization problem into a minimization problem (Max-heap to Min-heap)
        - To a different problem for which an algorithm is already available (problem reduction)
            - *Example:* Using the relationship lcm(m,n) * GCD(m,n) = m * n

4. **Motivation for Heap Data Structure**
    - Various implementations of heaps:
        - Array Type
        - Unsorted Array
        - Sorted Array
        - Linked List (Unsorted)
        - Min/Max Heap

5. **Heaps and Heapsort**
    - **Definition:** A heap is a binary tree with specific key relationships, either max-heap or min-heap.
        - Illustration of Heap's Definition
    - **Heap’s Array Representation**
        - Store heap’s elements in an array with top-down left-to-right order.
    - **Build Heap Algorithm**
    - **Full Binary Tree Properties & Time Efficiency**
    - **Max-Heapify Algorithm**
    - **Example for Extract_max Operation**
        - *Extract_max*
    - **Heap_increase_key Operation**
    - **Time Complexity**
        - Find_max
        - Extract_max/Delete_max
        - Build_heap
        - Insert
        - Increase_key

6. **Heap Sort**
    - **Algorithm: Heapsort(A)**
    - **Time Complexity**
        - O(nlogn)
    - **Comparison with Merge Sort**
        - Heap sort is efficient in terms of space.
        - In-place sorting algorithm, not stable.
