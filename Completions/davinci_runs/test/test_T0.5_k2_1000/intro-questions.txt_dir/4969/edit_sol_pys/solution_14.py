#!/usr/bin/env python3

import sys
import math

def main():
    R, C = map(int, sys.stdin.readline().strip().split())
    total_area = math.pi * R * R
    cheese_area = math.pi * (R - C) * (R - C)
    print(cheese_area / total_area * 100)

if __name__ == '__main__':
    main()
