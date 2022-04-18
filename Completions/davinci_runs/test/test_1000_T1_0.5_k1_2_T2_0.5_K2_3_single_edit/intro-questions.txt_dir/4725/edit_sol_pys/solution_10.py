

def simplicity(s):
    return len(set(s))

def min_erase(s, n):
    min_erase = len(s)
    for i in range(n):
        s_ = s[:i] + s[i+1:]
        min_erase = min(min_erase, len(s) - simplicity(s_))
    return min_erase

s = input()
print(min_erase(s, len(s)))
