

def main():
    a, b, c, d = map(int, input().split())  # 入力を4つの変数に格納
    print(max(a * d, a * c, b * d, b * c))  # 乗算した値の最大値を出力

if __name__ == '__main__':
    main()
