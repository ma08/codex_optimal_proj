import sys

def rearrange(n, A):
    A = sorted(A)
    if n % 2 == 0:
        A1 = A[:n//2]
        A2 = A[n//2:]
    else:
        A1 = A[:n//2]
        A2 = A[n//2+1:]
    A1.reverse()
    A1 = A1 + A2
    return A1

n = int(input())
A = [int(x) for x in input().split()]

print(*rearrange(n, t))
