

a, b, x = map(int, input().split())

if x < a:
    print(0)
else:
    n = (x - b) // a
    if a * n + b * len(str(n)) > x:
        print(n - 1)
    else:
        print(n)