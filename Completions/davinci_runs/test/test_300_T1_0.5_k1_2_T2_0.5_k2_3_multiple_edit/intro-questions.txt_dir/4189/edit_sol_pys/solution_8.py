#!/usr/bin/env python3



n = int(input())
soft, hard = 0, 0
for _ in range(n):
    name, type = input().split()
    if type == 'soft':
        soft += 1
    elif type == 'hard':
        hard += 1
print(soft*hard)
