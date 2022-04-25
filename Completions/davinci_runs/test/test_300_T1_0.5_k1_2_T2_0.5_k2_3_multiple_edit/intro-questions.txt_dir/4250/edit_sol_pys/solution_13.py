
#Solution

#!/bin/python3


import numpy as np

n, k = map(int, input().strip().split(' '))
s = np.array(list(map(int, input().strip().split(' '))))

s_unique, s_counts = np.unique(s, return_counts=True)
s_indices = np.argsort(-s_counts)[:k]

print(*s_unique[s_indices])
