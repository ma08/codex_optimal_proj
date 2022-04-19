#!/bin/python3

import os
import sys


n = int(input())
arr = list(map(int, input().rstrip().split()))

def largestRectangle(h):
    max_area = 0
    stack = []

    for i in range(len(h)):
        if len(stack) == 0 or h[stack[-1]] <= h[i]:
            stack.append(i)
        else:
            while len(stack) > 0 and h[stack[-1]] > h[i]:
                top = stack.pop()
                area = h[top] * (i - stack[-1] - 1 if len(stack) > 0 else i)
                max_area = max(max_area, area)
            stack.append(i)

    while len(stack) > 0:
        top = stack.pop()
        area = h[top] * (len(h) - stack[-1] - 1 if len(stack) > 0 else len(h))
        max_area = max(max_area, area)

    return max_area

result = largestRectangle(arr)

print(result)
