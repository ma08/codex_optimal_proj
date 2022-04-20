

N = int(input())
A = list(map(int, input().split()))

A.sort()

while len(A) > 1:
    A = A[:-2] + [A[-1] - A[-2]]

print(A[0])
