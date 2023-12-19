size = int(input())
    
if size <= 0:
    print(-1)
    exit()

array = list(map(int, input().split()))

swappings =  0

def heapify(arr, n, i):
    global swappings
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        swappings += 1
        heapify(arr, n, largest)

def heap_sort(arr):
    global swappings
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        swappings += 1
        heapify(arr, i, 0)

heap_sort(array)

print(swappings)
print(*array)