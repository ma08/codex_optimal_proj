
#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the balancedSums function below.
def balancedSums(arr):
    if len(arr) == 1:
        return 'YES'
    sum_left = 0
    sum_right = 0
    for i in range(1, len(arr)):
        sum_right += arr[i]
    if sum_left == sum_right:
        return 'YES'
    for i in range(1, len(arr)):
        sum_left += arr[i-1]
        sum_right -= arr[i]
        if sum_left == sum_right:
            return 'YES'
    return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    T = int(input().strip())
    for T_itr in range(T):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = balancedSums(arr)
        fptr.write(result + '\n')
    fptr.close()
