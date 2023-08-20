import time

num1 = 24
num2 = 56

start = time.time()


def is_prime(n):
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False
    return True


primes = [i for i in range(2, max(num1, num2) + 1) if is_prime(i)]
print(primes)

factors = [1]

m, n = num1, num2
for i in primes:
    while m % i == 0 and n % i == 0:
        factors.append(i)
        m /= i
        n /= i

print(factors)

hcf = 1
for j in factors:
    hcf *= j

end = time.time()

print("HCF of", num1, "and", num2, "=", hcf)

print((end - start) * 1000)