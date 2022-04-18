#!/usr/bin/env python3

import sys

def main():
    # Read the number of rods
    N = int(sys.stdin.readline())

    # Read the lengths of the rods
    rods = []
    for i in range(N):
        rods.append(int(sys.stdin.readline()))

    # Sort the rods from shortest to longest
    rods.sort()

    # Iterate over the rods
    while len(rods) > 1:
        # Fuse the two shortest rods
        rods[0] = rods[0] + rods[1] - 1
        # Remove the second shortest rod
        del rods[1]
        # Sort the rods from shortest to longest
        rods.sort()

    # Print the length of the resulting javelin
    print(rods[0])

if __name__ == "__main__":
    main()
