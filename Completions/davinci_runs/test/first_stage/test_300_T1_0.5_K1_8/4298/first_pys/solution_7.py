


def main():
    n, d = map(int, input().split())
    if d == 0:
        print(1)
    else:
        print(n // (2 * d + 1) + 1)


if __name__ == '__main__':
    main()