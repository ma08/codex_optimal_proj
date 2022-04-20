

import numpy as np

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if A[i] + A[j] + A[k] >= K:
                ans += 1

print(ans)
