n = int(input())

if n == 0:
    print("-1")
    exit()
    
a = list(map(int, input().split()))

max_val = max(a)

if n % 2 != 0:
    w = 0
    k = 1
    for i in range(0, n, 2):
        if a[i] != a[k]:
            w += 1
            print(w + 1)
            if a[k] != max_val:
                print(k + 1)
            else:
                print(i + 1)
            break
        k += 1
else:
    for i in range(n):
        if a[i] != max_val:
            if n % 2 == 0:
                print((n // 2) + 1)
            else:
                print(n // 2)
            print(i + 1)