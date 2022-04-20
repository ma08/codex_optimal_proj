
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
        two_gram = s[i:i + 2]  # 0:2, 1:3, 2:4, 3:5, 4:6, 5:7
        counter[two_gram] = counter.get(two_gram, 0) + 1  # BB:1, BA:1, AA:1, AB:1, BC:1, CB:1, BA:1
    max_value = max(counter.values())
    return [k for k, v in counter.items() if v == max_value][0]


if __name__ == "__main__":
    n = int(input())
    s = input()
    result = solve(s)
    print(result)
