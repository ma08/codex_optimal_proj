

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

# count the number of open and closed brackets and the number of changes
def count_changes(s):
    open_ = s.count('(')
    close_ = s.count(')')
    if open_ == close_:
        return 0
    if open_ > close_:
        return open_ - close_
    return close_ - open_


print(count_changes(s))
