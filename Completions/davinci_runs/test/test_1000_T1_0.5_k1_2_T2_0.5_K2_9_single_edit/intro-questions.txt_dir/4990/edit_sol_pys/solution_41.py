

import sys

b, k, g = map(int, sys.stdin.readline().split())
print(int(b / g) + (1 if b % g > 0 else 0) * k)
