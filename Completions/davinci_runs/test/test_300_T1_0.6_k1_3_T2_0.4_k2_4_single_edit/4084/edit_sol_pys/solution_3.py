

n = int(input())

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

gcd = gcd(a, b)

print(n // (a + b) * a + min(n % (a + b), a))
