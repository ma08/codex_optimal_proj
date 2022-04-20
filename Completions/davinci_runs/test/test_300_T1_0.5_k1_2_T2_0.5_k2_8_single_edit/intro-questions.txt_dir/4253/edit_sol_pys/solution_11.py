

N = int(input())
A = [int(input()) for _ in range(N)]

A.sort()

print(A[-1] - A[0])
