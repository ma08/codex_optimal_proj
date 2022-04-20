

n = int(input())
s = input()

def is_good(s):
    """
    >>> is_good("good")
    True
    >>> is_good("bad")
    False
    >>> is_good("")
    True
    >>> is_good("a")
    True
    """
    if s == "":
        return True
    for i in range(0, len(s), 2):
        if s[i] == s[i+1]:
            return False
    return True

def remove_bad(s):
    """
    >>> remove_bad("good")
    'good'
    >>> remove_bad("bad")
    'bd'
    >>> remove_bad("aabc")
    'ab'
    >>> remove_bad("aaa")
    ''
    """
    if is_good(s):
        return s
    for i in range(0, len(s), 2):
        if s[i] == s[i+1]:
            return remove_bad(s[:i] + s[i+2:])

print(len(s) - len(remove_bad(s)))
print(remove_bad(s))