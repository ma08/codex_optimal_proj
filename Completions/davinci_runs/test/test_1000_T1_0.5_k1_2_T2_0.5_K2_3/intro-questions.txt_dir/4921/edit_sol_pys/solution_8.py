
import sys
import math

lines = []
for line in sys.stdin:
    lines.append(line)

words = []
for line in lines:
    words.append(line.split())

for line in words:
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            if line[i] == line[j]:
                line[i] = "."
                break
    print(" ".join(line))
