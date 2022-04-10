

import sys

[n, a, b] = map(int, sys.stdin.readline().split())

if a == 0:
    print(0)
elif a == b:
    print(n // 2)
else:
    print(n - n // (a + b) * (a + b) // a * a)