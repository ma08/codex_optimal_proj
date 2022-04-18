

import sys
import math

n = int(input())
a = list(map(int, input().split()))

d = {}

for i in range(n):
    if a[i] not in d:
        d[a[i]] = 1
    else:
        d[a[i]] += 1

sorted_keys = sorted(d.keys())

if len(sorted_keys) == 2:
    if sorted_keys[0] == sorted_keys[1] - 1:
        if d[sorted_keys[0]] == d[sorted_keys[1]]:
            print('YES')
            print(sorted_keys[0], sorted_keys[1])
            sys.exit()

if len(sorted_keys) == 3:
    if sorted_keys[0] == sorted_keys[1] - 1 and sorted_keys[1] == sorted_keys[2] - 1:
        if d[sorted_keys[0]] == d[sorted_keys[1]] and d[sorted_keys[1]] == d[sorted_keys[2]]:
            print('YES')
            print(sorted_keys[0], sorted_keys[1], sorted_keys[2])
            sys.exit()

print('NO')
