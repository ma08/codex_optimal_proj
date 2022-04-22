
def solve(s):
    """
    >>> solve("BBAABBBA")  # doctest: +NORMALIZE_WHITESPACE
    'BB'
    >>> solve("ABACABA")
    'AB'
    >>> solve("ZZZAA")
    'ZZ'
    """
    counter = dict()
    for i in range(len(s) - 1):
        two_gram = s[i:i+2]
        counter[two_gram] = counter.get(two_gram, 0) + 1
    max_value = max(counter.values())
    for k, v in counter.items():
        if v == max_value:
            return k


if __name__ == "__main__":
    n = int(input())
    s = input()
    result = solve(s)
    print(result)
