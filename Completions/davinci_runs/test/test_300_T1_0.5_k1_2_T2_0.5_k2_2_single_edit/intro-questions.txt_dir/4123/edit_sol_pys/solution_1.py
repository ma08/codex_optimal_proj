
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
    for i in range(len(s) - 1):  # 処理する文字列の長さ - 1
        two_gram = s[i:i+2]  # 文字列のスライス
        counter[two_gram] = counter.get(two_gram, 0) + 1
    max_value = max(counter.values())  # 出現回数の最大値
    for k, v in counter.items():
        if v == max_value:  # 最大値と同じ出現回数
            return k


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # n = int(input())
    # s = input()
    # result = solve(s)
    # print(result)
