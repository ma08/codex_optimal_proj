#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:21:04 2017
@author: tz
"""
from itertools import product

N, T, M = map(int, input().split())
print(len(set(product(range(N), range(T), range(M))))) # list(product(range(N), range(T), range(M)))
