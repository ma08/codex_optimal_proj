import math

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A)
# print(A)
ans = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if A[i] * A[j] <= K:
            ans = max(ans, A[i] * A[j])

print(ans)
