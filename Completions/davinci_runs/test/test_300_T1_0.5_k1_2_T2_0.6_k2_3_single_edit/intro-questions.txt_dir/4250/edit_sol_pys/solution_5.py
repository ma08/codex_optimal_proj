

#Solution

#!/bin/python3

import numpy as np

n, m = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)

s_unique, s_counts = np.unique(s, return_counts=True)
s_indices = np.argsort(-s_counts)

t = s_unique[s_indices[:k]]
print(*t)
