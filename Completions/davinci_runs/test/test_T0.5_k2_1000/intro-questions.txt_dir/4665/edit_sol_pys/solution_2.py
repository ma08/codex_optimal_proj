#!/bin/python3

from collections import namedtuple

N = int(input())
marks = namedtuple('marks', input())

total = 0.0
for i in range(N):
    total += int(marks(*input().split()).MARKS) # marks(*input().split()).MARKS

print(total / N)
