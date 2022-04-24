

import sys

N, K = map(int, sys.stdin.readline().split())
if N % K == 0:
    print(0)
else:
    print(N % K)
