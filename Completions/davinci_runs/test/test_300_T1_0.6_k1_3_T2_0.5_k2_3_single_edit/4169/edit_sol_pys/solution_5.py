

import sys
import math

#-----Constants-----

#-----Input and Setup-----
n, m = map(int, input().split())
stores = []

for i in range(n):
    a, b = map(int, input().split())
    stores.append([a, b])

#-----Solve-----

for i in range(n):
    print(stores[i])
#-----Display-----
