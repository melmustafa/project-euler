m_value = [20, 25, 50, 100, 125, 250]

for m in m_value:
    n = (500 // m) - m
    if n < 0:
        continue
    print(n, m)
    a = m ** 2 - n ** 2
    b = 2 * m * n
    c = m ** 2 + n ** 2
    print(a, b, c)
    print(a**2 + b**2 == c**2)
    if a + b + c == 1000:
        print(a*b*c)