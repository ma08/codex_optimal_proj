
def main():
    a, b = map(int, input().split())  # 文字列を整数に変換

    if a == b:
        print(4 * a)  # 4倍
    else:
        print(2 * (a + b))  # 2倍


if __name__ == "__main__":
    main()
