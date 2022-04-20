#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: September 2019
# This program prints out the missing numbers in a list



n = int(input())
f = list(map(int, input().split()))

for i in range(n):
    if f[i] == 0:
        for j in range(1, n+1):
            if j not in f:
                f[i] = j
                break

print(*f)
