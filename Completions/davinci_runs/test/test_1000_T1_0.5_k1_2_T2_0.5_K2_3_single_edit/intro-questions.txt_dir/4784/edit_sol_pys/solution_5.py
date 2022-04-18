#!/bin/python3


X = int(input())
N = int(input())

total = X
for i in range(N):
    total -= int(input())

print(total)
