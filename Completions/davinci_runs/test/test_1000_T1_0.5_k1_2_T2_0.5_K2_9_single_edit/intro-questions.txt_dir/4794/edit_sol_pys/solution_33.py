
import sys

rows, cols = map(int, sys.stdin.readline().split())

# Just count the number of free spaces
free = 0
for i in range(rows):
    for j in range(cols):
        if sys.stdin.read(1) == '.':
            free += 1
        sys.stdin.read(1)

# Squash 0, 1, 2, 3, or 4 cars, if possible
if free >= 0:
    print(free)
if free - 2*cols >= 0:
    print(free - 2*cols)
if free - 4*cols >= 0:
    print(free - 4*cols)
if free - 6*cols >= 0:
    print(free - 6*cols)
if free - 8*cols >= 0:
    print(free - 8*cols)
