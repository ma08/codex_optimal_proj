#!/usr/bin/env python3

import sys

def min_coins_to_equalize(positions):
    if len(positions) == 1:
        return 0
    positions.sort()
    mid_pos = positions[len(positions) // 2 - 1]
    return sum(abs(mid_pos - pos) for pos in positions)

def main():
    n = int(input())
    positions = list(map(int, input().split()))
    print(min_coins_to_equalize(positions))

if __name__ == '__main__':
    main()
