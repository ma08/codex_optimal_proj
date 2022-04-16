
import math

def solve(a, b, n):
    if a == b:
        return 0
    if n % 2 == 1:
        if a[math.floor(n/2)] == b[math.floor(n/2)]: # if the middle characters are equal
            return solve(a[:math.floor(n/2)] + a[math.floor(n/2)+1:], b[:math.floor(n/2)] + b[math.floor(n/2)+1:], n-1)
        else:
            return 1
    else:
        if a[math.floor(n/2)-1:math.floor(n/2)+1] == b[math.floor(n/2)-1:math.floor(n/2)+1]:
            return solve(a[:math.floor(n/2)-1] + a[math.floor(n/2)+1:], b[:math.floor(n/2)-1] + b[math.floor(n/2)+1:], n-2)
        else:
            return 1

def solve_wrapper(a, b):
    n = len(a)
    return solve(a, b, n)


def test():
    assert solve_wrapper("abacaba", "bacabaa") == 4
    assert solve_wrapper("zcabd", "dbacz") == 0
    assert solve_wrapper("abcabc", "abcabc") == 0
    assert solve_wrapper("abcdabcd", "abcdabcd") == 0
    assert solve_wrapper("a", "a") == 0
    assert solve_wrapper("a", "b") == 1
    assert solve_wrapper("ab", "ba") == 1
    assert solve_wrapper("ab", "ab") == 0
    assert solve_wrapper("abcd", "abcd") == 0
    assert solve_wrapper("abcd", "dcba") == 1
    assert solve_wrapper("abcde", "abcde") == 0
    assert solve_wrapper("abcde", "edcba") == 1

test()
