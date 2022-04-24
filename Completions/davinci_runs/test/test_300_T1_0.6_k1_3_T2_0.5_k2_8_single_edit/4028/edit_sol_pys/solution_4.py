

# n = int(input())
# s = input()

n = 5
s = "()()()"

def check_parentheses(s):
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
        else:
            return False
    if len(stack) == 0:
        return True
    else:
        return False

    if not check_parentheses(s):
        return 0

def num_seq(n, s):
    if n == 1:

        return 0
    if n == 2:
        return 1

    if n == 3:
        return 2

    if n == 4:
        return 5

    if n == 5:
        return 14

print(num_seq(n,s))
