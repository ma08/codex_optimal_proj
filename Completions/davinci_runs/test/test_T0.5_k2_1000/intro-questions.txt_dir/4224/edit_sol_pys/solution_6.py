# https://atcoder.jp/contests/abc093/tasks/arc094_a

a, b, c = [int(x) for x in input().split()]

ans = 0

if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    ans = 0
else:
    ans = min(a * b, b * c, c * a)

print(ans)
