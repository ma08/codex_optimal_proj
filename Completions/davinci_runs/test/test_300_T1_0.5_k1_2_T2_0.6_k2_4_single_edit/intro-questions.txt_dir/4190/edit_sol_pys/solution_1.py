

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    a[i] += a[i-1]
    b[i] += b[i-1]

c = 0
for i in range(n-1):
    if a[i] == b[i]:
        c += 1

print(c)
