import math

import sys

f = sys.stdin

x, y = map(int, f.readline().split(" "))

if y == 1:
    print("0")
elif x == 0:
    print("IMPOSSIBLE")
else:
    print(math.ceil(x / (y-1)))
