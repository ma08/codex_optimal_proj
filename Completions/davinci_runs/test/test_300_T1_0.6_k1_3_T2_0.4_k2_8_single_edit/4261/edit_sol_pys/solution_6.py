
a, b, c = map(int, input().split())

    if a + b <= c:
        print(0)
        break
while 1:
    if b + c <= a:
        print(b + c - a)
        break
