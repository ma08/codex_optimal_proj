

def main():
    x, n = map(int, input().split())  # x: 目的地, n: ピラミッドの数
    p = sorted(list(map(int, input().split())))

    if x < p[0]:  # ピラミッドの最も小さい数より小さい場合
        print(p[0] - x)  # ピラミッドの最も小さい数との差を出力
    elif x > p[-1]:  # ピラミッドの最も大きい数より大きい場合
        print(x - p[-1])  # ピラミッドの最も大きい数との差を出力
    else:
        for i in range(n-1):
            if p[i] < x < p[i+1]:  # ピラミッドの最も小さい数より大きいかつ最も大きい数より小さい場合
                print(min(x-p[i], p[i+1] - x))  # 距離の小さい方を出力
                break

if __name__ == '__main__':
    main()
