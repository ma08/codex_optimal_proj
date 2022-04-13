#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])
    print(str(min_sum) + " " + str(max_sum))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
