

def main():
    n, b, a = map(int, input().split())  # n: 入力数 b: 生産数 a: 加工数
    s = list(map(int, input().split()))  # 入力数
    ans = 0
    i = 0
    while i < n:
        if a < b:  # 加工数が生産数より少ない場合
            a += 1
        else:  # 生産数が加工数より少ない場合
            b += 1
        if a > 0:  # 加工数がある場合
            a -= 1
            ans += 1
        elif b > 0:  # 生産数がある場合
            b -= 1
            ans += 1
        else:
            break
        i += 1
    print(ans)

if __name__ == "__main__":
    main()
