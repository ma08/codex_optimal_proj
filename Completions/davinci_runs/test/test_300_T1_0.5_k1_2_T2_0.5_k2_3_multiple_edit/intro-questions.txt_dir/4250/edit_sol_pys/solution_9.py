

# Solution

#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

if __name__ == '__main__':
    n, k = map(int, input().split())
    s = np.array(list(map(int, input().split())))

    s_unique, s_counts = np.unique(s, return_counts=True)
    s_indices = np.argsort(-s_counts)

t = s_unique[s_indices[:k]]
print(*t)
