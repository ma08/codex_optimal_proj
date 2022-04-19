
import numpy as np
n = 5
a = np.zeros((n,n),dtype=int)
for i in range(n):
    for j in range(n):
        a[i][j] = int(input())
print(a)
