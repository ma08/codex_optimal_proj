

a, b, c, d = map(int, input().split())
if c < a:
    if d <= a:
        print(0)
    elif d <= b:
        print(d - a)
    else:
        print(b - a)
elif c < b:
    if d <= b:
        print(d - c)
    else:
        print(b - c)
else:
    print(0)
