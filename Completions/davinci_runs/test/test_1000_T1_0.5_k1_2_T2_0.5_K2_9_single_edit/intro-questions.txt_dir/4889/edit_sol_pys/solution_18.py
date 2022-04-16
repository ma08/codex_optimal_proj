

import sys, math

def main():
    # Read the number of rods
    N = int(input())

    # Read the lengths of the rods
    rods = []
    for i in range(N):
        rods.append(int(input()))

    # Sort the rods from shortest to longest
    rods.sort()

    # Iterate over the rods
    while len(rods) > 1:
        # Fuse the two shortest rods
        rods[0] = rods[0] + rods[1] - 1 #-1 to account for the overlap
        # Remove the second shortest rod
        del rods[1]
        # Sort the rods from shortest to longest
        rods.sort()

    # Print the length of the resulting javelin
    print(math.ceil(rods[0]/2)) #/2 because of the overlap

if __name__ == "__main__":
    main()
