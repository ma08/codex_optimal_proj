
import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))

A.sort()

print(A[N-1] - A[0])
