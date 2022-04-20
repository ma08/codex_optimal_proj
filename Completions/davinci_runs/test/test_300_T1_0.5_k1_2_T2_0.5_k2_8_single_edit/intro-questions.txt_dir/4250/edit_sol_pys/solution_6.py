
#!/usr/bin/env python3

import numpy as np

n, k = map(int, input().strip().split(' '))
s = np.array(input().strip().split(' '), dtype=int)

unique, counts = np.unique(s, return_counts=True)
indices = np.argsort(-counts)

print(' '.join(unique[indices[:k]].astype(str)))
