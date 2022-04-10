

def solve(s, t):
    """
    >>> solve("bbaba", "bb")
    3
    >>> solve("baaba", "ab")
    2
    >>> solve("abcde", "abcde")
    0
    >>> solve("asdfasdf", "fasd")
    3
    """
    for i in range(len(s), 0, -1):
        for j in range(len(s) - i + 1):
            if t in s[j:j+i]:
                return i

if __name__ == "__main__":
    print(solve(input(), input()))