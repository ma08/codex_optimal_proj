#!/bin/python3


import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_count = 0
    oranges_count = 0
    for apple in apples:
        if (a + apple) >= s and (a + apple) <= t:
            apples_count += 1
    for orange in oranges:
        if (b + orange) >= s and (b + orange) <= t:
            oranges_count += 1
    print(apples_count)
    print(oranges_count)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
