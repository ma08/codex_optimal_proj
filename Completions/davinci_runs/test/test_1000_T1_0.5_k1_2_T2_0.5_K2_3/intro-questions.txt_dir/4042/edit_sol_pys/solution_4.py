

import sys
import math

def find_min_max(arr):
    min_list = []
    max_list = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                a = arr[i] - arr[j]
                if a > 0:
                    min_list.append(a)
                else:
                    max_list.append(a)
    min_list.sort()
    max_list.sort()
    return min_list[0], max_list[-1]

def find_min_max_2(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in range(1, len(arr)):
        if min_val > arr[i]:
            min_val = arr[i]
        if max_val < arr[i]:
            max_val = arr[i]
    return max_val - min_val

def find_min_max_3(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in range(1, len(arr)):
        if min_val > arr[i]:
            min_val = arr[i]
        if max_val < arr[i]:
            max_val = arr[i]
    return min_val, max_val

def find_min_max_4(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in arr:
        if min_val > i:
            min_val = i
        if max_val < i:
            max_val = i
    return max_val - min_val

def find_min_max_5(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in arr:
        if min_val > i:
            min_val = i
        if max_val < i:
            max_val = i
    return min_val, max_val

def find_min_max_6(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in arr:
        if min_val > i:
            min_val = i
        if max_val < i:
            max_val = i
    return max_val - min_val

def find_min_max_7(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in arr:
        if min_val > i:
            min_val = i
        if max_val < i:
            max_val = i
    return min_val, max_val

def find_min_max_8(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in arr:
        if min_val > i:
            min_val = i
        if max_val < i:
            max_val = i
    return max_val - min_val

def find_min_max_9(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in arr:
        if min_val > i:
            min_val = i
        if max_val < i:
            max_val = i
    return min_val, max_val

def find_min_max_10(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in arr:
        if min_val > i:
            min_val = i
        if max_val < i:
            max_val = i
    return max_val - min_val

def find_min_max_11(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in arr:
        if min_val > i:
            min_val = i
        if max_val < i:
            max_val = i
    return min_val, max_val

def find_min_max_12(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in arr:
        if min_val > i:
            min_val = i
        if max_val < i:
            max_val = i
    return max_val - min_val

def find_min_max_13(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in arr:
        if min_val > i:
            min_val = i
        if max_val < i:
            max_val = i
    return min_val, max_val

def find_min_max_14(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in arr:
        if min_val > i:
            min_val = i
        if max_val < i:
            max_val = i
    return max_val - min_val

def find_min_max_15(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in arr:
        if min_val > i:
            min_val = i
        if max_val < i:
            max_val = i
    return min_val, max_val

def find_min_max_16(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in arr:
        if min_val > i:
            min_val = i
        if max_val < i:
            max_val = i
    return max_val - min_val

def find_min_max_17(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in arr:
        if min_val > i:
            min_val = i
        if max_val < i:
            max_val = i
    return min_val, max_val

def find_min_max_18(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in arr:
        if min_val > i:
            min_val = i
        if max_val < i:
            max_val = i
    return max_val - min_val

def find_min_max_19(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in arr:
        if min_val > i:
            min_val = i
        if max_val < i:
            max_val = i
    return min_val, max_val

def find_min_max_20(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in arr:
        if min_val > i:
            min_val = i
        if max_val < i:
            max_val = i
    return max_val - min_val
