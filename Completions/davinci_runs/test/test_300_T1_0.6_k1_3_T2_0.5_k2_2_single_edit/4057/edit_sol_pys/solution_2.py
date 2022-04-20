#!/bin/python3

import math
import os
import random
import re
import sys


# n = int(input())
# arr = list(map(int, input().split()))

n = 6
arr = [1, 2, 4, 3, 3, 2, 3]

def get_min_pockets(n, arr):
  d = {}
  for i in arr:
    if i in d:
      d[i] += 1
    else:
      d[i] = 1
  return len(d.keys())

print(get_min_pockets(n, arr))
