

import sys
import math

n = int(input())

a = list(map(int, input().split()))

b = []
c = []

for i in range(n):
    if i % 2 == 0:
        b.append(a[i])
    else:
        c.append(a[i])

b.sort()
c.sort()

for i in range(n):
    if i % 2 == 0:
        a[i] = b[i // 2]
    else:
        a[i] = c[i // 2]

print(" ".join(map(str, a)))
