#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the minimumBribes function below.
def minimumBribes(q):
    swaps = 0
    for i, p in enumerate(q):
        if p - (i + 1) > 2:
            print('Too chaotic')
            return
        for j in range(max(p-2, 0), i):
            if q[j] > p:
                swaps += 1
    print(swaps)
if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)
