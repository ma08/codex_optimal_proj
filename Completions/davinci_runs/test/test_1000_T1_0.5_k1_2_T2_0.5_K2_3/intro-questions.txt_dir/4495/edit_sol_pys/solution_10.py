
import math, sys

a, b, x = map(int, sys.stdin.readline().split())

if a % x == 0:
    print(int(math.floor(b/x) - math.floor(a/x) + 1))
else:
    print(int(math.floor(b/x) - math.floor(a/x)))
