

import sys
import math

f = open("1.in", "r")
#f = sys.stdin

x, y = map(int, f.readline().split(" "))

x = 32
y = 2

if y == 1:
    print("ALL GOOD")
elif x == 0:
    print("IMPOSSIBLE")
else:
    print(x / (y - 1))
