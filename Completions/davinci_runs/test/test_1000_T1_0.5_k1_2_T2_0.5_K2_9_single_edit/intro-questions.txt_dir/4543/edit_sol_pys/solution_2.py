

def is_square(x):
    return int(x**0.5)**2 == x


def main():
    a, b = map(int, input().split())

    if is_square(int(str(a) + str(b))):  # 文字列を結合して整数に変換している
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
