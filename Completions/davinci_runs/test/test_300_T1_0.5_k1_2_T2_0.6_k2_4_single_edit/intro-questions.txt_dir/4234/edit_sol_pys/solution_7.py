

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

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(a + b + c + d)
print(''.join(stack))
