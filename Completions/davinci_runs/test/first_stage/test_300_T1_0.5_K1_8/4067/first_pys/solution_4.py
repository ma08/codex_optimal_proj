

# noinspection PyPep8Naming
def solve(n, s):
    """
    >>> solve(3, '121')
    '021'
    >>> solve(6, '000000')
    '001122'
    >>> solve(6, '211200')
    '211200'
    >>> solve(6, '120110')
    '120120'
    """
    s = list(s)
    count_0 = s.count('0')
    count_1 = s.count('1')
    count_2 = s.count('2')
    if count_0 == count_1 == count_2:
        return ''.join(s)
    if count_0 > count_1:
        index = s.index('0')
        s[index] = '1'
    else:
        index = s.index('2')
        s[index] = '1'
    return ''.join(s)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    n = int(input())
    s = input()
    print(solve(n, s))