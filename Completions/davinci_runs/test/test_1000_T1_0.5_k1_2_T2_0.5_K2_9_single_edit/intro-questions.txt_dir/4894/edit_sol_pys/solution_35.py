def check_braces(string):
    stack = []
    opening = {'{', '[', '('}
    pairs = {'}': '{', ']': '[', ')': '('}
    for char in string:
        if char in opening:
            stack.append(char)
        elif char in pairs:
            if stack.pop() != pairs[char]:
                return False
    return len(stack) == 0


print(check_braces('{}[]()'))
print(check_braces('{[}]'))
print(check_braces('{[()]}'))
print(check_braces('{[(])}'))
print(check_braces('{{[[(())]]}}'))
