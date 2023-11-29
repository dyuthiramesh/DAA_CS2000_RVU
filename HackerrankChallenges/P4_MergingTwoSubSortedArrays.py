size_1 = int(input())
list_1 = list(map(int, input().split()))

if size_1 <= 0 and (len(list_1) == 1 and list_1[0] == 0):
    print(-1)
    exit()

elif size_1 <= 0 and (len(list_1) == 1 and list_1[0] != 0):
    size_2 = list_1[0]
    list_2 = list(map(int, input().split()))
    print(0)
    for i in list_2:
        print(i, end=" ")
    exit()

size_2 = int(input())
if size_1 > 0 and size_2 <= 0:
    print(0)
    for i in list_1:
        print(i, end=" ")
    exit()

list_2 = list(map(int, input().split()))

m_list = []

comparisons, m, n = 0, 0, 0

while (m != len(list_1) and n != len(list_2)):
    comparisons += 1
    if list_1[m] < list_2[n]:
        m_list.append(list_1[m])
        m += 1
    else:
        m_list.append(list_2[n])
        n += 1

if m < len(list_1):
    for k in range(m, len(list_1)):
        m_list.append(list_1[k])

elif n < len(list_2):
    for k in range(n, len(list_2)):
        m_list.append(list_2[k])

print(comparisons)
for i in m_list:
    print(i, end=" ")