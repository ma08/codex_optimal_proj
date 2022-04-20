

n = int(input())
s = input()

# n = 5
# s = "()))()"

def num_seq(n, s):
    stack = []
    for i in range(n):
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')':
            if len(stack) == 0:
                return 0
            else:
                stack.pop()
    if len(stack) == 0:
        return 1
    return 0

print(num_seq(n,s))
