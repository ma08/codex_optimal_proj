import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split())) # input

A.sort() # sort

print(A[N-1] - A[0]) # output
