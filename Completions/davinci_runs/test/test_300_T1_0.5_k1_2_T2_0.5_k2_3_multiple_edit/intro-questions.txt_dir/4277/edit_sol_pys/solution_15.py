import sys
N, A, B = map(int, sys.stdin.readline().rstrip().split())

def minExpense(N, A, B):
    if N * A <= B:
        return N * A
    else:
        return B


print(minExpense(N, A, B))
