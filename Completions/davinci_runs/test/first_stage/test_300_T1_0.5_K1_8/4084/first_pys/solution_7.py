


def main():
    n, a, b = map(int, input().split())
    n_blue_balls = n // (a + b) * a
    n_blue_balls += min(n % (a + b), a)
    print(n_blue_balls)


if __name__ == '__main__':
    main()