
n, a, b = map(int, input().split())
n = n % (a + b)
if n <= a:
    print(n)
else:
    print(a)
