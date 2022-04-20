

import numpy as np

n, m = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)

print(np.add(a, b), np.subtract(a, b), np.multiply(a, b), np.floor_divide(a, b), np.mod(a, b), np.power(a, b), sep='\n')
