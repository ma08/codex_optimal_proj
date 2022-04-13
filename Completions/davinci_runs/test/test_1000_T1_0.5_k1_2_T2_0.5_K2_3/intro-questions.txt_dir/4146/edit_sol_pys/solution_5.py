
import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort()
b.sort()
c.sort()

ans = 0
for i in range(n):
    for j in range(m):
        for k in range(n):
            if b[j] > a[i] and b[j] > c[k]:
                ans += 1

ans = 0
if a[-1] == a[-2]:
    ans = 0
else:
    ans = a[-1] - a[-2]

print(ans)
