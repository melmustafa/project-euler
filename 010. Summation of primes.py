import math
import time

start = time.time()

list = [i for i in range(2, 2000000)]

for i in range(len(list)):
    if list[i] > math.sqrt(2000000):
        break
    if list[i] == 0:
        continue
    n = list[i]
    for k in range(1, (1999999//n)):
        list[i + k * n] = 0
print(sum(list))

end = time.time()
print(end - start)