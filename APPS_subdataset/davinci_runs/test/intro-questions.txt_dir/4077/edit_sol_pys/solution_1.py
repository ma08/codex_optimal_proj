# https://atcoder.jp/contests/abc087/tasks/abc087_b


def main():
    n, m = map(int, input().split())  # n: 500, m: 1000
    a = list(map(int, input().split()))  # a: 500

    cnt = 0
    for i in range(n):
        for j in range(i, n):
            if a[(i+j)//2] == m:
                cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
