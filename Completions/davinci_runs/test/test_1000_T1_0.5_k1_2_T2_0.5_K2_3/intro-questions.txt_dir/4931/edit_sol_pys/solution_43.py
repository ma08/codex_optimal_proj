

import sys
import math

f = open("1.in", "r")
#f = sys.stdin

x, y = map(int, f.readline().split(" "))

#x = 32
#y = 2

if y == 1:
    print("All Good")
elif x == 0:
    print("Impossible")
else:
    print(math.ceil(x / (y - 1)))
