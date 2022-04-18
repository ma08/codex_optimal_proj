#!/usr/bin/python3

n = int(input())
pushes = list(map(int, input().split()))

cleanups = 0
dirtiness = 0

for day in range(1, 367):
    dirtiness += sum([max(0, day - push) for push in pushes if push <= day])
    if dirtiness >= 20:
        cleanups += 1
        dirtiness = 0

print(cleanups)
