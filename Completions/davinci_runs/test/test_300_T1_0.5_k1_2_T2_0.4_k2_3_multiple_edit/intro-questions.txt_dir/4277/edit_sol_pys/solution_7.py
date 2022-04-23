# https://atcoder.jp/contests/abc086/tasks/abc086_a

import sys

a, b = map(int, sys.stdin.readline().rstrip().split())


if a * b % 2 == 0:
    print("Even")
else:
    print("Odd")

