# Insertion Sort

Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. It works by repeatedly taking an element from the unsorted part of the list and inserting it into its correct position in the sorted part of the list. Insertion sort is efficient for small datasets or nearly sorted datasets and is often used in practice for such cases.

## Algorithm

1. Start with the second element (index 1) of the list.
2. Compare it with the previous element (index 0) to determine if it's greater.
3. If the previous element is greater, swap them.
4. Continue this process, moving backward through the sorted part of the list, until the correct position for the current element is found.
5. Move to the next unsorted element (index i) and repeat steps 2-4.
6. Continue this process until all elements are in their correct sorted positions.

## Time Complexity

- **Best-case time complexity**: O(n)
  - Occurs when the list is nearly sorted, and each element requires minimal comparisons and swaps.
- **Average-case time complexity**: O(n^2)
  - In the average case, insertion sort makes multiple passes through the list, comparing and swapping elements.
- **Worst-case time complexity**: O(n^2)
  - Occurs when the list is sorted in reverse order, and each element needs to be moved to the beginning of the list.

Insertion sort is efficient for small lists, but its quadratic time complexity makes it less suitable for large datasets.

## Space Complexity

Insertion sort is an in-place sorting algorithm, meaning it sorts the list without using additional memory for data structures like arrays or linked lists. It has a space complexity of O(1) as it only uses a constant amount of extra space for temporary variables during swaps.

Insertion sort's simplicity and efficiency for small datasets make it a reasonable choice for sorting when dealing with limited data sizes. However, for large datasets, more efficient sorting algorithms like merge sort or quicksort are preferred.