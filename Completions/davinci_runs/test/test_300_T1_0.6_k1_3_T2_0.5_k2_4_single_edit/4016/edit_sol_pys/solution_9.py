def solve(n, k, t):
    """
    >>> solve(3, 4, 'aba')
    'ababababa'
    >>> solve(3, 2, 'cat')
    'catcat'
    """
    s = ''
    while k > 0:
        s += t
        k -= 1
    return s + t[0:n-(len(s) % n)]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    n, k = map(int, input().split())
    t = input()
    print(solve(n, k, t))


def solve(n, k, t):
    """
    >>> solve(3, 4, 'aba')
    'ababababa'
    >>> solve(3, 2, 'cat')
    'catcat'
    """
    s = ''
    while k > 0:
        s += t
        k -= 1
    return s + t[0:n-(len(s) % n)]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    n, k = map(int, input().split())
    t = input()
    print(solve(n, k, t))
