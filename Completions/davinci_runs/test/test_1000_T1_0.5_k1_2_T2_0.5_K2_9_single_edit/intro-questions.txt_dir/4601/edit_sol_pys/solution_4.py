import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())

s = list(map(int, sys.stdin.readline().split()))

s.sort()

h.sort()

ans = 0
for i in range(n):
    if h[i] < k:
        ans += h[i]
        k -= h[i]
    else:
        ans += k
        k = 0
        ans += (h[i] - k)

print(ans)
