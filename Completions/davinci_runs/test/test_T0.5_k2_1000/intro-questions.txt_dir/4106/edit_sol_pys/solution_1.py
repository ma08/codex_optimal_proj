#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from collections import deque
from itertools import accumulate, chain

def solve(n, k, x, a):
    if x < k:
        return -1
    elif k == 1:
        return sum(a)
    else:
        acc = list(chain([0], accumulate(a)))
        prefix = [0] + acc[:n-k]
        suffix = acc[k:] + [0]
        max_suffix = deque([0])
        for i in range(n-k-1, -1, -1):
            max_suffix.appendleft(max(max_suffix[0], suffix[i]))
        return max(prefix[i]+max_suffix[i+1] for i in range(n-k+1))

def main():
    n, k, x = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    print(solve(n, k, x, a))

if __name__ == "__main__":
    main()
