array = [2, 5, 3, 7, 9, 3, 1, 4, 8, 9, 0, 5]
key = 0
isPresent = False

for i in range(len(array)):
    if array[i] == key:
        index = i
        isPresent = True
        break

if isPresent:
    print("Index of", key, "in array is", index)
else:
    print("Element not found")