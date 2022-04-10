

import sys

# s = sys.stdin.readline().strip()
# n = len(s)

s = '(((()'
n = len(s)

stack = []

for i in range(n):
    if s[i] == '(':
        stack.append(s[i])
    else:
        if len(stack) == 0:
            stack.append(s[i])
        else:
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s[i])

# print(stack)

if len(stack) == 0:
    print(n)
else:
    count = 0
    for i in range(len(stack)):
        if stack[i] == '(':
            count += 1
    print(count)