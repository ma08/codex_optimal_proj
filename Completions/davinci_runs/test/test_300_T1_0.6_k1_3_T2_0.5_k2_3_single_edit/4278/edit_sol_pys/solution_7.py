# https://atcoder.jp/contests/abc126/tasks/abc126_c


def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        tmp = 1
        while i < k:
            i *= 2
            tmp /= 2
        ans += tmp / n
    print(ans)


if __name__ == "__main__":
    main()
