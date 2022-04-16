

import sys, heapq

n, m = map(int, input().split())
A = list(map(int, input().split())) + [0] * (n + 1)

# 全ての順列を試す
ans = float('inf')
for i in range(N):
    total = 0
    for j in range(1, N):
        total += A[(i + j) % N] - A[(i + j - 1) % N]
    ans = min(ans, total)

print(ans)
