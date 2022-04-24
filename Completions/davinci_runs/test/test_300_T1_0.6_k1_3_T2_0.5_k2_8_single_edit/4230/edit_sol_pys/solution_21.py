

def main():
    x, n = map(int, input().split())  # 入力
    p = sorted(list(map(int, input().split())))  # 入力

    if x < p[0]:  # 最初の値より小さい場合
        print(p[0] - x)
    elif x > p[-1]:  # 最後の値より大きい場合
        print(x - p[-1])
    else:  # 他の場合
        for i in range(n-1):  # ループ処理
            if x < p[i+1]:
                print(min(x-p[i], p[i+1] - x))
                break

if __name__ == '__main__':
    main()
