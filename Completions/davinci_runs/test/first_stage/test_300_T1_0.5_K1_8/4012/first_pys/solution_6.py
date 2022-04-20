

T = int(input())

for i in range(T):
    a, b, c = map(int, input().split())

    # b = a * x
    # c = b * y
    # c = a * x * y
    # c = a * z

    # x = c / a
    # y = c / b
    # z = c / a

    # print(a, b, c)
    # print(x, y, z)

    x = c // a
    y = c // b
    z = c // a

    # print(x, y, z)

    if x > 1:
        a = a * x
        b = b * x
        c = c * x
    elif y > 1:
        a = a * y
        b = b * y
        c = c * y
    elif z > 1:
        a = a * z
        b = b * z
        c = c * z

    print(a, b, c)