
import sys

N, A, B = map(int, sys.stdin.readline().split())


def min_expenses(N, A, B):
    if N * A <= B:
        return N * A
    else:
        return B


print(min_expenses(N, A, B))
