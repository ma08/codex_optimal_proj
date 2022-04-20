#!/usr/bin/env python3

import sys

N = int(sys.stdin.readline())

# If N is even, there is no need to calculate.
if N % 2 == 0:
    print(N)
else:
    print(N*2)
