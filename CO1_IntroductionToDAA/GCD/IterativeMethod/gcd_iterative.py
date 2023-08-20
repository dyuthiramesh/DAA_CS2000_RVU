import time

num1 = 1234512345
num2 = 8765487654

n = min(num1, num2)

hcf = 1
for i in range(1, n):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i

print("HCF =", hcf)

print(time.time())