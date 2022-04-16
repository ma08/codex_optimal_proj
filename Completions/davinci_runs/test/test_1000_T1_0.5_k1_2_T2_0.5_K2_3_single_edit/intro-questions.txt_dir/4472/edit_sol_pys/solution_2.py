
import math

def solve(a, b):
    if a == b:
        return 0
    n = len(a)
    if n % 2 == 1:
        if a[int(n/2)] == b[int(n/2)]:
            return solve(a[:int(n/2)] + a[int(n/2)+1:], b[:int(n/2)] + b[int(n/2)+1:])
        else:
            return 1
    else:
        if a[int(n/2)-1:int(n/2)+1] == b[int(n/2)-1:int(n/2)+1]:
            return solve(a[:int(n/2)-1] + a[int(n/2)+1:], b[:int(n/2)-1] + b[int(n/2)+1:])
        else:
            return 1


def test():
    assert solve("abacaba", "bacabaa") == 1
    assert solve("zcabd", "dbacz") == 1
    assert solve("abcabc", "abcabc") == 1
    assert solve("abcdabcd", "abcdabcd") == 1
    assert solve("a", "a") == 1
    assert solve("a", "b") == 2
    assert solve("ab", "ba") == 2
    assert solve("ab", "ab") == 1
    assert solve("abcd", "abcd") == 1
    assert solve("abcd", "dcba") == 2
    assert solve("abcde", "abcde") == 1
    assert solve("abcde", "edcba") == 2
