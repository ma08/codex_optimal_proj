import sys
from collections import deque
from collections import defaultdict
import numpy as np
import math
from copy import deepcopy
import itertools
sys.setrecursionlimit(2000000)



x.sort()

dist = []
for i in range(N):
    dist.append(abs(X - x[i]))
dist.sort()

ans = 0
for i in range(1, N):
    ans = max(ans, (dist[i] - dist[i - 1]) // 2)

print(ans)
