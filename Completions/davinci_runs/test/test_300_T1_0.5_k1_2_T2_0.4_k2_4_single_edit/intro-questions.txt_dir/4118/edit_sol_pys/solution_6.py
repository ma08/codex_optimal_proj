

def main():
    a, b = map(int, input().split())
    if a == 1 or b == 1:
        print(a*b)
    elif a == 2 or a == 3 or a == 5 or a == 7:
        if b == 2 or b == 3 or b == 5 or b == 7:
            print(a * b)
        elif b == 4:
            print(-1)
        elif b == 6:
            print(10)
        elif b == 8:
            print(14)
        elif b == 9:
            print(18)
    elif a == 4 or a == 8:
        if b == 2 or b == 3 or b == 5 or b == 7:
            print(a * b)
        elif b == 4:
            print(a * b)
        elif b == 6:
            print(a * b)
        elif b == 8:
            print(a * b)
        elif b == 9:
            print(a * b)
    elif a == 6:
        if b == 2 or b == 3 or b == 5 or b == 7:
            print(a * b)
        elif b == 4:
            print(-1)
        elif b == 6:
            print(a * b)
        elif b == 8:
            print(a * b)
        elif b == 9:
            print(a * b)
    elif a == 9:
        if b == 2 or b == 3 or b == 5 or b == 7:
            print(a * b)
        elif b == 4:
            print(-1)
        elif b == 6:
            print(a * b)
        elif b == 8:
            print(a * b)
        elif b == 9:
            print(a * b)
    else:
        print(-1)


if __name__ == '__main__':
    main()
