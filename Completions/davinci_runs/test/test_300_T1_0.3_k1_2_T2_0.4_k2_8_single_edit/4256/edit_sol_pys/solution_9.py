#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    print(min(b // a, c))
