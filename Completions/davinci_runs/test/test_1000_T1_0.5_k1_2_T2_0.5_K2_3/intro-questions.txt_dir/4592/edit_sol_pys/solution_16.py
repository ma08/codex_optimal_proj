

import sys

def min_max(arr):
    min_val = sys.maxsize
    max_val = -sys.maxsize

    for i in range(len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
        if arr[i] > max_val:
            max_val = arr[i]
    return min_val, max_val

arr = [int(x) for x in input().split()]

min_val, max_val = min_max(arr)

print(min_val, max_val)
