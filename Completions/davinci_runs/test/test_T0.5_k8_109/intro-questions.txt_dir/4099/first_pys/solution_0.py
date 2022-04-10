

import sys
import numpy as np

# input
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# solve
if N == 1:
    print(M)
    sys.exit()

A_ave = np.mean(A)
if A_ave >= M:
    print(0)
    sys.exit()

if N*K < M*N:
    print(-1)
    sys.exit()

A_ave = (M*N - sum(A))/(N-1)
print(np.ceil(A_ave))