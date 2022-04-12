#!/bin/python3

from __future__ import print_function
from collections import namedtuple

N = int(input())
marks = namedtuple('marks', input())

total = 0.0
for i in range(N):
    total += int(marks(*input().split()).MARKS)  # marks is a class

print(total / N)
