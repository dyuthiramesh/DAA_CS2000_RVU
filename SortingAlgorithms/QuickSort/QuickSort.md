# Quick Sort

Quick sort is a widely used and efficient sorting algorithm that uses a divide-and-conquer strategy to sort an array or list. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

## Algorithm

1. **Select Pivot:** Choose an element from the array to serve as the pivot.
2. **Partitioning:** Rearrange the array elements such that elements smaller than the pivot are on the left, and elements greater than the pivot are on the right.
3. **Recursion:** Recursively apply the same process to the sub-arrays on the left and right of the pivot.
4. **Combine:** No additional combining step is needed in the quick sort algorithm.

## Time Complexity

- **Best-case time complexity:** O(n log n)
- **Average-case time complexity:** O(n log n)
- **Worst-case time complexity:** O(n^2)
  - Occurs when the pivot selection consistently results in unbalanced partitions.

Quick sort's average-case time complexity is generally better than other sorting algorithms, and it is often faster in practice due to its good cache performance and in-place nature.

## Space Complexity

Quick sort has a space complexity of O(log n) due to its recursive nature. However, it is an in-place sorting algorithm, meaning that it doesn't require additional memory proportional to the input size.

Quick sort is widely used for its efficiency and is often the sorting algorithm of choice for large datasets or when average-case performance is crucial.
