# https://atcoder.jp/contests/abc084/tasks/abc084_a

import sys

N, A, B = map(int, sys.stdin.readline().rstrip().split())


def min_expense(n, a, b):
    return min(n * a, b)


print(min_expense(N, A, B))
