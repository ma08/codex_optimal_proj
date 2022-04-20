

def main():
    n = int(input())  # n個の数字を入力
    a = list(map(int, input().split()))  # n個の数字を入力
    ans = 1  # 初期値を1にする
    cur = a[0]  # curをa[0]にする
    for i in range(1, n):  # 1からn-1まで繰り返す
        if a[i] <= cur * 2:  # a[i]がcur*2以下なら
            ans += 1  # ansに1を足す
        else:  # そうでなければ
            cur = a[i]  # curをa[i]にする
    print(ans)  # ansを出力

if __name__ == "__main__":
    main()
