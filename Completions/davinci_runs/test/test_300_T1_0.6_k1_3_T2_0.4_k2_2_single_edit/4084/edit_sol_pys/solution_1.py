
n, a, b = map(int, input().split())
n -= 1

gcd = gcd(a, b)
lcm = a * b // gcd

gcd = gcd(a, b)

print(n // (a + b) * a + min(n % (a + b), a))
