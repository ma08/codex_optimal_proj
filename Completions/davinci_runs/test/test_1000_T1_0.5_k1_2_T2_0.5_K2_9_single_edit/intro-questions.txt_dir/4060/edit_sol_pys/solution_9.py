

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

# count the number of open and closed brackets
def count_brackets(s):
    open_ = 0
    closed_ = 0
    for char in s:
        if char == '(':
            open_ += 1
        else:
            closed_ += 1
    return open_, closed_

def count_changes(s):
    if is_regular(s):
        return 0
    open_, closed_ = count_brackets(s)
    if open_ == closed_:
        return 0
    return open_ + closed_ - abs(open_ - closed_)

print(count_changes(s))
