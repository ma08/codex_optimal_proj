

def find_index(s):
    for i in range(len(s)):
        if s[i] == ')':
            return i
    return -1

def count_open(s):
    c = 0
    for i in range(len(s)):
        if s[i] == '(':
            c += 1
    return c

def min_changes(s):
    index = find_index(s)
    if index == -1:
        return 0
    return count_open(s[index:])
