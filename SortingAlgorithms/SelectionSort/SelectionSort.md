# Selection Sort

Selection sort is a simple comparison-based sorting algorithm that divides the input list into two parts: the sorted part and the unsorted part. It repeatedly selects the smallest (or largest) element from the unsorted part and moves it to the sorted part. Selection sort is easy to understand but not efficient for large datasets due to its quadratic time complexity.

## Algorithm

1. Start with the first element of the list as the initial "minimum" value.
2. Iterate through the unsorted part of the list to find the minimum element.
3. If a smaller element is found, update the "minimum" value.
4. After completing the iteration, swap the minimum element with the first unsorted element, effectively moving it to the sorted part of the list.
5. Repeat steps 1-4, moving the boundary between the sorted and unsorted parts one element to the right in each iteration.
6. Continue this process until the entire list is sorted.

## Time Complexity

- **Best-case time complexity**: O(n^2)
  - Occurs when the list is already sorted. Selection sort makes the same number of comparisons and swaps regardless of the input order.
- **Average-case time complexity**: O(n^2)
  - In the average case, selection sort still makes a quadratic number of comparisons and swaps.
- **Worst-case time complexity**: O(n^2)
  - Occurs when the list is sorted in reverse order or in the worst possible order. Each element in the unsorted part needs to be compared and swapped in each iteration.

Selection sort is not suitable for large datasets due to its quadratic time complexity. It's mainly used for educational purposes or when simplicity is more important than performance.

## Space Complexity

Selection sort is an in-place sorting algorithm, meaning it sorts the list without using additional memory for data structures like arrays or linked lists. It has a space complexity of O(1) as it only uses a constant amount of extra space for temporary variables during swaps.

While selection sort is not the most efficient sorting algorithm, its simplicity makes it easy to implement and understand. For small datasets or when memory usage is a concern, selection sort may be a reasonable choice.
