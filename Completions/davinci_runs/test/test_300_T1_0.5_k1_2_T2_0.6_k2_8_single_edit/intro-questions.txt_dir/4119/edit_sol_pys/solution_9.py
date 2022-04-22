

import heapq
import sys

n = int(input())
a = list(map(int,input().split()))

a.sort()

l = a[0]
r = a[-1]
ans = 0
for i in range(n):
    ans += min(abs(l - a[i]),abs(r - a[i]))
    l = min(l,a[i])
    r = max(r,a[i])

print(z)
