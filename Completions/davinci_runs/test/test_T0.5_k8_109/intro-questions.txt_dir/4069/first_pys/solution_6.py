

import sys

x, k, d = map(int, sys.stdin.readline().split())

if abs(x) >= k * d:
    print(abs(x) - k * d)
else:
    if ((k - abs(x) // d) % 2 == 0):
        print(abs(x) % d)
    else:
        print(d - abs(x) % d)