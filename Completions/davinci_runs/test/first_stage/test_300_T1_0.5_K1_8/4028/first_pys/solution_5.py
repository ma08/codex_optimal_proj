

def count_regular_brackets(n, s):
    """
    >>> count_regular_brackets(5, '()))()')
    5
    >>> count_regular_brackets(3, '(()')
    4
    >>> count_regular_brackets(2, '(((')
    0
    """
    MOD = 1000000007
    result = 0
    if s == '('*n + ')'*n:
        return 1
    if n <= len(s):
        return result
    for i in range(n-len(s)):
        result = (result + count_regular_brackets(n-i-1, s+')')) % MOD
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()