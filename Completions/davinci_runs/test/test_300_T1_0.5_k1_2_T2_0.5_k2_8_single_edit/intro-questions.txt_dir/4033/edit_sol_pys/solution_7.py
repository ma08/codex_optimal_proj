

def main():
    a, b = map(int, input().split())  # 標準入力

    if a == b:
        print(4*a)  # 標準出力
        return

    if a < b:
        a, b = b, a

    # a > b
    if (a+b) % 3 == 0:
        print(2*(a+b)//3)  # 標準出力
    else:
        print(2*(a+b)//3+1)  # 標準出力


if __name__ == "__main__":
    main()
