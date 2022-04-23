#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    n = len(arr)
    positive_count = 0
    negative_count = 0
    zero_count = 0
    for x in arr:
        if x > 0:
            positive_count += 1
        elif x < 0:
            negative_count += 1
        else:
            zero_count += 1
    print(positive_count / n)
    print(negative_count / n)
    print(zero_count / n)


if __name__ == '__main__':
    n = 6
    arr = [1, 0, -1, -1, -1, 0]

    plusMinus(arr)
