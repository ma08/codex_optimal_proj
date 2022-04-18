#!/usr/bin/env python


import sys, re, operator, string
#import numpy as np
from itertools import product
from functools import reduce
from collections import Counter

def main():
    N = int(sys.stdin.readline().rstrip())
    As = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(N):
        As[i] = (As[i], i)
    As = sorted(As, key=lambda x: x[0], reverse=True)
    for i in range(N):
        print(As[i][1]+1)

if __name__ == '__main__':
    main()
