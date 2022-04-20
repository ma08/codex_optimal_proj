

import sys

# Get the input from the console
a, b, c = [int(x) for x in sys.stdin.readline().split()]

# Calculate the amount of water that will remain in Bottle 2
print(c - (a - b))