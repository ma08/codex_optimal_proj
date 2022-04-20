

import sys

input = sys.stdin.readline().split()
a = int(input[0])
b = int(input[1])


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


print(lcm(a, b))