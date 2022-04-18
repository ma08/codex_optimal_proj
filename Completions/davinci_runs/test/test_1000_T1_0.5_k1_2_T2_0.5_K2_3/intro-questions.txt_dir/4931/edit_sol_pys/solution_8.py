

import sys
import math

x, y = map(int, sys.stdin.readline().split())

print("IMPOSSIBLE" if y == 1 and x != 0 else y - 1 / x)
