

def simplify(string):
    """Simplify a string of lowercase letters.
    >>> simplify('abc')
    3
    >>> simplify('aaabbbccc')
    3
    >>> simplify('abbbcabb')
    3
    >>> simplify('abbbcabbb')
    4
    """
    return len(set(string))


def erase(string):
    """Find minimum number of letters to erase to simplify a string.
    >>> erase('abc')
    0
    >>> erase('aaabbbccc')
    0
    >>> erase('abbbcabb')
    1
    >>> erase('abbbcabbb')
    2
    """
    if len(string) < 3:
        return 0
    if simplify(string) < 3:
        return 0
    for i in range(len(string)):
        if simplify(string[:i] + string[i + 1:]) < 3:
            return 1
    return 2

print(erase(input()))
