


#!/usr/bin/env python3

import sys
import numpy as np

n, m = map(int, input().split())
a = np.array(list(map(int, input().split())))

a_unique, a_counts = np.unique(a, return_counts=True)
a_indices = np.argsort(-a_counts)

b = a_unique[a_indices[:m]]
print(*b)
