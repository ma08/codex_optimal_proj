

def main():
    n, b, a = map(int, input().split()) # n = 人数、b = バッテリー、a = 残りの電池
    s = list(map(int, input().split())) # s = 人の位置
    ans = 0
    i = 0
    while i < n:
        if s[i] == 1: # バッテリーが充電できる人がいた場合
            if a < b: # 残りの電池がバッテリーより少ない場合
                a += 1
            else: # 残りの電池がバッテリーより多い場合
                b += 1
        if a > 0: # 残りの電池がある場合
            a -= 1
            ans += 1
        elif b > 0: # バッテリーがある場合
            b -= 1
            ans += 1
        else: # 残りの電池もバッテリーもない場合
            break
        i += 1
    print(ans)

if __name__ == "__main__":
    main()
