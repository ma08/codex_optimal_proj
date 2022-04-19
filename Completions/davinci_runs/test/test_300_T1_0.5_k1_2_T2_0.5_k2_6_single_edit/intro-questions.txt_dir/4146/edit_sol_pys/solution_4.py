
import sys

n = int(input())
v = map(int, input().split())

a = [0] * (10 ** 5 + 1)
for i in v:
    a[i] += 1

ans = 0
for i in range(10 ** 5 + 1):
    if a[i] == a[i + 1]:
        ans = 0
    else:
        ans = a[i] - a[i + 1]

print(ans)
