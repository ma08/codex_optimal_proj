
import numpy as np
import math

n = int(input())
x = np.array(list(map(int, input().split())))
u = np.mean(x)
s = np.std(x)
x_norm = (x - u) / s
print(np.sqrt(n))
print("{:.2f}".format(np.std(x_norm, ddof=1)))
