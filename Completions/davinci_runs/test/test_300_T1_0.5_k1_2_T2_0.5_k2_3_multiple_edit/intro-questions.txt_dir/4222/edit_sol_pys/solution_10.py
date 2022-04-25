import numpy as np

N, K = map(int, input().split())

A = np.empty(K, dtype=np.ndarray)
for i in range(K):
    d = int(input())
    A[i] = np.array(input().split(), dtype=int)

A_flat = np.unique(A)

ans = N - len(A_flat)
print(ans)
