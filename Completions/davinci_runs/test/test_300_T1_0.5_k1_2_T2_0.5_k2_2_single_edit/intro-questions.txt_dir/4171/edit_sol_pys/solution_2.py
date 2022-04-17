# Problem

https://atcoder.jp/contests/abc061/tasks/abc061_b

# Solution

n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == 1:
    print(max(a))
else:
    print(max(a) - min(a) + 1)
