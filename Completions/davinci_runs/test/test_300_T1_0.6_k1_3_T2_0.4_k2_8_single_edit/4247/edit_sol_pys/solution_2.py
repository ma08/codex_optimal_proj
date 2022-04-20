

import math
import numpy as np
import matplotlib.pyplot as plt

n = int(input())
p = list(map(int, input().split()))
# n = 5
# p = [1,3,5,4,2]

x = np.arange(1,n+1,1)
y = np.array(p)

plt.plot(x,y)
plt.show()
