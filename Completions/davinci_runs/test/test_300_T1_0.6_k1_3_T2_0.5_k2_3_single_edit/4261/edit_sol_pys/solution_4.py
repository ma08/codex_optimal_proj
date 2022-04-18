

a, b = map(int, input().split())

while 1:
    if b <= a:
        print(0)
        break
    elif b > a:
        print(b - a)
        break
