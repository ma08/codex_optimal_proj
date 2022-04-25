
# https://atcoder.jp/contests/abc126/tasks/abc126_a
a,b,k = map(int, input().split())

if k <= a:
    a -= k
else:
    k -= a
    a = 0
    if k <= b:
        b -= k
    else:
        b = 0

print(a,b)
