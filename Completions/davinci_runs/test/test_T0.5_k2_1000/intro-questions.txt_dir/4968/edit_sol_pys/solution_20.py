

import sys, math

[N, M] = map(int, sys.stdin.readline().split())
A = map(int, sys.stdin.readline().split())
B = map(int, sys.stdin.readline().split())

def check(A, B):
    for i in A:
        if i in B:
            A.remove(i)
            B.remove(i)
    return len(A)

print check(A, B)
