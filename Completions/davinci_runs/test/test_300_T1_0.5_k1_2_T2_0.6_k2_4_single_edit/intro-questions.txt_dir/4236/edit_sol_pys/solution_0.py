

def is_valid(s):
    stack = []
    for i in s:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
    return stack == []

print(is_valid("[()]"))
print(is_valid("[(])"))
