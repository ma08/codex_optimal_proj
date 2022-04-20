

import sys

a, b, x = map(int, sys.stdin.readline().split())

if x < a + b:
    print(0)
    exit()

l, r = 1, 10**9
while l < r:
    m = (l + r + 1) // 2
    if a * m + b * len(str(m)) > x:
        r = m - 1
    else:
        l = m

print(l)