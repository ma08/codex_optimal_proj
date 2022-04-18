


def main():
    a, b, c = map(int, input().split())
    print(a*b*c if a*b*c > a+b+c else a+b+c)


if __name__ == '__main__':
    main()
