

from math import sqrt
from sys import stdin, stdout

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve(a, b):
    if a < b:
        return solve(b, a)
    if a == b:
        return a + b
    if a % b == 0:
        return a + b
    return gcd(a, b) + a + b

a, b = map(int, stdin.readline().split())
stdout.write(str(solve(a, b)))
