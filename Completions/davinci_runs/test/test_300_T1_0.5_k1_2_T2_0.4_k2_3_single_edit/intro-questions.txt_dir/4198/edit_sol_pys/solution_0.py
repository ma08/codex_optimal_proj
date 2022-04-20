

import numpy as np

N, M = list(map(int, input().split()))

A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

A = np.sort(A)
B = np.sort(B)

print(np.sum(A[-M:]))
