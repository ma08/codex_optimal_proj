#!/usr/bin/python3

n = int(input())

days = [0 for i in range(365)]

for i in range(n):
    start, end = map(int, input().split())
    for j in range(start - 1, end):
        days[j] += 1

print(sum(days))
