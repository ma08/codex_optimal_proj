#!/usr/bin/env python3

import sys

def main():
    N = int(sys.stdin.readline().strip())
    rods = []
    for i in range(N):
        rods.append(int(sys.stdin.readline().strip()))
    rods.sort()
    while len(rods) > 1:
        rods.append(rods.pop() + rods.pop() - 1)
        rods.sort()
    print(rods[0])

if __name__ == '__main__':
    main()
