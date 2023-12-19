size = int(input())

if size <= 0:
    print(-1)
    exit()

array = list(map(int, input().split()))

comparisons = 0

def merge(B, C, A):
    global comparisons
    m, n, k = 0, 0, 0
    while m < len(B) and n < len(C):
        comparisons += 1
        if B[m] < C[n]:
            A[k] = B[m]
            m += 1
        else:
            A[k] = C[n]
            n += 1
        k += 1

    while m < len(B):
        A[k] = B[m]
        m += 1
        k += 1

    while n < len(C):
        A[k] = C[n]
        n += 1
        k += 1

def mergesort(A):
    if len(A) > 1:
        mid = len(A) // 2
        B = A[:mid]
        C = A[mid:]
        mergesort(B)
        mergesort(C)
        merge(B, C, A)

sorted_array = array.copy()
mergesort(sorted_array)
print(comparisons)
print(*sorted_array)
