
import sys
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 全ての順列を試す
ans = float('inf')
for i in range(K):
    total = 0
    for j in range(1, K):
        total += A[(i + j) % K] - A[(i + j - 1) % K]
    ans = min(ans, total)

print(ans)
