
def simplicity(s):
    return len(s) - len(set(s))

def min_erase(s):
    min_erase = len(s) - len(set(s))
    for i in range(len(s)):
        s_ = s[:i] + s[i+1:]
        min_erase = min(min_erase, simplicity(s_))
    return min_erase

print(min_erase(input()))
