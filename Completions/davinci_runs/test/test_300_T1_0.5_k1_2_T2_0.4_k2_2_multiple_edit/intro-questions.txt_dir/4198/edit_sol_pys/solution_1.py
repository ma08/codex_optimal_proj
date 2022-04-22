
# https://atcoder.jp/contests/abc085/tasks/abc085_b
a, b, x = map(int, input().split())

if a + b > x:
    print(0)
    exit()

k = (x - b) // a
l = len(str(k))

if a * k + b * l <= x:
    print(k)
else:
    print(k - 10 ** (l - 1))  # 10 ** (l - 1) = 10^(l-1)
