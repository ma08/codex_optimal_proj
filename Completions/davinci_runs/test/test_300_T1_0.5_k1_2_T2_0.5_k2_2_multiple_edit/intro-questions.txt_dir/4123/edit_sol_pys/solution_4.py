
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
    for i in range(len(s) - 3 + 1):
        three_gram = s[i:i + 3]
        counter[three_gram] = counter.get(three_gram, 0) + 1
    max_value = max(counter.values())
    for k, v in counter.items():
        if v == max_value:
            return k


if __name__ == "__main__":
    n = int(input())
    s = input()
    result = solve(s)
    print(result)
