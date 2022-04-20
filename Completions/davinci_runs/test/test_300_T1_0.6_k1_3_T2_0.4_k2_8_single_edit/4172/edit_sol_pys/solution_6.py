

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    min_diffs = []

    for i in range(k - 1, n):
        min_diffs.append(arr[i] - arr[i - k + 1])

    return min(min_diffs)

# Read in the input
n, k = map(int, input().split())
arr = []

for _ in range(n):
    arr_item = int(input())
    arr.append(arr_item)

result = maxMin(k, arr)

print(str(result) + '\n')
