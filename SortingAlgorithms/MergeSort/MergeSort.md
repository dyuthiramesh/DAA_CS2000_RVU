 # Merge Sort

Merge sort is a divide-and-conquer algorithm that works by dividing the input array into two halves, recursively sorting each half, and then merging the sorted halves to produce a single sorted array. It is an efficient and stable sorting algorithm with a guaranteed time complexity of O(n log n).

## Algorithm

1. **Divide:** Split the unsorted list into two halves.
2. **Conquer:** Recursively sort each half.
3. **Combine:** Merge the sorted halves to produce a single sorted array.

## Time Complexity

- **Best-case time complexity:** O(n log n)
  - Occurs when the input array is already sorted.
- **Average-case time complexity:** O(n log n)
- **Worst-case time complexity:** O(n log n)
  - Merge sort consistently performs well and is not sensitive to the initial order of elements.

Merge sort divides the input array into two halves, recursively sorts them, and then merges the sorted halves. This divide-and-conquer approach results in a time complexity that is a significant improvement over quadratic algorithms like insertion sort for large datasets.

## Space Complexity

Merge sort has a space complexity of O(n) because it requires additional space to store the two halves of the array during the merge step. The extra space is proportional to the size of the input.

Merge sort's efficient use of time and stable sorting make it a preferred choice for situations where the stability of the algorithm is crucial, and the dataset is large enough to benefit from its O(n log n) time complexity.
