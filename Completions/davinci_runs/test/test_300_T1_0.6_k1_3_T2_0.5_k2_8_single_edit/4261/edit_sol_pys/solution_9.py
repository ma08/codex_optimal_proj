
a, b, c = map(int, input().split())
while True:
    if b + c <= a:
        print(0)
        break
    elif b + c > a:
        print(b + c - a)
        break
