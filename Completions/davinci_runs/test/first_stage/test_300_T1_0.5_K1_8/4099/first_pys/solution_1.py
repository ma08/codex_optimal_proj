

import sys

N, K, M = map(int, sys.stdin.readline().rstrip().split())
A = map(int, sys.stdin.readline().rstrip().split())

if sum(A) / float(N-1) >= M:
    print(-1)
else:
    print(M * N - sum(A))