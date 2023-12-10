def find_minimum(arr, n, index=0):
    if n == 0:
        return -1, float('inf')
    sub_index, sub_element = find_minimum(arr, n - 1, index + 1)
    if arr[n - 1] < sub_element:
        return index, arr[n - 1]
    else:
        return sub_index, sub_element

size = int(input())
if size == 0:
    print("-1")
else:
    array = list(map(int, input().split()))
    index, element = find_minimum(array, size)
    print(size-index-1)
    print(element)