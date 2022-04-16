

a, b, c = map(int, input().split())


def main():
    if a + b < c:
        print(0)
    else:
        if a + b == c:
            print(1)
        else:
            print(2)


if __name__ == '__main__':
    main()
