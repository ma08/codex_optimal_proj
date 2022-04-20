

n, a, b = map(int, input().split()) - 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

gcd = gcd(a, b)

print(n // (a + b) * a + min(n % (a + b), a))
