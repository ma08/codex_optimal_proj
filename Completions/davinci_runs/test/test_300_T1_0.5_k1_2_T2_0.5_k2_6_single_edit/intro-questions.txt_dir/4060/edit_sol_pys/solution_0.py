
n = int(input())
s = input()

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

def count_changes(s):
    open_, close_ = count_brackets(s)
    if open_ == close_:
        return 0
    return open_ + close_ - abs(open_ - close_)

print(count_changes(s))
