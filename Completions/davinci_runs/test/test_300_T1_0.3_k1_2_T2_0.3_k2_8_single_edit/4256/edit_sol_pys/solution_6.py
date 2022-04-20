#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    A, B, C = map(int, sys.stdin.readline().rstrip().split())
    print(min(B // A, C))
