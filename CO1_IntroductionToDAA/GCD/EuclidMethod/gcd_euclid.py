import time

num1 = 24
num2 = 56

start = time.time()

m, n = max(num1, num2), min(num1, num2)

while n != 0:
    r = m % n
    m = n
    n = r

end = time.time()

print("HCF =", m)

print(end - start)