

def is_substring(a, b):
    """
    >>> is_substring('a', 'a')
    True
    >>> is_substring('ab', 'a')
    False
    >>> is_substring('a', 'ab')
    True

    """
    if a == b:
        return True
    if len(a) > len(b):
        return False
    start = 0
    while True:
        if a == b[start:start+len(a)]:
            return True
        start += 1
        if start > len(b) - len(a):
            return False

def reorder(strings):
    """
    >>> reorder(['a', 'aba', 'abacaba', 'ba', 'aba'])
    ['a', 'ba', 'aba', 'aba', 'abacaba']
    >>> reorder(['a', 'abacaba', 'ba', 'aba', 'abab'])
    False
    >>> reorder(['qwerty', 'qwerty', 'qwerty'])
    ['qwerty', 'qwerty', 'qwerty']
    """
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if is_substring(strings[j], strings[i]):
                continue
            if not is_substring(strings[i], strings[j]):
                return False
    return strings

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    n = int(input())
    strings = []
    for _ in range(n):
        strings.append(input())
    result = reorder(strings)
    if result:
        print("YES")
        for s in result:
            print(s)
    else:
        print("NO")
