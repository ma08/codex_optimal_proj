#!/usr/bin/env python3

N = int(input())

count = 0
for a in range(1, N+1):
    for b in range(1, N+1):
        c = N - a - b
        if c > 0 and a*b*c == N:
            count += 1

print(count)
