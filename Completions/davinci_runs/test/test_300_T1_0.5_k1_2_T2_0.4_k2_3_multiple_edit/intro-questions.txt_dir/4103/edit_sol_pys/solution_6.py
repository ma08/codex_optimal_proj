

def main():
    n, b, a = map(int, input().split())  # 入力
    s = list(map(int, input().split()))  # 入力
    ans = 0
    i = 0
    while i < n:
        if s[i] == 1 and a < b:  # 充電器が足りない場合
            a += 1
        elif s[i] == 1:
            b += 1
        if a > 0:
            a -= 1
            ans += 1
        elif b > 0:
            b -= 1
            ans += 1
        else:
            break
        i += 1
    print(ans)

if __name__ == "__main__":
    main()
