


def main():
    a, b, c = map(int, input().split())

    print(min(a + b, b + c, c + a))


if __name__ == '__main__':
    main()
