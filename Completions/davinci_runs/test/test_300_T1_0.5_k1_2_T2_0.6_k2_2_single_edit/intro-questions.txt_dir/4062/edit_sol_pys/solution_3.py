

def main():
    a, b, c, d = map(int, input().split())   # スペース区切りの整数の入力
    print(max(a * c, a * d, b * c, b * d))   # 最大値を出力

if __name__ == '__main__':
    main()
