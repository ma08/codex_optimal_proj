
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 20:59:28 2020
@author: kushal
"""


## Read input as specified in the question.

## Print output as specified in the question.

def min_price(arr):
    total = sum(arr)
    max_val = max(arr)
    if (total - max_val) >= max_val:
        return max_val
    else:
        return total // len(arr)


if __name__ == '__main__':
    q = int(input("enter the number of test cases: "))
    for i in range(q):
        n = int(input("enter the number of elements: "))
        arr = list(map(int, input("enter the elements: ").split()))
        print(min_price(arr))
