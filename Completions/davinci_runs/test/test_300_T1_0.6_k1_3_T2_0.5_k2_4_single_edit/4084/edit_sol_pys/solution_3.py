
n, a, b = map(int, input().split())
n -= 1
print(n // (a + b) * a + min(n % (a + b), a))
