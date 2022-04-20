import math


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a, b, c, d = map(int, input().split())
lcm = c * d // gcd(c, d)
print(b - a + 1 - (b // c + b // d - b // lcm) + (a - 1) // c + (a - 1) // d - (a - 1) // lcm)
