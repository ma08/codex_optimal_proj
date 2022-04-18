

def simplicity(s):
    return len(set(s))

def min_erase(s):
    m = len(s)
    for i in range(len(s)):
        s_ = s[:i] + s[i+1:]
        m = min(m, len(s) - simplicity(s_))
    return m

print(min_erase(input()))
