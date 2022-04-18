
import copy
import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

stack = copy.deepcopy(s)

for i in range(n):
    if len(stack) > 1 and stack[i] == stack[i-1]:
        stack = stack[:i-1] + stack[i+1:]
        i -= 2

print(len(stack))
print(stack)
