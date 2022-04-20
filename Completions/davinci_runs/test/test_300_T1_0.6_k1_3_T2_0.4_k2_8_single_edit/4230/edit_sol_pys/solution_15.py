
def main():
    x, n = map(int, input().split()) # 入力値を読み込む
    p = sorted(list(map(int, input().split()))) # 入力値を読み込む

    if x < p[0]: # xがpの最小値より小さい場合
        print(p[0] - x)
    elif x > p[-1]: # xがpの最大値より大きい場合
        print(x - p[-1])
    else:
        for i in range(n-1):
            if x < p[i+1]:
                print(min(x-p[i], p[i+1] - x))
                break

if __name__ == '__main__':
    main()
