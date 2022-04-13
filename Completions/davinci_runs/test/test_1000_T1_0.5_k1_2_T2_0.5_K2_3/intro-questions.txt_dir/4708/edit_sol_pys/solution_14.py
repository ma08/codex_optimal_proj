# https://atcoder.jp/contests/abc095/tasks/abc095_b

import sys

N, X = map(int, sys.stdin.readline().split())
M = [int(sys.stdin.readline()) for _ in range(N)]

print(N + (X - sum(M)) // min(M))
