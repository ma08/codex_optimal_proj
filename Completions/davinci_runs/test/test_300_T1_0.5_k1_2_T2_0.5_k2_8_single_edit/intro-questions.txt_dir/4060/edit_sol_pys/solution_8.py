

n = int(input())
s = input()

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

def count_brackets(s):
    open_ = 0
    close_ = 0
    for char in s:
        if char == '(':
            open_ += 1
        else:
            close_ += 1
    return open_, close_

def find_first_unpaired(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if not stack:
                return i
            stack.pop()
    if stack:
        return stack.pop()
    return -1


def count_changes(s):
    if is_regular(s):
        return 0
    open_, close_ = count_brackets(s)
    if open_ > close_:
        return open_ + close_
    if open_ == close_:
        return 0
    return open_ + close_ - abs(open_ - close_)

print(count_changes(s))
