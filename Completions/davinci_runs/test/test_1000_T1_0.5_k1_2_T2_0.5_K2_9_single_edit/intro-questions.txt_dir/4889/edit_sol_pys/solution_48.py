#!/usr/bin/env python

import sys

def main():
    n = int(sys.stdin.readline().strip())
    rods = [int(sys.stdin.readline().strip()) for i in range(n)]
    rods.sort()
    while len(rods) > 1:
        rods[0] += rods.pop(-1)
        rods.sort()
    print(rods[0])

if __name__ == '__main__':
    main()
