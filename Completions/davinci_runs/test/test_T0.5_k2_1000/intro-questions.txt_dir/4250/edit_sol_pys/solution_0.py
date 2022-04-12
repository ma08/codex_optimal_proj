
# Solution

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    i = 0
    while k > 0:
        k -= prices[i]
        i += 1
    return i - 1


t = s_unique[s_indices[:k]]
print(*t)
