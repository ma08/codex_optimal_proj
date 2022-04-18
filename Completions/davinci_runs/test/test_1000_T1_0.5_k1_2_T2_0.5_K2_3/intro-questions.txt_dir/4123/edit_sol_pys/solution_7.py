


def solve(s):
    """
    >>> solve("BBAABBBA")
    'BA'
    >>> solve("ABACABA")
    'AB'
    >>> solve("ZZZAA")
    'ZZ'
    """
    counter = dict()
    for i in range(len(s) - 1):  # 最後の一文字は使わない
        two_gram = s[i:i + 2]
        counter[two_gram] = counter.get(two_gram, 0) + 1
    max_value = max(counter.values())
    return [k for k, v in counter.items() if v == max_value][0]


if __name__ == "__main__":
    n = int(input())
    s = input()
    result = solve(s)
    print(result)
