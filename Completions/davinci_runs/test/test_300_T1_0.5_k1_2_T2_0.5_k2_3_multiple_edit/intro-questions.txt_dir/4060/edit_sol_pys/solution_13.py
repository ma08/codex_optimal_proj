

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

# count the number of opening and closing brackets
def count_brackets(s):
    open_ = 0
    close_ = 0
    for char in s:
        if char == '(':
            open_ += 1
        else:
            close_ += 1
    return open_, close_

def count_changes(s):
    if is_regular(s):
        return 0
    open_, close_ = count_brackets(s)
    return open_ + close_ - 2 * min(open_, close_)

print(count_changes(s))
