
def main():
    n, b, a = map(int, input().split())  # n: 入力数, b: 残り電池数, a: 残り充電数
    s = list(map(int, input().split()))  # s: 入力
    ans = 0  # 答え
    i = 0  # 入力インデックス
    while i < n:  # 入力が終わるまで
        if s[i] == 1:  # 入力が1なら
            if a < b:  # 充電数が残り電池数より少ないなら
                a += 1  # 充電数を増やす
            else:  # 充電数が残り電池数より多いなら
                b += 1  # 残り電池数を増やす
        if a > 0:  # 充電数が0より大きいなら
            a -= 1  # 充電数を減らす
            ans += 1  # 答えを増やす
        elif b > 0:  # 残り電池数が0より大きいなら
            b -= 1  # 残り電池数を減らす
            ans += 1  # 答えを増やす
        else:  # どちらも0なら
            break  # 終了
        i += 1  # 入力インデックスを増やす
    print(ans)  # 答えを出力

if __name__ == "__main__":
    main()
