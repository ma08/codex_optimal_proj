

from math import sqrt
from sys import stdin, stdout

def solve(a, b, n):
    if n == 0:
        return a
    if n == 1:
        return b
    return solve(b, a + b, n - 1)

a, b, n = map(int, stdin.readline().split())
stdout.write(str(solve(a, b, n)))
