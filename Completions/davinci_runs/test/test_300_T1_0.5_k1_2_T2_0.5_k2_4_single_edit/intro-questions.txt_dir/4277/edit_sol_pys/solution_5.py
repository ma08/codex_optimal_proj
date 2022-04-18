
import sys

def min_expense(N, A, B):
    if N * A <= B:
N, A, B = map(int, sys.stdin.readline().rstrip().split())
        return N * A
    else:
        return B


print(min_expense(N, A, B))
