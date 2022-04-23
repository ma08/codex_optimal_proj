#!/usr/bin/env python3

import sys

# read inputs
lines = sys.stdin.readlines()
lines = [line.rstrip().split() for line in lines]

# calculate time in world A
for j in range(len(lines)):
    T = float(lines[j][0])
    X = float(lines[j][1])
    print(T / X)
