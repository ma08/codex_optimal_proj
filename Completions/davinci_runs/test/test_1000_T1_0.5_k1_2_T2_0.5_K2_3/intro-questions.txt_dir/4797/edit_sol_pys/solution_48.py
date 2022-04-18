n = input()
stack = []
for c in n:
    if c == '<':
        stack.pop()
    else:
        stack.append(c)
print(''.join(stack))
