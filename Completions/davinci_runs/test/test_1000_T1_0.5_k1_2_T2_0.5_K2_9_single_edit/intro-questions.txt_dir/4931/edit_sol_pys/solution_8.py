

import sys
import math

x, y = map(int, sys.stdin.readline().split())

if y == 1:
    if x != 0:
        print("IMPOSSIBLE")
    else:
        print("ALL GOOD")
else:
    print(x / (y - 1))
