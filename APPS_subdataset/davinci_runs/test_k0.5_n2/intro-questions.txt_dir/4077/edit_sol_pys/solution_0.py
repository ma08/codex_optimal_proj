# https://atcoder.jp/contests/abc087/tasks/abc087_b


def main():
    n, a, b = map(int, input().split())
    x = list(map(int, input().split()))

    ans = 0
    for i in range(n-1):
        if x[i+1] - x[i] <= a:
            ans += x[i+1] - x[i]
        else:
            ans += a

    print(ans)


if __name__ == '__main__':
    main()
