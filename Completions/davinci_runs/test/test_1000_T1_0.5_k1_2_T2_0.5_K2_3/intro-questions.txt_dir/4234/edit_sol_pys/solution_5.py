#!/usr/bin/python2.7

import sys

n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip().split(' ')

stack = [0]
for i in s:
    if len(stack) > 1:
        if i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    else:
        stack.append(i)

print(len(stack) - 1)
