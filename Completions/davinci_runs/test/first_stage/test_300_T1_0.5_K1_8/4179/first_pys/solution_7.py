

import sys

n, m, c = map(int, sys.stdin.readline().split())
b = list(map(int, sys.stdin.readline().split()))

count = 0
for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    sum = c
    for j in range(m):
        sum += a[j] * b[j]
    if sum > 0:
        count += 1
print(count)