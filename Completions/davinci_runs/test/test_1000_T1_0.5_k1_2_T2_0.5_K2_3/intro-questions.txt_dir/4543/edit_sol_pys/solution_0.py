def is_square(x):
    return int(x ** 0.5) ** 2 == x


def main():
    a, b = map(int, input().split())

    if is_square(int(str(a) + str(b))):  # str(a) + str(b)を数値に変換して二乗数かどうか判定
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
