

def simplify(s, i):
    """Simplify a string of lowercase letters."""
    return len(set(s[:i] + s[i + 1:]))

def erase(s):
    """Find minimum number of letters to erase to simplify a string."""
    if len(s) < 3:
        return 0
    if simplify(s, 0) < 3:
        return 0
    for i in range(len(s)):
        if simplify(s, i) < 3:
            return 1
    return 2

print(erase(input()))
