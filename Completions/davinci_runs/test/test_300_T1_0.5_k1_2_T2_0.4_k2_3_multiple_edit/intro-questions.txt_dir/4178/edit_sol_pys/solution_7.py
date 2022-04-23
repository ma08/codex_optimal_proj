# https://atcoder.jp/contests/abc166/tasks/abc166_c


def main():
    n = int(input())
    m = int(input())
    h = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(m)]

    ans = [0] * n

    for i in range(m):
        a = ab[i][0] - 1
        b = ab[i][1] - 1

        if h[a] > h[b]:
            ans[b] = 1
        elif h[a] < h[b]:
            ans[a] = 1
        else:
            ans[a] = 1
            ans[b] = 1

    print(ans.count(0))


if __name__ == '__main__':
    main()
