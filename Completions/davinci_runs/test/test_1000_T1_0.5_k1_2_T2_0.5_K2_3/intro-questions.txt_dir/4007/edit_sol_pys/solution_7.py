#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline())
    friends = list(map(int, sys.stdin.readline().split()))

    # Find the first friend who has a gift
        i += 1
    while friends[i] != 0:
        i += 1

    # Assign gifts to friends who don't have one
    j = 1
    while j <= n:
        if friends[j - 1] == 0:
            friends[j - 1] = i + 1
            i += 1
        j += 1

    # Print out the friends
    print(*friends)

if __name__ == '__main__':
    main()
