def numberofdivisors(n):
    d = 1
    k = 1
    while n % 2 == 0:
        n = n // 2
        k = k + 1
    d = d * k
    m = 3
    for m in range(3, n + 1, 2):
        if n <= 1:
            break
        k = 1
        while n % m == 0:
            n = n // m
            k = k + 1
        d = d * k
        m = m + 2
    return d

for i in range(1, 10**10):
    n = i * (i + 1) // 2
    if numberofdivisors(n) > 500:
        print(n)
        break