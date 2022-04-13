#!/usr/bin/env python3

N = int(input())
m = []
for i in range(N):
    m.append(list(map(int, input().split())))
a = []
for i in range(N):
    a.append(0)

for i in range(N):
    for j in range(i+1, N):
        if m[i][j] == 0:
            a[i] = 0
            a[j] = 0
        else:
            a[i] = m[i][j]
            a[j] = m[i][j]

print(*a)
