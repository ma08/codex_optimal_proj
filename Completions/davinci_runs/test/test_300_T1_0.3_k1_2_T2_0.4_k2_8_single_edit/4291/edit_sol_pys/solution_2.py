# https://atcoder.jp/contests/abc086/tasks/abc086_b

n, q = map(int, input().split())
s = input()
a = list(map(int, input().split()))
a.sort()
print(a[0] + a[1])
