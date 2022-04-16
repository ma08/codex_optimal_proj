


def main():
    a, b, c, k = map(int, input().split())
    print(a + b + c + max(a, b, c) * 2 ** k)


if __name__ == '__main__':
    main()
