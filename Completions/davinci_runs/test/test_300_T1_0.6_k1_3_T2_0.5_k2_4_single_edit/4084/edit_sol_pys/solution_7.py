
n, a, b = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

gcd = gcd(a, b)

print((n - 1) // (a + b) * a + min((n - 1) % (a + b), a))
