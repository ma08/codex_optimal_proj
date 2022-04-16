

def main():
    a, b, c, d = map(int, input().split()) # 4つの整数を入力
    print(max(a * c, a * d, b * c, b * d)) # 乗算した値の最大値を出力

if __name__ == '__main__':
    main()
