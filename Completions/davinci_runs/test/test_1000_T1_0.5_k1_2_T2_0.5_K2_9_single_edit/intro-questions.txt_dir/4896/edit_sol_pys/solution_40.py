#!/usr/bin/env python3

import re
import sys

def main():
    num_cases = int(sys.stdin.readline().strip())

    for _ in range(num_cases):
        num_bricks = int(sys.stdin.readline().strip())
        bricks = [int(x) for x in sys.stdin.readline().strip().split()]

        min_width = bricks[0]
        num_towers = 1

        for brick in bricks[1:]:
            if brick > min_width:
                num_towers += 1
                min_width = brick

        print(num_towers)

if __name__ == '__main__':
    main()
