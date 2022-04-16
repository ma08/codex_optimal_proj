

import sys, os

def main():
    # Read the number of rods
    N = int(sys.stdin.readline()) # read from input

    # Read the lengths of the rods
    rods = []
    for i in range(N): # iterate over all the rods
        rods.append(int(sys.stdin.readline()))

    # Sort the rods from shortest to longest
    rods.sort() # sort the rods from shortest to longest

    # Iterate over the rods
    # iterate over all the rods
    while len(rods) > 1:
        # Fuse the two shortest rods
        rods[0] = rods[0] + rods[1] - 1

        # Remove the second shortest rod
        del rods[1]

        # Sort the rods from shortest to longest
        rods.sort()

    # Print the length of the resulting javelin
    print(rods[0]) # print the length of the resulting javelin

if __name__ == "__main__":
    main()
