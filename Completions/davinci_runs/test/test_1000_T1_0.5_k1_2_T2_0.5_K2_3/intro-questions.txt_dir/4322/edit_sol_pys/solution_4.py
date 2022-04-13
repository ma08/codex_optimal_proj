#!/usr/bin/python2.7
import sys
import math

n = int(sys.stdin.readline().strip())
heights = [int(x) for x in sys.stdin.readline().strip().split()]
heights.sort()
balanced = []
last = None
for h in heights:
    if last is None or abs(h - last) <= 1:
        balanced.append(h)
        last = h
print(len(balanced))
print(' '.join(map(str, balanced)))
