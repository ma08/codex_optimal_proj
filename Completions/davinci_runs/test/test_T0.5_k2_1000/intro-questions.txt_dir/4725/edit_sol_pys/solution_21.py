
def simplicity(s):
    return len(set(s))

def min_erase_count(s):
    min_erase_count = len(s)
    for i in range(len(s)):
        s_ = s[:i] + s[i+1:]
        min_erase_count = min(min_erase_count, len(s) - simplicity(s_))
    return min_erase_count

print(min_erase_count(input()))
