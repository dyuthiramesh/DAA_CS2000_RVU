# Linear Search

Linear search, also known as sequential search, is a simple searching algorithm that checks each element of a list one by one until a match is found or the entire list has been examined. It is suitable for unsorted lists and is straightforward to implement but may not be the most efficient for large datasets.

## Algorithm

1. Start from the beginning (the first element) of the list.
2. Compare the current element with the target value.
3. If the current element matches the target, return its index (position) in the list.
4. If no match is found, move to the next element in the list and repeat steps 2-3.
5. Continue this process until the target is found or the end of the list is reached.
6. If the target is not found after examining all elements, return a signal (e.g., -1) indicating that the target is not in the list.

## Time Complexity

- **Best-case time complexity**: O(1)
  - Occurs when the target is found at the very beginning of the list. In this case, only one comparison is needed.
- **Average-case time complexity**: O(n)
  - In the average case, linear search examines about half of the list on average. This results in n/2 comparisons on average, where n is the number of elements in the list.
- **Worst-case time complexity**: O(n)
  - Occurs when the target is either at the end of the list or not in the list at all. In the worst case, linear search needs to compare the target with all n elements of the list.

Linear search is not the most efficient searching algorithm, especially for large datasets. Its performance is directly proportional to the size of the input.

## Space Complexity

Linear search is an in-place search algorithm, meaning it doesn't require extra memory allocation based on the input size. It has a space complexity of O(1) as it only uses a constant amount of extra space for variables such as the index and the target value.

Linear search is most useful when you have a small list or when the list is not sorted. It's a simple and easy-to-understand algorithm, making it suitable for educational purposes and cases where efficiency is not a primary concern.
