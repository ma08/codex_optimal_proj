
def is_substring(a, b):
    """
    >>> is_substring('a', 'a')
    True
    >>> is_substring('ab', 'a')
    False
    >>> is_substring('a', 'ab')
    True
    >>> is_substring('a', 'abab')
    True
    >>> is_substring('ab', 'abab')
    True
    >>> is_substring('abab', 'abab')
    True
    >>> is_substring('abab', 'ab')
    False
    >>> is_substring('ab', 'ababab')
    True
    >>> is_substring('abcabcabcabcabcabcabcabcabcabcabcab', 'a')
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
    >>> reorder(['a', 'aba', 'abacaba', 'ba', 'aba'])[0]
    'a'
    >>> reorder(['a', 'aba', 'abacaba', 'ba', 'aba'])[1]
    'ba'
    >>> reorder(['a', 'aba', 'abacaba', 'ba', 'aba'])[2]
    'aba'
    >>> reorder(['a', 'aba', 'abacaba', 'ba', 'aba'])[3]
    'aba'
    >>> reorder(['a', 'aba', 'abacaba', 'ba', 'aba'])[4]
    'abacaba'
    >>> reorder(['a', 'abacaba', 'ba', 'aba', 'abab']) is False
    True
    >>> reorder(['qwerty', 'qwerty', 'qwerty'])[0]
    'qwerty'
    >>> reorder(['qwerty', 'qwerty', 'qwerty'])[1]
    'qwerty'
    >>> reorder(['qwerty', 'qwerty', 'qwerty'])[2]
    'qwerty'
    """
    for i in range(len(strings)-1):
        for j in range(i+1, len(strings)-1):
            if not is_substring(strings[i], strings[j]) and not is_substring(strings[j], strings[i]):
                return False, []
    strings.sort(key=len)
    return True, strings

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    n = int(input())
    strings = []
    for _ in range(n):
        strings.append(input())
    result, strings = reorder(strings)
    if result:
        print("YES")
        for s in result:
            print(s)
    else:
        print("NO")
