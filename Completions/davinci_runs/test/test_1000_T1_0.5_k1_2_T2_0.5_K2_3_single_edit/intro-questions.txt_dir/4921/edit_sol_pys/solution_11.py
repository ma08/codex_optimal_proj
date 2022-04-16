

import sys
import math

lines = []
for line in sys.stdin:
    lines.append(line)

words = []
for line in lines:
    words.append(line.split())

for line in words:
    i = 0
    while i < len(line):
        if line[i] in line[i+1:]:
            line[i] = "."
        i += 1
    print(" ".join(line)) 
