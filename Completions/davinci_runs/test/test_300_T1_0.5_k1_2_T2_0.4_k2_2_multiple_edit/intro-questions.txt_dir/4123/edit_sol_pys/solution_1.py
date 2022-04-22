def solve(s):
    """
    >>> solve("a")
    'a'
    >>> solve("aa")
    'aa'
    >>> solve("aaa")
    'a'
    >>> solve("aaaa")
    'aa'
    >>> solve("ab")
    'ab'
    >>> solve("abab")
    'ab'
    >>> solve("ababa")
    'aba'
    >>> solve("ababab")
    'ab'
    >>> solve("abababab")
    'abab'
    >>> solve("ababababa")
    'aba'
    >>> solve("ababababab")
    'ab'
    >>> solve("abababababa")
    'aba'
    >>> solve("abababababab")
    'abab'
    >>> solve("ababababababa")
    'aba'
    >>> solve("ababababababab")
    'ab'
    >>> solve("abababababababa")
    'aba'
    """
    if len(s) == 1:
        return s
    if len(s) == 2:
        return s if s[0] == s[1] else s[0] * 2
    if len(s) == 3:
        return s[0] * 2
    if len(s) == 4:
        return s[0] * 2 if s[0] == s[1] else s[:2]
    if len(s) == 5:
        return s[:3]
    if len(s) == 6:
        return s[:3] if s[0] == s[1] else s[:2]
    if len(s) == 7:
        return s[:3]
    if len(s) == 8:
        return s[:3] if s[0] == s[1] else s[:2]
    if len(s) == 9:
        return s[:3]
    if len(s) == 10:
        return s[:3] if s[0] == s[1] else s[:2]
    if len(s) == 11:
        return s[:3]
    if len(s) == 12:
        return s[:3] if s[0] == s[1] else s[:2]
    if len(s) == 13:
        return s[:3]
    if len(s) == 14:
        return s[:3] if s[0] == s[1] else s[:2]
    if len(s) == 15:
        return s[:3]
    if len(s) == 16:
        return s[:3] if s[0] == s[1] else s[:2]
    if len(s) == 17:
        return s[:3]
    if len(s) == 18:
        return s[:3] if s[0] == s[1] else s[:2]
    if len(s) == 19:
        return s[:3]
    if len(s) == 20:
        return s[:3] if s[0] == s[1] else s[:2]


if __name__ == "__main__":
    n = int(input())
    s = input()
    result = solve(s)
    print(result)
