import math

primes = [2]
i = 3
while(len(primes) < 10001 ):
    j = 0
    found = True
    while(primes[j] <= math.sqrt(i)):
        if i % primes[j] == 0:
            found = False
            break
        j = j + 1
    if found:
        primes.append(i)
    i = i + 2

print(primes[10000])

def isPrime(k):
    if (k <= 1):
        return 0
    if (k == 2 or k == 3):
        return 1
    if (k % 2 == 0 or k % 3 == 0):
        return 0
    for i in range(5, 1 + int(k ** 0.5), 6):
        if (k % i == 0 or k % (i + 2) == 0):
            return 0
    return 1

def nthPrime(n):
    if n == 1:
        return 2
    n = n - 1
    i = 3
    while(n > 0):
        if isPrime(i):
            n = n - 1
        i = i + 2
    return i - 2

print(nthPrime(10001))