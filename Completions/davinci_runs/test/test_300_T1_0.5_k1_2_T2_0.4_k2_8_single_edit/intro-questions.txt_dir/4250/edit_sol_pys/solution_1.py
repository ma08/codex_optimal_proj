
#!/usr/bin/env python3

import sys
import numpy as np

n, k = map(int, input().split())
s = np.array(list(map(int, input().split())), dtype=np.int64)

s_unique, s_counts = np.unique(s, return_counts=True, axis=0)
s_indices = np.argsort(-s_counts, axis=0)

t = s_unique[s_indices[:k]]
print(*t)
