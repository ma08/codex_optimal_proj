
def solve(s):
    """
    >>> solve("BBAABBBA") == 'BB'
    True
    >>> solve("ABACABA") == 'AB'
    True
    >>> solve("ZZZAA") == 'ZZ'
    >>> solve("ZZZAAAA") == 'ZZ'
    True
    True
    """
    count = dict()
    for i in range(len(s)-1):
        two_gram = s[i:i+2]
        count[two_gram] = count.get(two_gram, 0) + 1
    max_value = max(count.values())
    for k, value in count.items():
        if value == max_value:
            return k


if __name__ == "__main__":
    n = int(input())
    s = input()
    result = solve(s)
    print(result)
