import os
import csv
import sys
import math
from collections import Counter


def get_min_pockets(n, arr):
  d = Counter(arr)
  return len(d)

n = int(input())
arr = list(map(int, input().split()))
print(get_min_pockets(n, arr), end='')
