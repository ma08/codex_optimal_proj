

n = int(input())
s = [input() for _ in range(n)]

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
    open_ = 0
    close_ = 0
    for char in s:
        if char == '(':
            open_ += 1
        else:
            close_ += 1
    return open_, close_

def count_changes(seq):
    if is_regular(seq):
        return 'YES'
    open_, close_ = count_brackets(seq)
    if open_ != close_:
        return 'NO'
    return 'YES'

for seq in s:
    print(count_changes(seq))
