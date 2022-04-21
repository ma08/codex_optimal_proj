#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()


#-----Solution-----

#This is a greedy algorithm.
#The idea is to greedily multiply by 3 until the number is greater than m.
#Then, multiply by 2 as many times as possible, until the number is greater than m.
#If the number is not m, then the answer is -1.

n, m = map(int, input().split())

if n == m:
    print(0)
elif m % 2 == 0 and n % 2 == 1:
    print(-1)
else:
    steps = 0
    while n < m:
        if n * 3 <= m:
            n *= 3
        else:
            n *= 2
        steps += 1
    if n == m:
        print(steps)
    else:
        print(-1)
