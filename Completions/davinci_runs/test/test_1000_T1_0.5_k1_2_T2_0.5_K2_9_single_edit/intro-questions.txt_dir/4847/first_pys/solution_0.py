

import sys

def area(A, B, C):
    return abs(A[0]*(B[1] - C[1]) + B[0]*(C[1] - A[1]) + C[0]*(A[1] - B[1]))/2

def contains(A, B, C, P):
    return area(A, B, C) == area(A, B, P) + area(A, P, C) + area(P, B, C)

A = tuple(map(int, sys.stdin.readline().split()))
B = tuple(map(int, sys.stdin.readline().split()))
C = tuple(map(int, sys.stdin.readline().split()))

N = int(sys.stdin.readline())

count = 0
for i in range(N):
    P = tuple(map(int, sys.stdin.readline().split()))
    if contains(A, B, C, P):
        count += 1

print("%.1f" % area(A, B, C))
print(count)