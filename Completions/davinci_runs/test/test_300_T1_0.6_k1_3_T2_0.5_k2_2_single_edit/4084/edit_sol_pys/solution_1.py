import sys

n, a, b = map(int, input().split())
n -= 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

gcd = gcd(a, b)

sys.stdout.write(str(n // (a + b) * a + min(n % (a + b), a)))
