
import math

def solve(a, b):
    if a == b:
        return 0
    n = len(a)
    if n % 2 == 1:
        if a[int(math.floor(n/2))] == b[int(math.floor(n/2))]:
            return solve(a[:int(math.floor(n/2))] + a[int(math.floor(n/2))+1:], b[:int(math.floor(n/2))] + b[int(math.floor(n/2))+1:])
        else:
            return 1
    else:
        if a[int(math.floor(n/2))-1:int(math.floor(n/2))+1] == b[int(math.floor(n/2))-1:int(math.floor(n/2))+1]:
            return solve(a[:int(math.floor(n/2))-1] + a[int(math.floor(n/2))+1:], b[:int(math.floor(n/2))-1] + b[int(math.floor(n/2))+1:])
        else:
            return 1


def test():
    assert solve("abacaba", "bacabaa") == 4, "abacaba"
    assert solve("zcabd", "dbacz") == 0, "zcabd"
    assert solve("abcabc", "abcabc") == 0, "abcabc"
    assert solve("abcdabcd", "abcdabcd") == 0, "abcdabcd"
    assert solve("a", "a") == 0, "a"
    assert solve("a", "b") == 1, "a"
    assert solve("ab", "ba") == 1, "ab"
    assert solve("ab", "ab") == 0, "ab"
    assert solve("abcd", "abcd") == 0, "abcd"
    assert solve("abcd", "dcba") == 1, "abcd"
    assert solve("abcde", "abcde") == 0, "abcde"
    assert solve("abcde", "edcba") == 1, "abcde"

test()
