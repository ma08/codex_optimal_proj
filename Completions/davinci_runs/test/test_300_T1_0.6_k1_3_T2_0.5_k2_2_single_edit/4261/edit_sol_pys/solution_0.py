

a, b, c = map(int, input().split())

while 1:
    if a + b <= c:
        print(0)
        break
    elif a + b > c:
        print(a + b - c)
        break
