

import sys

a, b, k = [int(x) for x in sys.stdin.readline().split()]

if a > k:
    a -= k
else:
    k -= a
    a = 0
    if b > k:
        b -= k
    else:
        b = 0

print(a, b)