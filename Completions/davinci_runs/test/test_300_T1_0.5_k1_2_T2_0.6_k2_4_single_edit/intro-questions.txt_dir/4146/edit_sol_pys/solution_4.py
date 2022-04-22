

import sys

n = int(input())
v = list(map(int, input().split()))

a = [0] * (10**5 + 1)
for i in v:
    a[i] += 1

a.sort()

ans = max(0, a[-1] - a[-2])

print(ans)
