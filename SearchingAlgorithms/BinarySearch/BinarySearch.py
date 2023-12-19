array = [1, 3, 5, 7, 9, 12, 13, 15, 16, 17, 19, 20, 27, 28, 30]

key = 18
isPresent = False

lower, upper = 0, len(array) - 1
mid = (lower + upper) // 2

while upper - lower > 1:
    print(array[mid])
    if array[mid] == key:
        pos = mid
        print(pos)
        isPresent = True
        break
    elif array[mid] > key:
        upper = mid
        mid = (lower + upper) // 2
    else:
        lower = mid
        mid = (lower + upper) // 2

if isPresent:
    print("Index of", key, "in array is", pos)
else:
    print("Element not found")
