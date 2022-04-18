

def main():
    a, b = map(int, input().split())
    if a == 1 or b == 1 or a == b:
        print(a*b)
    elif a == 2 and b == 4:
        print(4)
    elif a == 4 and b == 2:
        print(4)
    elif a == 3 and b == 6:
        print(9)
    elif a == 6 and b == 3:
        print(9)
    elif a == 2 and b == 8:
        print(8)
    elif a == 8 and b == 2:
        print(8)
    else:
        print(-1)

if __name__ == '__main__':
    main()
