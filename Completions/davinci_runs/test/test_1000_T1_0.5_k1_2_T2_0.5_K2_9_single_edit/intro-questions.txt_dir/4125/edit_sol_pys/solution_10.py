

import math

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

B = [0] * N
for i in range(N - 1):
    B[i + 1] = B[i] + A[i]

ans = 0
for i in range(N - K + 1):
    ans += B[i + K] - B[i]

print(ans / (N - K + 1))
