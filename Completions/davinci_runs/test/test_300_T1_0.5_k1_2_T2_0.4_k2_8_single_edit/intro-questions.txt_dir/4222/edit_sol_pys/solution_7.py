#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

import numpy as np
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
INF = float('inf')
import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[n//2] - a[n//2 - 1])

if __name__ == '__main__':
    main()
