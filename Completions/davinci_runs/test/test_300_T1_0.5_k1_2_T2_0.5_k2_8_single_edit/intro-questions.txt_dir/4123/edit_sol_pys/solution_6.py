
def solve(s):
    """
    >>> solve("BBAABBBA")
    'BB'
    >>> solve("ABACABA")
    'AB'
    >>> solve("ZZZAAZZ")
    'ZZZ'
    """
    counter = dict()
    for i in range(len(s) - 2):
        two_gram = s[i:i + 3]
        counter[two_gram] = counter.get(two_gram, 0) + 1
    max_value = max(counter.values())
    return max(counter, key=counter.get)



if __name__ == "__main__":
    n = int(input())
    s = input()
    result = solve(s)
    print(result)
