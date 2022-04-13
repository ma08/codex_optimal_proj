#!/usr/bin/python3

import sys

lines = []
for line in sys.stdin:
    lines.append(line)

words = []
for line in lines:
    words.append(line.split())

for line in words:
    for i in range(len(line)):
        if line[i] in line[i + 1:]:
            line[i] = "*"
    print(" ".join(line))
