

def main():
    a, b = map(int, input().split())
    if a == 1 or b == 1 or a == b:
        print(a*b)
    elif a == 2:
        if b == 2 or b == 3 or b == 5 or b == 7 or b == 8:
            print(a*b)
        else:
            print(-1)
    elif a == 3 or a == 5 or a == 7:
        if b == 2 or b == 3 or b == 5 or b == 7 or b == 8:
            print(a*b)
        else:
            print(-1)
    else:
        print(-1)

if __name__ == '__main__':
    main()
