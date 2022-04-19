
import sys
sys.setrecursionlimit(10**7)

def solve(s):
    """
    >>> solve("BBAABBBA")
    'BB'
    >>> solve("ABACABA")
    'AB'
    >>> solve("ZZZAA")
    >>> solve("ZZZA")
    'ZZ'
    'ZZ'
    """
    counter = dict()
    for i in range(len(s)):
        for j in range(1, len(s) - i + 1):
            two_gram = s[i:i+j]
            counter[two_gram] = counter.get(two_gram, 0) + 1
    max_value = max(counter.keys(), key=lambda x: counter[x])
    return max_value


if __name__ == "__main__":
    n = int(input())
    s = input()
    result = solve(s)
    print(result)
