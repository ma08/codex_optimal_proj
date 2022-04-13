#!/usr/bin/env python

# Read input
N = int(raw_input())

# Check if N is even or odd
if (N % 2 == 0):
    if (N >= 2 and N <= 5):
        print("Not Weird")
    elif (N >= 6 and N <= 20):
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")
