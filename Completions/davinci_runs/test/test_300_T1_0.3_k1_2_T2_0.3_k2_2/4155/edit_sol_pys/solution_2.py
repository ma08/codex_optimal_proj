#!/usr/bin/env python3

import sys

# Read input
n = int(sys.stdin.readline().rstrip())
h = list(map(int, sys.stdin.readline().rstrip().split()))

# Initialize
count = 0

# For each flower
for i in range(n):
    # If the flower is not at the right height
    if h[i] != 0:
        # Water the flowers to the left
        for j in range(i):
            h[j] += 1
        # Water the flowers to the right
        for j in range(i + 1, n):
            h[j] += 1
        # Increment the count
        count += 1

# Print the count
print(count)
