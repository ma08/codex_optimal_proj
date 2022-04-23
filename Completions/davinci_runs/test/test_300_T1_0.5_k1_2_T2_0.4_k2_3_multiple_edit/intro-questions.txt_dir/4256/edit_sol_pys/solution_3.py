

n, a, b = map(int, input().split())

if n % (a + b) == 0:
    print(n // (a + b) * a)
else:
    print(n // (a + b) * a + min(n % (a + b), a))
