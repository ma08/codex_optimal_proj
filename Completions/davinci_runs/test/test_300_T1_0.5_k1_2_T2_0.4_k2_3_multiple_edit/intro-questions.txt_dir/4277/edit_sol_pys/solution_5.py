# https://atcoder.jp/contests/abc086/tasks/abc086_a

import sys

A, B = map(int, sys.stdin.readline().rstrip().split())


def min_expense(N, A, B):
    if N * A <= B:
        return N * A
    else:
        return B


print(min_expense(N, A, B))
