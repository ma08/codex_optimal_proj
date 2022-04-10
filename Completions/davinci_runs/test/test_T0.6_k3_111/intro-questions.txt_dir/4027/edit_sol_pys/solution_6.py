#!/usr/bin/env python3

import sys
import math

def minDiff(m):
    if m % 2 == 0:
        return m // 2
    else:
        return 1

if __name__ == '__main__':
    m = int(sys.stdin.readline().strip())
    print(minDiff(m))
