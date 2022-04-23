

def solve(n, k, s):
    """
    >>> solve(3, 4, 'ab')
    'ababababa'
    >>> solve(3, 2, 'ca')
    'caca'
    """
    t = ''
    while k > 0:
        t += s
        k -= 1
    return t + s[0:n-(len(t) % n)]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    n, k = map(int, input().split())
    t = input()
    print(solve(n, k, t))
