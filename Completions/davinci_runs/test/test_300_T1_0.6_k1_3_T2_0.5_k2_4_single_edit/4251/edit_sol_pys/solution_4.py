

import math
n, m = [int(x) for x in input().split()]

d = [0]*n
d[0] = float('inf')

for i in range(1, n):
    d[i] = int(input())

d.sort()

def is_valid(k, d):
    pos = 0
    for i in range(m):
        if pos >= n:
            return False
        while pos < n and d[pos] - d[0] < k:
            pos += 1
        if pos >= n:
            return False
        d[0] = d[pos]
        pos += 1
        d.sort()
    return True

l, r = 0, 10**9

while l < r:
    m = (l + r)//2
    if is_valid(m, d):
        r = m
    else:
        l = m + 1

print(r)
