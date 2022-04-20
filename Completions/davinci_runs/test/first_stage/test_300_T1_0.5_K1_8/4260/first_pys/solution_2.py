


def leap_time(T, X):
    return T / X


def main():
    T, X = map(int, input().split())
    print(leap_time(T, X))


if __name__ == '__main__':
    main()