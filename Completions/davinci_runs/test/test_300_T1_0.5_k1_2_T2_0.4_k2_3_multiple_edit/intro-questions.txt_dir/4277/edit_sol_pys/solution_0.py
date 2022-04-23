
# 파이썬은 이렇게 입력을 받는다.
import sys

N, A, B = map(int, sys.stdin.readline().rstrip().split()) # 입력을 받는다.


def min_expense(N, A, B):
    if N * A <= B:
        return N * A
    else:
        return B


print(min_expense(N, A, B))
