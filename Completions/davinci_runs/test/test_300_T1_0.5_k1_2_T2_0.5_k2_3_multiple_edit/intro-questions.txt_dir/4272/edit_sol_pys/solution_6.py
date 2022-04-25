# https://atcoder.jp/contests/abc176/tasks/abc176_a

n, x, t = map(int, input().split())

if n % x == 0:
    print(n // x * t)
else:
    print((n // x + 1) * t)
