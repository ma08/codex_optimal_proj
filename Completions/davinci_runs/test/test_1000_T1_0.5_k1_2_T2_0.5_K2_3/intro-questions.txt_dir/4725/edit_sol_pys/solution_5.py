

def simplicity(s):
    return len(set(s))


def min_erasure(s):
    min_erasure = len(s)
    for i in range(len(s)):
        s_ = s[:i] + s[i + 1:]
        min_erasure = min(min_erasure, len(s) - simplicity(s_))
    return min_erasure


print(min_erasure(input()))
