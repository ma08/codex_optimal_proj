

import sys
from collections import deque
sys.setrecursionlimit(10**6)

for i in range(n):
    if times[i][0] <= times[i][1]:
        print("Edward is right")
        quit()

print("Gunilla has a point")
