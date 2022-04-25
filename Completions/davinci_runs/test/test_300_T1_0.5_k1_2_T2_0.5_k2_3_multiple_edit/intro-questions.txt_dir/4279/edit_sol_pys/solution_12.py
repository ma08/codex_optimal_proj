#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(n):
    if n % 4 == 0:
        return 'Yes'
    else:
        return 'No'


if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()
