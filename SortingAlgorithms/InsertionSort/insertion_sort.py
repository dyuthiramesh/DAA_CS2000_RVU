n = int(input())

if n <= 0:
    print("-1")
    exit()

l = list(map(int, input().split()))

if n == 1:
    print("0")
    print("0")
    print(l[0])
    exit()

comparisons, movements = 0, 0

for i in range(1, n):
    temp = l[i]
    j = i - 1
    while j >= 0:
        comparisons += 1
        if l[j] > temp:
            l[j + 1] = l[j]
            movements += 1
            j -= 1
        else:
            break
    l[j + 1] = temp

print(comparisons)
print(movements)
for element in l:
    print(element, end=" ")