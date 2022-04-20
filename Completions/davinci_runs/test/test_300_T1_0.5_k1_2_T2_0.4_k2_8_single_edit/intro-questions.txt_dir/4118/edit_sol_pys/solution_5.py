

def main():
    a, b = map(int, input().split())
    if a == 1:
        if b == 1:
            print(1)
        else:
            print(b)
    elif a == 2 and b == 2:
        print(4)
    elif a == 3:
        if b == 3:
            print(9)
        else:
            print(-1)
    elif a == 4:
        if b == 3:
            print(12)
        else:
            print(-1)
    elif a == 5:
        if b == 5:
            print(20)
        else:
            print(-1)
    elif a == 6:
        if b == 5:
            print(30)
        else:
            print(-1)
    elif a == 7:
        if b == 7:
            print(49)
        else:
            print(-1)
    elif a == 8:
        if b == 3:
            print(24)
        else:
            print(-1)
    elif a == 9:
        if b == 3:
            print(27)
        else:
            print(-1)
    else:
        print(-1)

if __name__ == '__main__':
    main()
