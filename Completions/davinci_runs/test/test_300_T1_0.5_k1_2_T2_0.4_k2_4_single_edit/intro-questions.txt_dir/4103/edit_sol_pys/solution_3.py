

def main():
    n, b, a = map(int, input().split())
    s = list(map(int, input().split()))  # 充電ステーションのリスト
    ans = 0
    i = 0
    while i < n:
        if s[i] == 1:  # 充電ステーションがある場合
            if a < b:  # aの方が空いている場合
                a += 1  # aを充電
            else:  # bの方が空いている場合
                b += 1  # bを充電
        if a > 0:
            a -= 1  # aを使用
            ans += 1
        elif b > 0:
            b -= 1  # bを使用
            ans += 1
        else:
            break  # aもbも残りがない場合
        i += 1
    print(ans)

if __name__ == "__main__":
    main()
