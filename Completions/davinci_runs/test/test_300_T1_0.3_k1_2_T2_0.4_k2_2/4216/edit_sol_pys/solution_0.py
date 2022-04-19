

import math

n = int(input())

sqrt_n = int(math.sqrt(n))

for i in range(sqrt_n, 0, -1):
    if n % i == 0:
        break

a = len(str(i))
b = len(str(n // i))

print(max(a, b))
