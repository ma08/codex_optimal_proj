

import sys
import math

def read_ints():
  temp = input().split()
  temp = [int(t) for t in temp]
  return temp

def read_tuple(convert_func):
  temp = input().split()
  temp = [convert_func(t) for t in temp]
  return tuple(temp)

def read_int():
  temp = input().split()
  return int(temp[0])

def max_diff(a, b):
  return max(a) - min(a)

def solve():
  n, m = read_tuple(int)
  a = read_ints()
  segments = [read_tuple(int) for _ in range(m)]

  # print(n, m)
  # print(a)
  # print(segments)

  max_diffs = [0] * m
  for i in range(m):
    segment = segments[i]
    l, r = segment
    max_diffs[i] = max_diff(a[l-1:r])

  # print(max_diffs)

  max_diff_val = max(max_diffs)
  max_diff_indices = []
  for i in range(m):
    if max_diffs[i] == max_diff_val:
      max_diff_indices.append(i+1)

  print(max_diff_val)
  print(len(max_diff_indices))
  print(' '.join([str(i) for i in max_diff_indices]))

solve()