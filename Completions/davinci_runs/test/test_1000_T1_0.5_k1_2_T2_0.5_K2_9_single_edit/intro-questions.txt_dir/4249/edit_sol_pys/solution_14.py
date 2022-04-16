import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxSum = -63
    for i in range(1, 5):
        for j in range(1, 5):
            sum = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i][j] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            if sum > maxSum:
                maxSum = sum
    return maxSum


cups = 0
pages = 0
days = 0

while cups < n:
    pages += a[cups]
    days += 1
    cups += 1
    if pages >= m:
        break
    if cups < n:
        pages -= days - 1

if pages < m:
    days = -1

print(days)
