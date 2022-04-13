
def hailstone(n):
    """
    >>> hailstone(10)
    7
    >>> hailstone(1)
    4
    """
    if n == 1:
        return 4
    if n % 2 == 0:
        return n + hailstone(n // 2)
    else:
        return n + hailstone(3 * n + 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
