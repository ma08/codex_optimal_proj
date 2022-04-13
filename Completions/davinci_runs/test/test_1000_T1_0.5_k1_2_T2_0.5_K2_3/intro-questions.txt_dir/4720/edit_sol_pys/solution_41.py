# https://atcoder.jp/contests/abc176/tasks/abc176_a

n, x, t = map(int, input().split())

print((n + x - 1) // x * t)
