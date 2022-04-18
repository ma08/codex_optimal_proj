

def main():
    r, g, b = map(int, input().split())  # スペース区切りで数値を取得

    num = r * 100 + g * 10 + b  # 三桁の数値を作る
    if num % 4 == 0:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
