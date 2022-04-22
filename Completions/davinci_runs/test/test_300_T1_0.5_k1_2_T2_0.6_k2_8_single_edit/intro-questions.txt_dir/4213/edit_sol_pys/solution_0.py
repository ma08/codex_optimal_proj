

import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split())) # A = [1, 2, 3, 4]

A.sort() # A = [1, 2, 3, 4]

print(A[N-1] - A[0]) # 4 - 1 = 3
