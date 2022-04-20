

import math
import numpy as np

n = int(input())
a = np.array([int(i) for i in input().split()])

# print(np.mean(a))
# print(np.median(a))
# print(int(np.argmax(np.bincount(a))))

print(np.mean(a))
print(np.median(a))
print(int(np.argmax(np.bincount(a))))
