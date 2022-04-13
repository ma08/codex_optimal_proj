
def simplicity(s):
    return len(set(s))

def min_erase(s):
    min_erase_ = len(s)
    for i in range(len(s)):
        s_ = s[:i] + s[i+1:]
        min_erase_ = min(min_erase_, len(s) - simplicity(s_))
    return min_erase_

print(min_erase(input()))
