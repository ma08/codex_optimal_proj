#!/usr/bin/python3

n, m = map(int, input().split())
d = []
for i in range(n):
    d.append(input())

t = 0
for i in d:
    for j in i:
        if j == '_':
            t += 1
print(t)
