
import sys

N = int(input())
A = list(map(int, input().split()))

# 全ての並び順を試す
ans = float('inf')
for i in range(N):
    total = A[i]
    for j in range(1, N):
        total += min(A[(i + j) % N] - A[(i + j - 1) % N], A[(i + j - 1) % N] + K - A[(i + j) % N])
    ans = min(ans, total)

print(ans)
