

#Solution
import sys
#!/bin/python3


import numpy as np

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

a = np.array(a)

unique_elements, counts_elements = np.unique(a, return_counts=True)
a_indices = np.argsort(-counts_elements)[:k]

print(*unique_elements[a_indices])
