

n = int(input())
s = input()

# check if the sequence is already regular
def is_regular(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    if stack:
        return False
    return True

# count the number of open and close brackets
def count_brackets(s):
    open_brackets = 0
    close_brackets = 0
    for char in s:
        if char == '(':
            open_brackets += 1
        else:
            close_brackets += 1
    return open_brackets, close_brackets

def count_changes(s):
    if is_regular(s):
        return 0
    open_brackets, close_brackets = count_brackets(s)
    if open_brackets == close_brackets:
        return 0
    return open_brackets + close_brackets - abs(open_brackets - close_brackets)

print(count_changes(s))
