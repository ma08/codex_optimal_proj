
def main():
    n = int(input())  # 入力
    h = list(map(int, input().split()))  # 入力
    ans = 0  # 初期化
    while n > 0:  # 繰り返し
        n -= 1  # インクリメント
        if n == 0:  # 条件分岐
            ans += 1  # 処理
            break  # 処理
        if h[n] >= h[n-1]:  # 条件分岐
            ans += 1  # 処理
        else:  # 条件分岐
            break  # 処理
    print(ans)  # 出力

if __name__ == '__main__':
    main()
