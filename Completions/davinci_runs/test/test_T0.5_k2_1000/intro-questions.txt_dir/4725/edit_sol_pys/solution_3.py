
def min_erase(s):
    min_erase = len(s)
    for i in range(len(s)):
        s_ = s[:i] + s[i + 1:]
        min_erase = min(min_erase, len(s) - simplicity(s_) - 1)

    return min_erase

def simplicity(s):
    return len(set(s))

print(min_erase(input()))
