

n, m = map(int, input().split())
a = [int(input()) for _ in range(m)]

def lcm(a, b):
    return a * b // gcd(a, b)

gcd = gcd(a, b)

print(n // (a + b) * a + min(n % (a + b), a))
