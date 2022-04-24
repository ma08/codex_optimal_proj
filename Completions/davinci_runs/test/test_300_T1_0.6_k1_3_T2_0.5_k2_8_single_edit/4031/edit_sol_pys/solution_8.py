

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
    >>> is_substring('ab', 'abab')
    False
    >>> is_substring('ab', 'ababab')
    True
    >>> is_substring('abcabcabcabcabcabcabcabcabcabcabcab', 'a')
    True
    >>> is_substring('a', 'b')
    False
    """
    if a == b or a == '':
        return True
    if len(a) > len(b):
        return False
    start = 0
    while True:
        if start > len(b) - len(a):
            return False
        if a == b[start:start+len(a)]:
            return True
        start += 1

def reorder(strings):
    """
    >>> reorder(['a', 'aba', 'abacaba', 'ba', 'aba'])
    ['a', 'ba', 'aba', 'aba', 'abacaba']
    >>> reorder(['a', 'abacaba', 'ba', 'aba', 'abab'])
    False
    >>> reorder(['qwerty', 'qwerty', 'qwerty'])
    ['qwerty', 'qwerty', 'qwerty']
    >>> reorder(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'])
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    >>> reorder(['ba', 'a'])
    False
    >>> reorder(['a', 'b', 'a', 'b', 'a'])
    False
    >>> reorder(['a', 'b', 'b', 'a', 'a'])
    ['a', 'b', 'a', 'b', 'a']
    >>> reorder(['a', 'b', 'b', 'a', 'a'])
    ['a', 'b', 'a', 'b', 'a']
    """
    if len(strings) == 0:
        return strings
    for i in range(len(strings)):
        if strings[i] == '':
            return False
        for j in range(i+1, len(strings)):
            if not (is_substring(strings[i], strings[j]) or is_substring(strings[j], strings[i])):
                return False
    strings.sort(key = len)
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
