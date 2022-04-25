

def main():
    n, b, a = map(int, input().split())  # n:個数, b:バッテリー, a:充電器
    s = list(map(int, input().split()))  # s:スイッチ(1:ON, 0:OFF)
    ans = 0
    i = 0
    while i < n:
        if s[i] == 1:
            if a < b:
                a += 1
            else:
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
