
import sys

n = int(input())
a = [int(s) for s in input().split()]

for i in range(n):
    a.append(a[i])
    a.reverse()

print(*a)
