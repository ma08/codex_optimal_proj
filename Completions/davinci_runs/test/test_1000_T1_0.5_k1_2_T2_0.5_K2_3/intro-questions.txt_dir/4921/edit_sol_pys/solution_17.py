
import sys
import math

lines = []
for line in sys.stdin:
    lines.append(line)

words = []
for line in lines:
    words.append(line.split())

print(words)

for line in words:
    i = 0
    while i < len(line):
        if line[i] in line[i+1:]:  # check if the word appears more than once
            line[i] = "."  # if the word appears more than once, replace it with a dot
        i += 1
    print(" ".join(line))
