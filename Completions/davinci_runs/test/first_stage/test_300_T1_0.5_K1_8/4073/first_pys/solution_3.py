

import sys
import math

def main():
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]

    # sort the array
    a.sort()

    # find the maximum possible number of pairs
    # this is the maximum number of elements that can be paired
    # with the first element
    pairs = 0
    for i in range(1, n):
        if a[i] - a[0] > 4:
            break
        pairs += 1

    # find the maximum possible number of pairs
    # this is the maximum number of elements that can be paired
    # with the last element
    for i in range(n-2, -1, -1):
        if a[n-1] - a[i] > 4:
            break
        pairs = max(pairs, n-1-i)

    print(n - pairs)

if __name__ == "__main__":
    main()