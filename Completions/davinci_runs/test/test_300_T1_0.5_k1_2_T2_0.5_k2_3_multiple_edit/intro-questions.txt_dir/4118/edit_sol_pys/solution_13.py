
def main():
    a, b = map(int, input().split())
    if a == 1 or b == 1:
        print(a*b)
    elif a == 2:
        if b in [2, 3, 5, 7]:
            print(a*b)
        else:
            print(-1)
    elif a == 3:
        if b in [2, 3, 5, 7]:
            print(a*b)
        else:
            print(-1)
    elif a == 4:
        if b in [3, 5, 7]:
            print(a*b)
        else:
            print(-1)
    elif a == 5:
        if b in [2, 3, 5, 7]:
            print(a*b)
        else:
            print(-1)
    elif a == 6:
        if b in [5, 7]:
            print(a*b)
        else:
            print(-1)
    elif a == 7:
        if b in [2, 3, 5, 7]:
            print(a*b)
        else:
            print(-1)
    elif a == 8:
        if b in [3, 5, 7]:
            print(a*b)
        else:
            print(-1)
    elif a == 9:
        if b in [2, 3, 5, 7]:
            print(a*b)
        else:
            print(-1)
    else:
        print(-1)

if __name__ == '__main__':
    main()
