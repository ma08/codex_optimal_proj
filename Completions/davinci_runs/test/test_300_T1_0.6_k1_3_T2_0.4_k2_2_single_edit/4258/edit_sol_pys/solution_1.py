import sys

import math

a, b, t = map(int, sys.stdin.readline().split())

ans = math.floor(t / a) * b
print(int(ans))
