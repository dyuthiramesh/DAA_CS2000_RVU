# Bubble Sort

Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. Bubble sort is not an efficient algorithm for large lists and is primarily used for educational purposes due to its simplicity.

## Algorithm

1. Start with the first element (index 0) of the list.
2. Compare it with the next element (index 1). If the first element is greater than the second element, swap them.
3. Move to the next pair of adjacent elements (index 1 and index 2) and repeat step 2.
4. Continue this process, comparing and swapping adjacent elements, until you reach the end of the list.
5. After the first pass, the largest element will be at the end of the list.
6. Repeat steps 1-5 for the remaining unsorted elements, excluding the last one after each pass (as it's already in its correct position).
7. Continue this process until no more swaps are needed, indicating that the list is sorted.

## Time Complexity

- **Best-case time complexity**: O(n)
  - Occurs when the list is already sorted, and no swaps are needed. Each element is compared once.
- **Average-case time complexity**: O(n^2)
  - In the average case, bubble sort makes multiple passes through the list, comparing and swapping elements.
- **Worst-case time complexity**: O(n^2)
  - Occurs when the list is sorted in reverse order, and the algorithm needs to make the maximum number of swaps.

Bubble sort is not suitable for large lists due to its quadratic time complexity.

## Space Complexity

Bubble sort is an in-place sorting algorithm, meaning it does not require additional memory for sorting. It has a space complexity of O(1) as it only uses a constant amount of extra space for temporary variables during swaps.

Bubble sort's simplicity makes it easy to understand but inefficient for sorting large datasets. It is primarily used for educational purposes and not for practical applications.
