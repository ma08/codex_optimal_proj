


def main():
    a, b, c = map(int, input().split())
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(int(area))


if __name__ == '__main__':
    main()