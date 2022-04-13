


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 12:24:43 2020

@author: kieranodonnell
"""
# SOLUTION

from collections import Counter

pairs = int(input())
socks = list(map(int, input().split()))

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
