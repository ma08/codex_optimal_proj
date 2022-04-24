import math

n, a, b = map(int, input().split())
n -= 1

gcd = math.gcd(a, b)

print(n // (a + b) * a + min(n % (a + b), a))
