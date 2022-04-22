

def main():
    a, b = map(int, input().split())
    if a == 1 or b == 1:
        print(a * b)
    elif a == 2:
        if b == 2 or b == 3 or b == 5 or b == 6:
            print(a * b)
        else:
            print(-1)
    elif a == 3:
        if b == 2 or b == 3 or b == 5 or b == 6:
            print(a * b)
        else:
            print(-1)
    elif a == 4:
        if b == 3 or b == 5 or b == 7:
            print(a * b)
        else:
            print(-1)
    elif a == 5:
        if b == 2 or b == 3 or b == 5 or b == 6:
            print(a * b)
        else:
            print(-1)
    elif a == 6:
        if b == 5 or b == 7:
            print(a * b)
        else:
            print(-1)
    elif a == 7:
        if b == 2 or b == 3 or b == 5 or b == 6:
            print(a * b)
        else:
            print(-1)
    elif a == 8:
        if b == 3 or b == 5 or b == 7:
            print(a * b)
        else:
            print(-1)
    elif a == 9:
        if b == 2 or b == 3 or b == 5 or b == 6:
            print(a * b)
        else:
            print(-1)
    else:
        print(-1)

if __name__ == '__main__':
    main()
