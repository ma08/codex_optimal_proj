

import math
import sys

rows, cols = map(int, input().split())

# Just count the number of free spaces
free = 0
for i in range(rows):
    for j in range(cols):
        if input() == '.':
            free += 1
        input()

# Squash 0, 1, 2, 3, or 4 cars
print(math.ceil(free/2))
print(math.ceil((free - 2*cols)/2))
print(math.ceil((free - 4*cols)/2))
print(math.ceil((free - 6*cols)/2))
print(math.ceil((free - 8*cols)/2))
