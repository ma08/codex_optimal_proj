#!/usr/bin/env python3

import math

# Read input
x, y, x1, y1, x2, y2 = map(int, input().split())  # input() gives a string

# Find the distances to the sides of the rectangle
dx = min(abs(x - x1), abs(x - x2))
dy = min(abs(y - y1), abs(y - y2))

# Print the minimum distance
print(math.sqrt(dx * dx + dy * dy))
