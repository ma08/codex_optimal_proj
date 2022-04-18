

def main():
    a, b, c = [int(x) for x in input().split()]
    order = input()

    if order == "ABC":
        if a > b:
            a, b = b, a
        if b > c:
            b, c = c, b
        if a > b:
            a, b = b, a
    elif order == "ACB":
        if a > c:
            a, c = c, a
        if a > b:
            a, b = b, a
        if b > c:
            b, c = c, b
    elif order == "BAC":
        if b > a:
            b, a = a, b
        if b > c:
            b, c = c, b
        if a > c:
            a, c = c, a
    elif order == "BCA":
        if b > c:
            b, c = c, b
        if b > a:
            b, a = a, b
        if a > c:
            a, c = c, a
    elif order == "CAB":
        if c > a:
            c, a = a, c
        if c > b:
            c, b = b, c
        if a > b:
            a, b = b, a
    elif order == "CBA":
        if c > b:
            c, b = b, c
        if c > a:
            c, a = a, c
        if a > b:
            a, b = b, a

    print(a, b, c)


if __name__ == '__main__':
    main()
