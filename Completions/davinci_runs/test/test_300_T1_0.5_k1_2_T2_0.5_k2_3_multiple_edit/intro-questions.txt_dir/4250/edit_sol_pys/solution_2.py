
#!/usr/bin/env python3
# Solution


import sys
import numpy as np

n, k = map(int, input().split())
a = np.array(list(map(int, input().split())))

a_unique, a_counts = np.unique(a, return_counts=True)
a_indices = np.argsort(-a_counts)

a_unique = a_unique[a_indices[:k]]
print(*a_unique)
