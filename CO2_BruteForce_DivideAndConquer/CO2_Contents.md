# Divide and Conquer Technique

The most well-known algorithm design strategy:

- Divide the instance of the problem into two or more smaller instances.
- Solve smaller instances recursively (typically).
- Obtain the solution to the original (larger) instance by combining these solutions.

It generally leads to a recursive algorithm!

## Divide and Conquer examples

- Sorting: merge sort and quicksort
- Binary tree traversals
- Multiplication of large integers
- Matrix multiplication: Strassen’s algorithm
- Closest-pair and convex-hull algorithms

## Merge Sort

**Pseudocode of Merge sort**

```plaintext
Algorithm MergeSort(A):
    if |A| > 1:
        split A into halves B and C
        MergeSort(B)
        MergeSort(C)
        Merge(B, C, A)
```

### Merge Function

Merge sorted arrays B and C into array A:

```plaintext
Algorithm Merge(B, C, A):
    while B and C are non-empty:
        if head(B) < head(C):
            remove head(B) and append to A
        else:
            remove head(C) and append to A
    append the remaining elements of B and C to A
```

**Merge Sort Example:**

```plaintext
A = [4, 3, 2, 5, 1]
```

**Analysis of Mergesort:**

All cases have the same efficiency:

\[ T(n) = 2T(n/2) + n \text{ ; } n > 1 \]
\[ 1 \text{ ; } n = 1 \]

- Time complexity: \( \Theta(n \log n) \)
- Space requirement: \( \Theta(n) \) (not in-place)

---

## Quicksort

Quicksort is another sorting algorithm based on the divide and conquer approach.

- Select a pivot (partitioning element).
- Rearrange the list so that elements smaller than or equal to the pivot are on one side, and elements larger than or equal to the pivot are on the other.
- Recursively sort the two subarrays.

**Quicksort Algorithm**

```plaintext
Algorithm Quicksort(A, p, r):
    if (p < r):
        q = partition(A, p, r)
        Quicksort(A, p, q-1)
        Quicksort(A, q+1, r)
```

### Partition Algorithm

```plaintext
Algorithm Partition(A, p, r):
    x = A[r]
    i = p-1
    for j = p to r-1:
        if (A[j] <= x):
            i = i+1
            exchange A[i] with A[j]
    exchange A[i+1] with A[r]
    return i+1
```

**Time Complexity:**

- Best case: \( T(n) = 2T(n/2) + n \)
- Worst case: \( T(n) = n + T(n-1) \)
- Average case: \( T(n) = 2n + T(n-1/2) \)

**Space Complexity:**

- Worst case: \( O(n) \)
- Best and average case: \( O(\log n) \)

---

# Strassen’s Matrix Multiplication

## Naive Algorithm

### Matrix Multiplication Pseudo Algorithm

```
Algorithm MatrixMultiplication(A, B, C)

// Assume A, B are square matrices of dimension nxn

// C is the resultant matrix and dimension is nxn

for i = 0 to n-1
    for j = 0 to n-1
        C[i][j] = 0
        for k = 0 to n-1
            C[i][j] = C[i][j] + A[i][k] * B[k][j]
```

#### Example:
```
// A: 4x4, B: 4x4
// C: 4x4

Naive Algorithm

A00 A01 B00 B01 = C00 C01
A10 A11 B10 B11   C10 C11

C00 = A00 * B00 + A01 * B10
C01 = A00 * B01 + A01 * B11

C10 = A10 * B00 + A11 * B10
C11 = A10 * B01 + A11 * B11
```

### Strassen's Matrix Multiplication Algorithm
```
Algorithm StrassenMatrixMultiplication(A, B, C)

if n = 1
    C[0][0] = A[0][0] * B[0][0]
else
    // Subdivide matrices
    Partition A and B into quadrants A11, A12, A21, A22, B11, B12, B21, B22

    // Calculate seven products
    M1 = StrassenMatrixMultiplication(A11 + A22, B11 + B22)
    M2 = StrassenMatrixMultiplication(A21 + A22, B11)
    M3 = StrassenMatrixMultiplication(A11, B12 - B22)
    M4 = StrassenMatrixMultiplication(A22, B21 - B11)
    M5 = StrassenMatrixMultiplication(A11 + A12, B22)
    M6 = StrassenMatrixMultiplication(A21 - A11, B11 + B12)
    M7 = StrassenMatrixMultiplication(A12 - A22, B21 + B22)

    // Calculate four quadrants of the result
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    // Combine results into the result matrix C
    Combine C11, C12, C21, C22 into matrix C

```

### Formulas for Strassen's algorithm:
```
M1 = (A11 + A22) * (B11 + B22)
M2 = (A21 + A22) * B11
M3 = A11 * (B12 - B22)
M4 = A22 * (B21 - B11)
M5 = (A11 + A12) * B22
M6 = (A21 - A11) * (B11 + B12)
M7 = (A12 - A22) * (B21 + B22)
```

### Analysis of Strassen’s Algorithm

If \(n\) is not a power of 2, matrices can be padded with zeros.

### Number of Multiplications

\[T(n) = \begin{cases} 
7 T(n/2) + n^2 & \text{if } n > 2 \\
1 & \text{if } n \leq 2 
\end{cases}\]

### Solution

\[T(n) = 7 \log_2 n = n \log_2 7 \approx n^{2.807} \text{ vs. } n^3 \text{ of brute-force algorithm.}\]

### Open Research Problem

This analysis presents an open research problem!
