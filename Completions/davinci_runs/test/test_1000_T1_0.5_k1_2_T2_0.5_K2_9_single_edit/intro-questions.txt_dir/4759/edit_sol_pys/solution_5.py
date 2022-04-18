#!/usr/bin/python3

import sys

n = int(input())
arr = list(map(int, input().split()))

sum = 0
count = 0

for i in arr:
    if i == -1:
        continue
    else:
        sum += i

print(sum / count)
