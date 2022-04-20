#!/usr/bin/env python3

import sys
import numpy as np

n, k = map(int, input().split())
arr = np.array(list(map(int, input().split())))

unique, counts = np.unique(arr, return_counts=True)
indices = np.argsort(-counts)

t = s_unique[s_indices[:k]]
print(*t)
