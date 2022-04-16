

import sys

def main():
    # Read the number of rods and the target length
    N, T = map(int, sys.stdin.readline().strip().split())

    # Read the lengths of the rods
    rods = []
    for i in range(N):
        rods.append(int(sys.stdin.readline()))

    # Sort the rods from shortest to longest
    rods.sort()

    # Iterate over the rods while the target length is not reached
    while rods[0] < T:
        # If there is only one rod left, the target length cannot be reached
        if len(rods) == 1:
            print("impossible")
            return

        # If there are two or more rods left, fuse the two shortest rods
        else:
            rods[0] = rods[0] + rods[1] - 1
            # Remove the second shortest rod
            del rods[1]
            # Sort the rods from shortest to longest
            rods.sort()

    # If the target length is reached, print the number of operations
    print(N - len(rods))

if __name__ == "__main__":
    main()
