

def main():
    a, b = map(int, input().split())  # 入力を受け取る

    if a == b:  # aとbが等しい場合
        print(4 * a)  # 出力
    else:
        print(2 * (a + b))  # 出力

if __name__ == "__main__":
    main()
