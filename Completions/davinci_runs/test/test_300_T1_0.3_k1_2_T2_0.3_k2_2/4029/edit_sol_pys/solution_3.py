

def main():
    n = int(input())
    if n % 25 == 0:
        print(0)
    else:
        if n % 2 == 0:
            print(2)
        elif n % 3 == 0:
            print(3)
        elif n % 5 == 0:
            print(5)
        elif n % 7 == 0:
            print(7)
        elif n % 11 == 0:
            print(11)
        elif n % 13 == 0:
            print(13)
        elif n % 17 == 0:
            print(17)
        elif n % 19 == 0:
            print(19)
        elif n % 23 == 0:
            print(23)
        print(-1)

if __name__ == "__main__":
    main()
