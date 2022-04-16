#!/bin/python3

N = int(input())
costumes = []
for i in range(N):
    costumes.append(int(input()))

costumes.sort()

print(costumes[-1] - costumes[0])
