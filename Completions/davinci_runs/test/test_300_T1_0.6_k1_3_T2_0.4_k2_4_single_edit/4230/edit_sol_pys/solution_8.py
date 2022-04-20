

def main():
    x, n = map(int, input().split())  # x: 無限大の数, n: ピラミッドの段数
    p = sorted(list(map(int, input().split())))  # p: ピラミッドの高さ
    # ピラミッドの中にxが無い場合

    if x < p[0]:
    # ピラミッドの中にxがある場合
        print(p[0] - x)
    elif x > p[-1]:
        print(x - p[-1])
    else:
        for i in range(n-1):
            if x < p[i+1]:
                print(min(x-p[i], p[i+1] - x))  # xと近い方を出力
                break

if __name__ == '__main__':
    main()
