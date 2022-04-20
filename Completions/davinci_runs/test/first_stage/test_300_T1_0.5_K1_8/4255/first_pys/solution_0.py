


def main():
    a, b, c = map(int, input().split())
    s = (a + b + c) / 2
    print(int((s * (s - a) * (s - b) * (s - c)) ** 0.5))


if __name__ == "__main__":
    main()