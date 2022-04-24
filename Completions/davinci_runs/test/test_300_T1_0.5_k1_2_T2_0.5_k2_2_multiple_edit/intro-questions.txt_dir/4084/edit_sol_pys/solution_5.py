

n, a, b = map(int, input().split())

if n <= a:
    print(n)
elif n <= a + b:
    print(a)
else:
    n = n - a - b
    print(a - n % (a + b))

