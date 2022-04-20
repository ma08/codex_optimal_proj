
def solve(s):
    """
    >>> solve("BBAABBBA") == 'BB'
    True
    >>> solve("ABACABA") == 'AB'
    True
    >>> solve("ZZZAA") == 'ZZ'
    True
    """
    counter = dict()
    for i in range(len(s) - 1):  # 0, 1, 2, 3, 4, 5, 6
        two_gram = s[i:i + 2]  # BB, BA, AA, AB, BB, BB, BA
        counter[two_gram] = counter.get(two_gram, 0) + 1
    max_value = max(counter.values())  # 3
    for k, v in counter.items():
        if v == max_value:  # 3
            return k  # BB


if __name__ == "__main__":
    n = int(input())
    s = input()
    result = solve(s)
    print(result)
