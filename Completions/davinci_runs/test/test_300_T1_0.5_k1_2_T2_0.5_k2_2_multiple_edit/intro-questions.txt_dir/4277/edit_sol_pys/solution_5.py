import sys

def min_expense(N, A, B):
    if N * A <= B:
        return N * A
    else:
        return B
N, A, B = map(int, sys.stdin.readline().rstrip().split())


print(min_expense(N, A, B))
