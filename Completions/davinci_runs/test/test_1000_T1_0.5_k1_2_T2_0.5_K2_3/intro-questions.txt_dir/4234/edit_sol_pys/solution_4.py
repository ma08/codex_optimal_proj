import sys

n = int(input())
s = input().strip()

stack = []
for i in range(n):
    stack.append(s[i])
    if len(stack) > 1 and stack[-1] == stack[-2]:
        stack.pop()
        stack.pop()

print(n - len(stack), ''.join(stack))
