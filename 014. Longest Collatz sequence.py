def Collatz(n):
    list = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        list.append(n)
    return len(list)
length = [0]
for i in range(1, 1000000):
    length.append(Collatz(i))

m = max(length)
print(length.index(m))