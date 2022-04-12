#!/usr/bin/env python3

import sys

def main():
    n = int(input())
    bricks = [int(x) for x in input().split()]  # list comprehension
    towers = 0
    base = 0

    for brick in bricks:
        if brick > base:
            towers += 1
            base = brick

    print(towers)

if __name__ == '__main__':
    main()
