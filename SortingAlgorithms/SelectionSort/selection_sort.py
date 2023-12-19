n = int(input())

if n <= 0:
    print("-1")
    exit()

l = list(map(int, input().split()))

if n == 1:
    print(l[0])
    exit()

comparisons, swappings = 0, 0

for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        comparisons += 1
        if l[j] < l[min_index]:
            min_index = j
    if l[i] != l[min_index]:
        swappings += 1
        l[i], l[min_index] = l[min_index], l[i]

print(swappings)
print(comparisons)
for element in l:
    print(element, end=" ")