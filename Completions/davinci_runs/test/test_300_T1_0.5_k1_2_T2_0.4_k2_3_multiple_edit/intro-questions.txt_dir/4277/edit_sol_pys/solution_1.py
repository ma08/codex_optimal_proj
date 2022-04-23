# https://atcoder.jp/contests/abc086/tasks/abc086_a

import sys

N = int(sys.stdin.readline().rstrip())


def is_odd(N):
    return N % 2 == 1



print(is_odd(N))
