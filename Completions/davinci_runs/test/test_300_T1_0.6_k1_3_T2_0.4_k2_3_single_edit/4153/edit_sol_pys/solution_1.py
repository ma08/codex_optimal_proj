#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:20:59 2018

@author: yiqian
"""

from collections import deque

n = int(raw_input())
s = deque(raw_input())

count = 0
while s:
    if s[0] == '0':
        count += 1
        s.popleft()
    elif s[0] == '1':
        if len(s) > 1 and s[1] == '0':
            count += 1
            s.popleft()
            s.popleft()
        else:
            break

print(count)
