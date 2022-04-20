import math
import os
import random
import re
import sys


def min_instability(n, array):
    array.sort()
    min_instability = array[-1] - array[0]

    for i in range(1, n - 1):
        instability = array[i] - array[i - 1]
        if instability < min_instability:
            min_instability = instability
        instability = array[i + 1] - array[i]
        if instability < min_instability:
            min_instability = instability
    return min_instability

if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    print(min_instability(n, array))
