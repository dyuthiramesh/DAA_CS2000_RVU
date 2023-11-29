# Transform & Conquer

## Outline

1. **Introduction to Transform & Conquer**
    - Motivation for heap

2. **Heap**
    - Max-heap – array representation
    - Build heap
        - Max_heapify
        - Extract_max
        - Increase_key

3. **Transform and Conquer**
    - This group of techniques solves a problem by a transformation:
        - to a simpler/more convenient instance of the same problem (instance simplification)
            - Eg: checking if all elements are distinct (element uniqueness)
        - to a different representation of the same instance (representation change)
            - Eg: transforming a maximization problem into a minimization problem and solving it. Max-heap to min-heap.
        - to a different problem for which an algorithm is already available (problem reduction)
            - Eg: We know that, lcm(m,n) * GCD(m,n) = m*n

4. **Motivation for Heap Data Structure**
    - Array type
        - Insert at end
        - Search
        - Find_min
        - Delete_min
    - Unsorted array
    - Sorted array
    - Linked list (unsorted)
    - Min/max Heap

5. **Heaps and Heapsort**
    - **Definition:** A heap is a binary tree (3-ary, n-ary) with keys at its nodes (one key per node) such that:
        - It is essentially complete
        - The key at each node is ≥ keys at its children (max-heap)
        - Illustration of the heap’s definition
            - Note: In Max-heap, the key of every parent is greater than its children. In Min-heap, the key of every parent is lesser than its children.
    - **Heap’s Array Representation**
        - Store heap’s elements in an array (whose elements indexed, for convenience, 1 to n) in top-down left-to-right order
            - Example:
            ```
            1 2 3 4 5 6
            9 5 3 1 4 2
            ```
    - **Build heap algorithm**
    - **Full Binary Tree Properties & Time Efficiency**
    - **Max-heapify algorithm**
    - **Example for extract_max**
        - Extract_max
    - **Heap_increase_key**
    - **Time Complexity**
        - Find_max
        - Extract_max/Delete_max
        - Build_heap
        - Insert
        - Increase_key

6. **Heap Sort**
    - **Algorithm Heapsort(A)**
    - **Time Complexity**
        - Time complexity: O(nlogn)
        - Compared to merge sort, heap sort is efficient in terms of space.
        - Heap sort: In-place sorting algorithm, not stable