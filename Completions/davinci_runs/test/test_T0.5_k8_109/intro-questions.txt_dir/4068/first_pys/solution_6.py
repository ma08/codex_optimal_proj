


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    # 階段にaが含まれない場合
    if m == 0:
        print(fib(n))
        return

    # 階段にaが含まれる場合
    # a[i]を除いた階段の数
    b = [0] * m
    # a[i]を除いた階段の数のフィボナッチ数
    c = [0] * m
    for i in range(m):
        if a[i] == 1:
            b[i] = a[i] - 1
        else:
            b[i] = a[i] - a[i - 1] - 1
        c[i] = fib(b[i])

    # 到達できる階段の数
    ans = 0
    for i in range(m):
        # a[i]を除いた階段の数のフィボナッチ数
        ans += c[i]
        # a[i]の一つ前のステップを除いた階段の数のフィボナッチ数
        if i > 0:
            ans += c[i - 1]
    print(ans % 1000000007)


def fib(n):
    if n <= 1:
        return 1
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    main()