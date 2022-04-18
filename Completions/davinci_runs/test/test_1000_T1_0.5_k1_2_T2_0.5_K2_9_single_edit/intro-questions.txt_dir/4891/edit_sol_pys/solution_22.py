#!/usr/bin/env python

import sys

# Get input
pieces = [int(x) for x in sys.stdin.readline().split(' ')]

# Check if each piece is in the correct quantity
print(str(1 - pieces[0]) + ' ' + str(1 - pieces[1]) + ' ' + str(2 - pieces[2]) + ' ' + str(2 - pieces[3]) + ' ' + str(2 - pieces[4]) + ' ' + str(8 - pieces[5]))
