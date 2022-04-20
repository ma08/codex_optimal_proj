#!/bin/python3


import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    min_unfair = float('inf')
    for i in range(0, len(arr) - k + 1):
        min_unfair = min(min_unfair, arr[i + k - 1] - arr[i])
    return min_unfair

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

# Read in the input
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Sort the array
a.sort()

# If k is 1, the output is 0
if k == 1:
    print(0)

# If k is n, the output is the difference between the max and min
elif k == n:
    print(a[n - 1] - a[0])

# Otherwise, for each i in range(k, n), get the difference between the max and min
# and then find the minimum of all of those differences
else:
    min_diffs = []

    for i in range(k - 1, n):
        min_diffs.append(a[i] - a[i - k + 1])

    print(min(min_diffs))
