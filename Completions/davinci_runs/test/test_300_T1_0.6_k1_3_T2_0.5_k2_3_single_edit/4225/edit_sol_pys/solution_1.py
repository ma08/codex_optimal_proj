

a, b, c, d = map(int, input().split())

if d <= a:
    print(d)
elif d <= a + b:
    print(a)
else:
    print(a - (d - (a + b)))
