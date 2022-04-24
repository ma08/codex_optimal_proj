

a, b, c, k = map(int, input().split())  # map(function, iterable)

if k <= a:
    print(k)
elif k <= a + b:
    print(a)
else:
    print(a - (k - (a + b)))
