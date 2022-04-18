
n, a, b = map(int, input().split())

if a > b:
    n = n % (a + b)

    if n <= a:
        print(n)
    else:
        print(a)
else:
    print(n % (a + b))
