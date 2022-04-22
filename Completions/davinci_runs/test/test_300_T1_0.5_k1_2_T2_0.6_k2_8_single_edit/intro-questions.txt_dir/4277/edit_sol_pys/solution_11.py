
import math
import sys

N, A, B = map(int, sys.stdin.readline().rstrip().split())


def min_expense(N, A, B):
    return min(A * N, B)


print(min_expense(N, A, B))
