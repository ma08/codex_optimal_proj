#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 18:16:50 2020


@author: karanwaghela
"""

def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


def max_subarray_circular(A):
    max_subarray_val = max_subarray(A)
    
    circular_sum = 0
    for i in range(len(A)):
        circular_sum += A[i]
        A[i] = -A[i]
    circular_sum += max_subarray(A)
    
    if circular_sum > max_subarray_val and circular_sum != 0:
        return circular_sum
    else:
        return max_subarray_val


if __name__ == "__main__":
    A = [2, -2, 2, 7, 8, 0]
    print(max_subarray_circular(A))
