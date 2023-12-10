def recursion_fibonacci_series(n):
    global temp
    if n<=1:
        return 1
    else:
        result = recursion_fibonacci_series(n-1)+recursion_fibonacci_series(n-2)
        if result>=temp:
            temp = result
            print(result, end=" ")
        return result

n = int(input())
n1,n2 = 0,1

temp = 2

if n<=0:
    print(n1, n2)
elif n == 1:
    print(n1, n2, end=" ")
    print(1, end=" ")    
else:
    print(n1, n2, end=" ")
    print(1, end=" ")
    recursion_fibonacci_series(n)