#!/usr/bin/env python3

n = int(input())
a = [int(i) for i in input().split()]

a = sorted(a)

count = 1
for i in range(1, n):
    if abs(a[i - 1] - a[i]) <= 5:
        count += 1
    else:
        break

for i in range(n - 2, -1, -1):
    if abs(a[i] - a[i + 1]) <= 5:
        count += 1
    else:
        break

print(count)
