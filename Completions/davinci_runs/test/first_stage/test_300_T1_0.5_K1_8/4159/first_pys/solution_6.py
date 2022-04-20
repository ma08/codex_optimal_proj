

import sys

a, b, k = map(int, sys.stdin.readline().split())

if k < a:
    print(a - k, b)
elif a <= k <= a + b:
    print(0, b - (k - a))
else:
    print(0, 0)