# https://atcoder.jp/contests/abc084/tasks/abc084_b

import sys

n, k = map(int, sys.stdin.readline().split())
p = list(map(int, sys.stdin.readline().split()))

print(sum(sorted(p)[:k]))
