
import sys

n = int(input())
a = list(map(int, input().split()))

a.sort()

s = 0
for i in range(n):
    s += a[i]*(i+1) + 1

print(s)
print(*[i+1 for i in range(n)])
