

def main():
    a, b = map(int, input().split())
    if a == 1 or b == 1:
        print(a*b)
    elif a == 2 or a == 3 or a == 5 or a == 7:
        if b == 2 or b == 3 or b == 5 or b == 7:
            print(a * b)
        elif a == 2 and b == 4:
            print(4)
        elif a == 3 and b == 4:
            print(6)
        elif a == 5 and b == 4:
            print(10)
        elif a == 7 and b == 4:
            print(14)
        elif a == 2 and b == 8:
            print(8)
        elif a == 3 and b == 8:
            print(12)
        elif a == 5 and b == 8:
            print(20)
        elif a == 7 and b == 8:
            print(28)
        elif a == 2 and b == 9:
            print(6)
        elif a == 3 and b == 9:
            print(9)
        elif a == 5 and b == 9:
            print(15)
        elif a == 7 and b == 9:
            print(21)
    else:
        print(-1)

if __name__ == '__main__':
    main()
