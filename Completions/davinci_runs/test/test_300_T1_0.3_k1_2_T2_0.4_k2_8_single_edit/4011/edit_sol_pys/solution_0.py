

def main():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))
    a = list(map(int, a))

    max_num = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(i, j + 1):
                a[k] = f[a[k] - 1]
            max_num = max(max_num, int(''.join(map(str, a))))  # 一括文字列に変換
            for k in range(i, j + 1):
                a[k] = int(a[k])  # 数値に戻す
    print(max_num)


if __name__ == "__main__":
    main()
