

def simplicity(s):
    return len(set(s))

def min_erase_count(s):
    min_count = len(s)
    for i in range(len(s)):
        s_ = s[:i] + s[i+1:]
        min_count = min(min_count, len(s) - simplicity(s_))
    return min_count

print(min_erase_count(input()))
