

def is_substring(a, b):
    """
    >>> is_substring('a', 'a')  # doctest: +NORMALIZE_WHITESPACE
    True
    >>> is_substring('ab', 'a')  # doctest: +NORMALIZE_WHITESPACE
    False
    >>> is_substring('a', 'ab')  # doctest: +NORMALIZE_WHITESPACE
    True
    >>> is_substring('a', 'abab')  # doctest: +NORMALIZE_WHITESPACE
    True
    >>> is_substring('ab', 'abab')  # doctest: +NORMALIZE_WHITESPACE
    True
    >>> is_substring('abab', 'abab')  # doctest: +NORMALIZE_WHITESPACE
    True
    >>> is_substring('abab', 'ab')  # doctest: +NORMALIZE_WHITESPACE
    False
    >>> is_substring('ab', 'ababab')  # doctest: +NORMALIZE_WHITESPACE
    True
    >>> is_substring('abcabcabcabcabcabcabcabcabcabcabcab', 'a')  # doctest: +NORMALIZE_WHITESPACE
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
    >>> reorder(['a', 'aba', 'abacaba', 'ba', 'aba'])  # doctest: +NORMALIZE_WHITESPACE
    ['a', 'ba', 'aba', 'aba', 'abacaba']
    >>> reorder(['a', 'abacaba', 'ba', 'aba', 'abab'])  # doctest: +NORMALIZE_WHITESPACE
    False
    >>> reorder(['qwerty', 'qwerty', 'qwerty'])  # doctest: +NORMALIZE_WHITESPACE
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
