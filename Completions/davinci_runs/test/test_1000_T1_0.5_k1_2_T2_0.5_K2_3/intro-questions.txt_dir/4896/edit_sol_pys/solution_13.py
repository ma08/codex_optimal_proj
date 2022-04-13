#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline())
    bricks = list(map(int, sys.stdin.readline().split()))
    towers = [bricks[0]]

    for brick in bricks:
        if brick > towers[-1]:
            towers.append(brick)
        else:
            for i in range(len(towers) - 1, -1, -1):
                if brick < towers[i]:
                    towers[i] = brick
                    break
    print(len(towers))

if __name__ == '__main__':
    main()
