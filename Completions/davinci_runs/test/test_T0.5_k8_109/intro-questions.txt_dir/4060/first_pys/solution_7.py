

def isRegular(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return True

n = int(input())
s = input()

count = 0
for i in range(n):
    if s[i] == '(':
        if not isRegular(s[:i] + ')' + s[i+1:]):
            count += 1
    else:
        if not isRegular(s[:i] + '(' + s[i+1:]):
            count += 1

print(count)