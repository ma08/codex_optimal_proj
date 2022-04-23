

a, b, c, d = map(int, input().split())

while 1:
    if b + c <= a and d <= a:
        print(0)
        break
    elif b + c <= a and d > a:
        print(d - a)
        break
    elif b + c > a and d <= a:
        print(b + c - a)
    elif b + c > a and d > a:
        print(max(b + c - a, d - a))
        break
        break
