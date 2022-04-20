

a, b = map(int, input().split())

while 1:
    if a + b <= 0:
        print(0)
        break
    elif a + b > 0:
        print(a + b)
        break
