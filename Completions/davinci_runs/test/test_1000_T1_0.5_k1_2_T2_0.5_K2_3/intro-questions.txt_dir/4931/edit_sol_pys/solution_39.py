

import sys
import math

x, y = map(int, sys.stdin.readline().split())

print("IMPOSSIBLE" if y == 1 and x != 0 else x / (y - 1) if y != 1 else "INFINITE")
