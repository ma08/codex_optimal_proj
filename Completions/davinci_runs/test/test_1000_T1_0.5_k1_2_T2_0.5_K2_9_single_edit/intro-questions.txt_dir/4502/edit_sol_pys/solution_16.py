#!/usr/bin/env python3

import sys

n = int(input())
a = list(map(int, input().split()))

stack = []
for i in a:
    if len(stack) == 0:
        print('-1')
    elif i == stack[-1]:
        stack.pop()
    else:
        print('-1')
    stack.append(i)

