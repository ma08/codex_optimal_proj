

def main():
    a, b = map(int, input().split())  # 整数の入力

    if a == b:
        print(4 * a)  # 出力
    else:
        print(2 * (a + b))  # 出力

if __name__ == "__main__":
    main()
