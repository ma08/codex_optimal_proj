# https://atcoder.jp/contests/abc085/tasks/abc085_b


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split().split()))

    ans = 0
    for i in range(n):
        if a[i] >= k:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
