# -*- coding: utf-8 -*-

n = int(input())

l = []
for i in range(n):
    l.append(int(input()))

l.sort(reverse = True)

output = 0
for i in range(n - 1):
    output += l[i] - 1

output += l[-1]

print(output)
