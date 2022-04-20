

def main():
    n, b, a = map(int, input().split())  # 入力
    s = list(map(int, input().split()))  # 入力
    ans = 0
    i = 0
    while i < n:  # 全ての要素について
        if s[i] == 1:  # タイプが1なら
            if a < b:  # aを充電
                a += 1  # aを1増やす
            else:  # aを充電
                b += 1  # bを1増やす
        if a > 0:  # aが0より大きいなら
            a -= 1  # aを1減らす
            ans += 1  # ansを1増やす
        elif b > 0:  # bが0より大きいなら
            b -= 1  # bを1減らす
            ans += 1  # ansを1増やす
        else:  # どちらも0なら
            break  # 終了
        i += 1  # iを1増やす
    print(ans)

if __name__ == "__main__":
    main()
