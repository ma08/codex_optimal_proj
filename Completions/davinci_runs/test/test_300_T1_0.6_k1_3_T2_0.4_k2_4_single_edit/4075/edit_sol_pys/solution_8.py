
import sys
import math
N = int(input())
A = [int(i) for i in input().split()]
A.sort()
if N % 2 == 0:
    print(sum([abs(A[i] - A[N-i-1]) for i in range(N//2)]))
else:
    print(sum([abs(A[i] - A[N-i-1]) for i in range(N//2)]) + abs(A[N//2]))
