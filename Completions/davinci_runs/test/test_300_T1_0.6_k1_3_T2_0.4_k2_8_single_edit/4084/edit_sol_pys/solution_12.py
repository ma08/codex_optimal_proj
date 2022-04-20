
n, a, b = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

lcm = a * b // gcd(a, b)

print(n // (a + b) * a + min(n % (a + b), a))
