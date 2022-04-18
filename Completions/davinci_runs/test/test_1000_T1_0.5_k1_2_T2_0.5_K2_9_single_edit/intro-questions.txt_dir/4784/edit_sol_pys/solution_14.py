

import sys

def main():
    # Read input
    X = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    P = [int(sys.stdin.readline()) for i in range(N)]

    # Init
    MB_left = X

    # Loop through months and calculate remaining MB
    for i in range(N):
        if MB_left >= P[i]:
            MB_left -= P[i]
        else:
            MB_left = 0
        MB_left += X

    # Print result
    print(MB_left)


main()
