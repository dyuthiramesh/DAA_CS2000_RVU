# Binary Search

Binary search is an efficient searching algorithm that works on sorted lists. It repeatedly divides the search interval in half until the target is found or the interval becomes empty. This algorithm is significantly faster than linear search for large datasets, making it suitable for sorted lists.

## Algorithm

1. Start with the entire sorted list.
2. Compare the target value with the middle element of the list.
3. If the target matches the middle element, return its index.
4. If the target is less than the middle element, repeat the search on the left half of the list.
5. If the target is greater than the middle element, repeat the search on the right half of the list.
6. Continue this process until the target is found or the search interval becomes empty.

## Time Complexity

- **Best-case time complexity:** O(1)
  - Occurs when the target is found at the middle of the list in the first comparison.
- **Average-case time complexity:** O(log n)
  - In the average case, binary search repeatedly divides the search interval in half, resulting in a logarithmic time complexity.
- **Worst-case time complexity:** O(log n)
  - Even in the worst case, binary search efficiently reduces the search interval, resulting in a logarithmic time complexity.

Binary search is highly efficient for large datasets due to its logarithmic time complexity.

## Space Complexity

Binary search is implemented using a recursive or iterative approach. Both approaches have a space complexity of O(log n) due to the call stack or iterative variables. The space required is proportional to the logarithm of the size of the input.

Binary search is a powerful algorithm for searching sorted datasets, providing faster results compared to linear search, especially for large lists.
