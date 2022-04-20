

a, b, c = map(int, input().split())

if c <= a:
    print(c)
elif c <= a + b:
    print(a)
else:
    print(a - (c - (a + b)))
