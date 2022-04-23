# https://atcoder.jp/contests/abc085/tasks/abc085_b

import sys

N = int(sys.stdin.readline().rstrip())
d = [int(sys.stdin.readline().rstrip()) for _ in range(N)]


def count_distinct(d):
    return len(set(d))


print(count_distinct(d))
