

# SOLUTION

#!/usr/bin/python

import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline()

stack = []

for i in range(n):
    if s[i] == '(':
        stack.append('(')
    else:
        if len(stack) == 0:
            stack.append(')')
        else:
            stack.pop()

print(len(stack))