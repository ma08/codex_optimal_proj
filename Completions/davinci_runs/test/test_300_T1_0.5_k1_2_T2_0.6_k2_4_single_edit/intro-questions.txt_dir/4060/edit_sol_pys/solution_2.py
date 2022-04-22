

n = int(input())
s = input()

# check if the sequence is already regular
def is_regular(sequence):
    stack = []
    for char in sequence:
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
def count_brackets(sequence):
    open_ = 0
    close_ = 0
    for char in sequence:
        if char == '(':
            open_ += 1
        else:
            close_ += 1
    return open_, close_

def count_changes(sequence):
    if is_regular(sequence):
        return 0
    open_, close_ = count_brackets(sequence)
    if open_ == close_:
        return 0
    return open_ + close_ - abs(open_ - close_)

print(count_changes(s))
