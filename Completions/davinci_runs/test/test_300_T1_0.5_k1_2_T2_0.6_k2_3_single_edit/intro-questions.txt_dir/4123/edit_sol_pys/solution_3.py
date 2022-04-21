from collections import Counter


def solve(s):
    """
    >>> solve("BBAABBBA")
    'BB'
    >>> solve("ABACABA")
    'AB'
    >>> solve("ZZZAA")
    'ZZ'
    """
    counter = Counter(s[i:i+2] for i in range(len(s) - 1))
    return counter.most_common(1)[0][0]


if __name__ == "__main__":
    n = int(input())
    s = input()
    result = solve(s)
    print(result)
