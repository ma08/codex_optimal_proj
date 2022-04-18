#!/usr/bin/env python3

import sys

N, T, M = map(int, sys.stdin.readline().split()) # N = number of rows, T = number of columns, M = number of files

print(N * T * M)
