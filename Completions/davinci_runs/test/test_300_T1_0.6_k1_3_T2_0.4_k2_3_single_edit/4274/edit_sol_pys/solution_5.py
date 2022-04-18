#!/usr/bin/env python3

import sys

N, M = list(map(int, sys.stdin.readline().split()))

if N == M:
    print("Yes")
else:
    print("No")
