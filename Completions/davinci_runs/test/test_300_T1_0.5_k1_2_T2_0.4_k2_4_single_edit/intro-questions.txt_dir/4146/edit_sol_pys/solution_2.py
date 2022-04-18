
import sys

n = int(input())
v = list(map(int, sys.stdin.readline().split()))

a = [0] * (10**5 + 2)
for i in range(n):
    a[v[i]] += 1

a.sort()

ans = 0
if a[-1] == a[-2]:
    ans = 0
else:
    ans = a[-1] - a[-2]

print(ans)
