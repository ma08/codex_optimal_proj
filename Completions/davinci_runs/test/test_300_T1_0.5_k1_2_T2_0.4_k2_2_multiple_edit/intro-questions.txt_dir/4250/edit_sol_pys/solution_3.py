

#Solution 1 (numpy)

#!/usr/bin/env python3

import numpy as np

n, k = map(int, input().split()) # input n and k
s = np.array(list(map(int, input().split()))) # input s

s_unique, s_counts = np.unique(s, return_counts=True)
s_indices = np.argsort(-s_counts)

t = s_unique[s_indices[:k]]
print(*t)
