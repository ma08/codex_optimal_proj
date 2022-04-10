

import math

n = int(input())

x = int(math.sqrt(n))

if x ** 2 == n:
    print(x * 2 - 1)
elif x ** 2 + x >= n:
    print(x * 2)
else:
    print(x * 2 + 1)