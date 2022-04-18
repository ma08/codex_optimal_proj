
def solve(s):
    """
    >>> solve('BBAABBBA')
    'BA'
    >>> solve('ABACABA')
    'BA'
    >>> solve('ZZZAA')
    'ZZ'
    """
    counter = dict()
    for i in range(len(s) - 1):  # 0, 1, 2, 3, 4, 5, 6
        two_gram = s[i:i + 2]
        counter[two_gram] = counter.get(two_gram, 0) + 1
    max_value = max(counter.values())
    max_keys = [k for k, v in counter.items() if v == max_value]
    return min(max_keys)


if __name__ == "__main__":
    n = int(input())
    s = input()
    result = solve(s)
    print(result)
