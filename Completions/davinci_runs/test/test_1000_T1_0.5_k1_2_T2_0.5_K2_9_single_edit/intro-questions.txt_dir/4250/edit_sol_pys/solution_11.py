
#!/usr/bin/env python3

import numpy as np

n, k = map(int, input().split())
s = np.array(input().split(), int)

unique, counts = np.unique(s, return_counts=True)
indices = np.argsort(-counts)

t = s_unique[s_indices[:k]]
print(*t)
