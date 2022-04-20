
import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
total = sum(A)
A.sort(reverse=True)

if A[M-1] >= total/(4*M):
    print('Yes')
else:
    print('No')