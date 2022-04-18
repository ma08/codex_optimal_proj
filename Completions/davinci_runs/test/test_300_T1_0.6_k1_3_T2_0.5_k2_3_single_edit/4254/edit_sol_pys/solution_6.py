
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    if i % 2 == 0:
        print(A[i], end=" ")
