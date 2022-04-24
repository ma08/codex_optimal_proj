import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort()

for i in range(N):
    if A[i] < B[i]:
        print("No")
        exit()

print("Yes")
