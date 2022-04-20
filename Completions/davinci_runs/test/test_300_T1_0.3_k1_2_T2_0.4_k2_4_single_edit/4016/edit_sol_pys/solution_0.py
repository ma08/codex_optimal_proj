# https://atcoder.jp/contests/abc159/tasks/abc159_a

n, k = map(int, input().split())
t = input()

if k == 1:
    print(t)
else:
    print(t * (k - 1) + t[:n - 1])
