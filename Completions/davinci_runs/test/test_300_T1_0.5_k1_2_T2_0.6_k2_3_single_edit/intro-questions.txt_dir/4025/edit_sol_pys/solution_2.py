

import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b, c = [int(x) for x in sys.stdin.readline().split()]

g = gcd(gcd(a, b), c)

sys.stdout.write(str(min(a//g, b//g, c//g)*7))
