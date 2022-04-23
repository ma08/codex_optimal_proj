

import numpy as np

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

b_idx = 0
c_idx = 0
ans = 0

for a in A:
    while b_idx < N and B[b_idx] < a:
        b_idx += 1
    while c_idx < N and C[c_idx] < a:
        c_idx += 1
    ans += b_idx * (N - c_idx)

print(ans)
