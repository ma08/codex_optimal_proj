


def solve(s):
    """
    >>> solve("BBAABBBA")
    'BB'
    >>> solve("ABACABA")
    'AB'
    >>> solve("ZZZAA")
    'ZZ'
    """
    counter = dict()
    for i in range(len(s) - 1):  # range(len(s) - 1)は[0, 1, 2, 3, 4, 5, 6, 7]
        two_gram = s[i:i+2]
        counter[two_gram] = counter.get(two_gram, 0) + 1  # counter.get(two_gram, 0)はdict.get(key, default)
    max_value = max(counter.values())
    for k, v in counter.items():  # counter.items()はdict.items()
        if v == max_value:
            return k


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # n = int(input())
    # s = input()
    # result = solve(s)
    # print(result)
