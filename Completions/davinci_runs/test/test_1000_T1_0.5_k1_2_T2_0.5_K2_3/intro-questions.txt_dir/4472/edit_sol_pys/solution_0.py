import math

def solve(a, b):
    if a == b:
        return 0
    n = len(a)
    if n % 2 == 1:
        if a[n//2] == b[n//2]:
            return solve(a[:n//2] + a[n//2+1:], b[:n//2] + b[n//2+1:])
        else:
            return 1
    else:
        if a[n//2-1:n//2+1] == b[n//2-1:n//2+1]:
            return solve(a[:n//2-1] + a[n//2+1:], b[:n//2-1] + b[n//2+1:])
        else:
            return 1


def test():
    assert solve("abacaba", "bacabaa") == 1
    assert solve("zcabd", "dbacz") == 0
    assert solve("abcabc", "abcabc") == 0
    assert solve("abcdabcd", "abcdabcd") == 0
    assert solve("a", "a") == 0
    assert solve("a", "b") == 1
    assert solve("ab", "ba") == 1
    assert solve("ab", "ab") == 0
    assert solve("abcd", "abcd") == 0
    assert solve("abcd", "dcba") == 1
    assert solve("abcde", "abcde") == 0
    assert solve("abcde", "edcba") == 1
