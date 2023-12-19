size = int(input())

if size <= 0:
    print(-1)
    exit()

array = list(map(int, input().split()))

comparisons, swappings = 0, 0

def partition(A, p, r):
    global comparisons
    global swappings
    x = A[r]
    i = p - 1
    for j in range(p, r):
        comparisons += 1
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            if i != j:
                swappings += 1
    A[i + 1], A[r] = A[r], A[i + 1]
    if i != j:
        swappings += 1
    return i + 1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

sorted_array = array.copy()
quicksort(sorted_array, 0, len(sorted_array) - 1)
print(comparisons)
print(swappings)
print(*sorted_array)