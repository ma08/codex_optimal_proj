#!/usr/bin/env python3

import sys
import numpy as np
n, k = map(int, sys.stdin.readline().split())
s = np.array(list(map(int, input().split())))
s_unique, s_counts = np.unique(s, return_counts=True)
s_indices = np.argsort(-s_counts)
t = s_unique[s_indices[:k]]
print(*t)
