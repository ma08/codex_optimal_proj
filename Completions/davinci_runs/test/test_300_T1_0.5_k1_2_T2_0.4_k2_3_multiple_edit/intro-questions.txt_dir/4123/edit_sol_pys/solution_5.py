
def solve(s):
    """
    >>> solve("BBAABBBA") == 'BB'
    True
    >>> solve("ABACABA") == 'AB'
    True
    >>> solve("ZZZAA") == 'ZZ'
    True
    """
    count = dict()
    for i in range(len(s) - 1):
        two_gram = s[i:i+2]
        count[two_gram] = count.get(two_gram, 0) + 1
    max_value = max(count.values())
    for k, v in count.items():
        if v == max_value:
            return k


if __name__ == "__main__":
    n = int(input())
    s = input()
    result = solve(s)
    print(result)
