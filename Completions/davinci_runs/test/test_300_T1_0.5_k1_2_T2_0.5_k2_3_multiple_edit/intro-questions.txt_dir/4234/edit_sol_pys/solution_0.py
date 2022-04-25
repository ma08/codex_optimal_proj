import sys

n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip().split(' ')

stack = []
for i in s:
    stack.append(i)
    if len(stack) > 1 and stack[-1] == stack[-2]:
        stack.pop()
        stack.pop()

print(n - len(stack))
print(''.join(stack))
