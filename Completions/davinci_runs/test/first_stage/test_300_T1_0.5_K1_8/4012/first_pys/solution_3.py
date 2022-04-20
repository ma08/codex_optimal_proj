

# SOLUTION
import sys

# sys.stdin = open('../input.txt', 'r')

T = int(input())

for _ in range(T):
    a, b, c = map(int, input().split())

    res = 0
    A = a
    B = b
    C = c

    while not (B % A == 0 and C % B == 0):
        if A == B and B == C:
            break
        elif A == B and B < C:
            B += 1
            res += 1
        elif A < B and B == C:
            A += 1
            res += 1
        elif A < B and B < C:
            if (C - B) > (B - A):
                A += 1
                res += 1
            else:
                B += 1
                res += 1

    print(res)
    print(A, B, C)