

def simplify(string):
    """Simplify a string of lowercase letters.

    >>> simplify('aaabbbccc')
    3
    >>> simplify('abcd')
    4
    """
    return len(set(string))

def erase(string):
    """Find minimum number of letters to erase to simplify a string.

    >>> erase('aaabbbccc')
    0
    >>> erase('aaabbbcccddd')
    1
    >>> erase('aaabbbcccddde')
    2
    >>> erase('aaabbbcccdddeee')
    3
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
