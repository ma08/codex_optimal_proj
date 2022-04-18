#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 13:45:41 2020


@author: karanwaghela
"""

import sys
from collections import defaultdict

def max_pair():
    n, m = map(int, sys.stdin.readline().strip().split())
    A = list(map(int, sys.stdin.readline().strip().split()))
    count = defaultdict(int)
    for a in A:
        count[a] += 1
        
    pairs = 0
    for c in count.values():
        pairs += c // 2
        
    if pairs >= m:
        return m
    else:
        return pairs + (m - pairs) // 2

if len(socks) % 2 != 0:
    print('impossible')
else:
    sock_count = Counter(socks)
    pairs_needed = 0
    for i in sock_count.values():
        pairs_needed += i // 2
    if pairs_needed > pairs:
        print('impossible')
    else:
        print(pairs * 2 - pairs_needed)
