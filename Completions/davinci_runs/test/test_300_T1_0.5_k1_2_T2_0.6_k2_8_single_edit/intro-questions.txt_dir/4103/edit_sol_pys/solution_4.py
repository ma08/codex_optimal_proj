

def main():
    n, b, a = map(int, input().split())
    s = list(map(int, input().split()))  # s[i] = 1:電池が減る, s[i] = 0:電池が減らない
    ans = 0
    i = 0
    while i < n:  # 全てのスイッチをONにする
        if s[i] == 1:
            if a < b:
                a += 1
            else:
                b += 1
        if a > 0:  # 電池を使う
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
