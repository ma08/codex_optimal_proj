

import numpy as np

N, K = map(int, input().split())

fruit = np.array(list(map(int, input().split())))
fruit = np.sort(fruit)

print(sum(fruit[:K]))
