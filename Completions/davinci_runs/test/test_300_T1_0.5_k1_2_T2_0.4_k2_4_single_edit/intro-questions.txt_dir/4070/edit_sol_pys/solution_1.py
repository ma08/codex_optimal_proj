#!/usr/bin/env python3

from math import sqrt
from itertools import count, islice
import sys

def main():
    n = int(sys.stdin.readline())
    print(solve(n)) 

def solve(n):
    return int(sqrt(n))

if __name__ == '__main__':
    main()
