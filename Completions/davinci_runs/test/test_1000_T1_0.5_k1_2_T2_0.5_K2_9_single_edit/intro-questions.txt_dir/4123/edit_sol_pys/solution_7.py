


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
    for i in range(len(s) - 1): # -1 は最後の文字を取り出せないので
        two_gram = s[i:i+2] # 2文字ずつ取り出す
        counter[two_gram] = counter.get(two_gram, 0) + 1
    max_value = max(counter.values()) # counter.values()は値のみのリストを取得
    for k, v in counter.items():
        if v == max_value:
            return k


if __name__ == "__main__":
    n = int(input()) # nは使わない
    s = input() # 文字列
    result = solve(s)
    print(result)
