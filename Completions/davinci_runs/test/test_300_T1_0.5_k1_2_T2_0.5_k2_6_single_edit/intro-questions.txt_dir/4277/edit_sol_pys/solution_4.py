import sys
N, A, B = map(int, sys.stdin.readline().rstrip().split())


def min_expense(N, A, B):
    if N * A <= B:
        return N * A
    else:
        return B


print(min_expense(N, A, B))
