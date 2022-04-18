from collections import deque

import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

stack = deque()
for i in range(n):
    stack.append(s[i])
    if len(stack) > 1 and stack[0] == stack[1]:
        stack.popleft()
        stack.popleft()

print(n - len(stack))
print(''.join(stack))
