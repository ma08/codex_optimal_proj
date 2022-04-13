
def main():
    r, g, b = map(int, input().split())
    num = r * 100 + g * 10 + b  # 各数字を10の位にずらす
    if num % 4 == 0:  # 4で割り切れるならYES
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
