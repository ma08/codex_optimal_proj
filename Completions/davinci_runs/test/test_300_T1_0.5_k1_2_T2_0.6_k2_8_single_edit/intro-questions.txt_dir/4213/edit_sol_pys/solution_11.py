
import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))

A.sort()
print(A[-1] - A[0])
