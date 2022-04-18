
import sys

N, A, B = map(int, sys.stdin.readline().rstrip().split())  # input N, A, B

def min_expense(N, A, B):  # function for finding minimum expense
    if N * A <= B:
        return N * A
    else:
        return B


print(min_expense(N, A, B))
