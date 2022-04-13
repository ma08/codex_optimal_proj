#! /usr/bin/env python3

n, k = map(int, input().split())
throws = input().split()

pos = 0

for i in range(k):
    if throws[i] == 'undo':
        pos += int(throws[i+1])
    else:
        pos += int(throws[i])
        if pos > n-1:
            pos -= n
        elif pos < 0:
            pos += n

print(pos)
