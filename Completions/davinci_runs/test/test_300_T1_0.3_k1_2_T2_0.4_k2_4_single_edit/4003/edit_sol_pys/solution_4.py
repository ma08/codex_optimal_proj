

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    b[0] = 1  # 要素数1
    for i in range(1, n):
        if a[i] > a[i - 1]:
            b[i] = b[i - 1] + 1
        else:
            b[i] = 1
    c = [0] * n
    c[n - 1] = 1  # 要素数1
    for i in range(n - 2, -1, -1):
        if a[i] < a[i + 1]:
            c[i] = c[i + 1] + 1
        else:
            c[i] = 1
    ans = 0  # 初期化
    for i in range(n):
        if b[i] + c[i] - 1 > ans:  # 合計が最大のものを探す
            ans = b[i] + c[i] - 1
    print(ans)  # 出力
    s = ""
    i = 0  # 初期化
    while i < n:
        if b[i] >= c[i]:  # 左に進む
            s += "L"
            i += b[i]
        else:  # 右に進む
            s += "R"
            i += c[i]
    print(s)  # 出力


if __name__ == "__main__":
    main()
