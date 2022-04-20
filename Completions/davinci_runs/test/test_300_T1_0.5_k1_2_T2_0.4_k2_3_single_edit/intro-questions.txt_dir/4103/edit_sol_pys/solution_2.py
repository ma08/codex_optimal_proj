
def main():
    n, b, a = map(int, input().split()) #n人目まで調べる、b個のバッテリー、a個のバッテリーがある
    s = list(map(int, input().split())) #s[i]はi人目が炭酸かどうか
    ans = 0 #答え
    i = 0 #現在調べている人
    while i < n:
        if s[i] == 1: #炭酸なら
            if a < b: #aの方が少ないなら
                a += 1
            else: #bの方が少ないなら
                b += 1
        if a > 0: #aがあるなら
            a -= 1
            ans += 1
        elif b > 0: #bがあるなら
            b -= 1
            ans += 1
        else: #ないなら
            break
        i += 1 #次の人
    print(ans)

if __name__ == "__main__":
    main()
