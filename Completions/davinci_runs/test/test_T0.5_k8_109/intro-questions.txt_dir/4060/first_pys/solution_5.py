

import sys

n = int(input())
s = input()

if s[0] == ')' or s[-1] == '(':
    print(0)
    sys.exit(0)

def is_regular(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

def change_type(s, i):
    return s[:i] + '(' if s[i] == ')' else ')' + s[i+1:]

count = 0
for i in range(len(s)):
    if not is_regular(s):
        count += 1
    s = change_type(s, i)

print(count)