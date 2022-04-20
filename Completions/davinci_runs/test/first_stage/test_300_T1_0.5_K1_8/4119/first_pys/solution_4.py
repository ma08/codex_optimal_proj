

import sys

n, m = map(int, sys.stdin.readline().split())
xs = list(map(int, sys.stdin.readline().split()))

xs.sort()

# print(n, m)
# print(xs)

ans = 0

i = 0
while i < m:
    l = xs[i]
    while i < m and xs[i] <= l + n - 1:
        i += 1
    ans += 1

print(ans)