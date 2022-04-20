

import numpy as np

# read input
n, m = map(int, input().split())
a = np.empty((n, m))
for i in range(n):
    a[i] = np.array(input().split(), dtype=np.int)

# find the maximum difference between elements in the same row
k = np.zeros(n)
for i in range(n):
    k[i] = max(a[i]) - min(a[i])

# find the minimum difference between rows
k_min = min(np.diff(np.sort(k)))

# output
print(int(k_min))