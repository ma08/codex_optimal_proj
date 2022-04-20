

def main():
    x, n = map(int, input().split()) # x: 基準値, n: プライマリーの数
    p = sorted(list(map(int, input().split()))) # p: プライマリー

    if x < p[0]:
        print(p[0] - x)
    elif x > p[-1]:
        print(x - p[-1])
    else:
        for i in range(n-1): # n-1 回ループ
            if x < p[i+1]: # 基準値と比較
                print(min(x-p[i], p[i+1] - x)) # 左右の距離を比較して小さい方を出力
                break

if __name__ == '__main__':
    main()
