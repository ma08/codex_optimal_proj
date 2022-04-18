# https://atcoder.jp/contests/abc051/tasks/abc051_b

n, k = map(int, input().split())
s = input()

if k > n or k == 0:
    print(-1)
else:
    print(n - k)
