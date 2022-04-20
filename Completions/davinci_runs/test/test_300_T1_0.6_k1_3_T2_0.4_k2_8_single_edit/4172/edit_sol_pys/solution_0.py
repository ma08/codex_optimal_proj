

# # SOLUTION
# # Read in the input
# n, k = map(int, input().split())
# a = list(map(int, input().split()))

# # Sort the array
# a.sort()

# # If k is 1, the output is 0
# if k == 1:
#     print(0)

# # If k is n, the output is the difference between the max and min
# elif k == n:
#     print(a[n - 1] - a[0])

# # Otherwise, for each i in range(k, n), get the difference between the max and min
# # and then find the minimum of all of those differences
# else:
#     min_diffs = []

#     for i in range(k - 1, n):
#         min_diffs.append(a[i] - a[i - k + 1])

#     print(min(min_diffs))

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count = 0
    i = 0
    while i < len(c) - 1:
        if i < len(c) - 2 and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
