

def main():
    n, b, a = map(int, input().split())  # n = バッテリーの数, b = バッテリーの残り, a = アンプの残り
    s = list(map(int, input().split()))  # s = バッテリーの負荷
    ans = 0
    i = 0
    while i < n:
        if s[i] == 1:  # 負荷が1である場合
            if a < b:
                a += 1  # アンプを使用する
            else:
                b += 1  # バッテリーを使用する
        if a > 0:  # アンプがある場合
            a -= 1
            ans += 1
        elif b > 0:  # バッテリーがある場合
            b -= 1
            ans += 1
        else:
            break
        i += 1
    print(ans)

if __name__ == "__main__":
    main()
