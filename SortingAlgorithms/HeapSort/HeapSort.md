# Heap Sort

Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to build a partially sorted binary tree, and then efficiently sorts the elements in the tree. It has a guaranteed time complexity of O(n log n), making it suitable for large datasets.

## Algorithm

1. **Build Heap:** Build a max-heap from the array.
2. **Heapify:** Repeatedly remove the maximum element from the heap and reconstruct the heap until all elements are sorted.
3. **Sort:** Place the maximum element at the end of the array and reduce the heap size, repeating until the entire array is sorted.

## Time Complexity

- **Best-case time complexity:** O(n log n)
- **Average-case time complexity:** O(n log n)
- **Worst-case time complexity:** O(n log n)

Heap sort provides a consistent O(n log n) time complexity in all cases, making it a reliable choice for sorting large datasets.

## Space Complexity

Heap sort is an in-place sorting algorithm, meaning it doesn't require additional memory proportional to the input size. Its space complexity is O(1), making it memory-efficient.

Heap sort's guaranteed time complexity and in-place nature make it suitable for scenarios where both time and space efficiency are crucial.
