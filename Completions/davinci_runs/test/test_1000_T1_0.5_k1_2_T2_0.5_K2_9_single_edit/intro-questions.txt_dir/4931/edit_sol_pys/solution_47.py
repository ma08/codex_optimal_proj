

import sys
import math

f = open("1.in", "r")
#f = sys.stdin

x, y = map(int, f.readline().split(" "))

if y == 1:
    print("ALL GOOD", end="")
elif x == 0:
    print("IMPOSSIBLE", end="")
else:
    print(math.ceil(x / (y - 1)), end="")
