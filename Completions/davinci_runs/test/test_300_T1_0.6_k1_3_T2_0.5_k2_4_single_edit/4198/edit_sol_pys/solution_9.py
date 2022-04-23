

import math, sys

a, b, x = map(int, input().split())

if a == 1:
    print(x)
else:
    y = (x-b)/a
    print(int(math.floor(y)))
