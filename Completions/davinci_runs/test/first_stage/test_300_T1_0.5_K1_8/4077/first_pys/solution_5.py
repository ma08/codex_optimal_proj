


def main():
    n, m = map(int, input().split())
    a = [0] + list(map(int, input().split()))

    # 前缀和
    for i in range(1, n + 1):
        a[i] += a[i - 1]

    # 前缀和中是否存在m，存在则记录出现的次数
    tmp = {}
    for i in range(1, n + 1):
        if a[i] - m in tmp:
            tmp[a[i] - m] += 1
        else:
            tmp[a[i] - m] = 1

    # 次数累加
    for i in range(n):
        if a[i] in tmp:
            tmp[a[i]] += 1
        else:
            tmp[a[i]] = 1

    res = 0
    for i in range(1, n + 1):
        if a[i] - m in tmp:
            res += tmp[a[i] - m]

    print(res)


if __name__ == "__main__":
    main()