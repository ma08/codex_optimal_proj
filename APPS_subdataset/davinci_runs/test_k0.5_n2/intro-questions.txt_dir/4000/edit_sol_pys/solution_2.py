def main():
    # 入力
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # 計算

    ans = 0
    for i in range(n):
        if a[i] > b[i]:
            ans += b[i]
            a[i] -= b[i]
            b[i] = 0
        else:
            ans += a[i]
            b[i] -= a[i]
            a[i] = 0
        if a[i] > 0:
            ans += a[i]
            b[i + 1] -= a[i]
            a[i] = 0
        if b[i] > 0:
            ans += b[i]
            a[i + 1] -= b[i]
            b[i] = 0
    print(ans)
    # 出力


if __name__ == '__main__':
    main()
