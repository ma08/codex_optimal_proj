#!/usr/bin/python
import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

stack = []
for i in range(n):
    stack.append(s[i])
    if len(stack) > 1 and stack[-1] == stack[-2]:
        stack.pop()
        stack.pop()

print(n - len(stack))
print(''.join(stack))
