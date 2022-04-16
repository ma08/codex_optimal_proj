
#Program

import sys
import math

def main():
    m = int(sys.stdin.readline())

    # Generate a list of all the cubes up to the limit
    cubes = [i**3 for i in range(1, int(m ** (1/3)) + 1)]

    # Generate a list of all the sums of two cubes
    sums = [cubes[i] + cubes[j] for i in range(len(cubes)) for j in range(i, len(cubes))]

    # Count the number of times each sum appears
    sums.sort()
    counts = []
    count = 1
    for i in range(1, len(sums)):
        if sums[i] == sums[i-1]:
            count += 1
        else:
            counts.append(count)
            count = 1
    counts.append(count)

    # Find the largest sum that appears at least twice
    for i in range(len(sums)-1, -1, -1):
        if counts[i] > 1 and sums[i] <= m:
            print(sums[i])
            break
    else:
        print("none")

main()
