

def get_max_increase_sequence(a):
    """
    >>> get_max_increase_sequence([1, 2, 4, 3, 2])
    (4, 'LRRR')
    >>> get_max_increase_sequence([1, 3, 5, 6, 5, 4, 2])
    (6, 'LRLRRR')
    >>> get_max_increase_sequence([2, 2, 2])
    (1, 'R')
    >>> get_max_increase_sequence([1, 2, 4, 3])
    (4, 'LLRR')
    """
    n = len(a)
    l = [0] * n
    r = [0] * n
    l[0] = 1
    r[n - 1] = 1
    for i in range(1, n):
        l[i] = l[i - 1]
        if a[i] > a[i - 1]:
            l[i] += 1
        r[n - i - 1] = r[n - i]
        if a[n - i - 1] < a[n - i]:
            r[n - i - 1] += 1
    m = 0
    res = ''
    for i in range(n):
        if l[i] + r[i] - 1 > m:
            m = l[i] + r[i] - 1
            res = 'L' * l[i] + 'R' * (r[i] - 1)
    return m, res

if __name__ == '__main__':
    import doctest
    doctest.testmod()