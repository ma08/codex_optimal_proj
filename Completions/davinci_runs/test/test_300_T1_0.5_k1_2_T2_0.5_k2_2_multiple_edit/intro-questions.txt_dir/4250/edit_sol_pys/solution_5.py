
#https://www.hackerrank.com/challenges/np-shape-reshape/problem
#Solution:

#!/usr/bin/env python3

import sys
import numpy as np

n, m = map(int, input().split())
s = np.array(list(map(int, input().split())), int)

print(np.reshape(s, (n, m)))

t = s_unique[s_indices[:k]]
print(*t)
