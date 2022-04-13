#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline())
    bricks = list(map(int, sys.stdin.readline().split()))
    towers = [0] * n

    for brick in bricks:
        for i in range(n):
            if brick < towers[i]:
                towers[i] = brick
                break
    print(towers)

if __name__ == '__main__':
    main()
