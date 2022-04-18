

def solve(n, k, t):
    """
    >>> solve(3, 1, 'aba')
    'aba'
    >>> solve(2, 3, 'cat')
    'catcatcat'
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
