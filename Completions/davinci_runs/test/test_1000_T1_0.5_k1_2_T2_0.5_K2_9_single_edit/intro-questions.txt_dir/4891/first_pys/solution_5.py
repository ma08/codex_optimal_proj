

import sys

# Get input
pieces = [int(x) for x in sys.stdin.readline().split()]

# Check if each piece is in the correct quantity
print(1 - pieces[0], 1 - pieces[1], 2 - pieces[2], 2 - pieces[3], 2 - pieces[4], 8 - pieces[5])