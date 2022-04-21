
# https://atcoder.jp/contests/abc015/tasks/abc015_4


def main():
    n = int(input())
    w = int(input())
    a = [0] * w
    for i in range(n):
        a[i] = int(input())
    ans = 0
    for i in range(1 << n):
        s = 0
        for j in range(n):
            if (i >> j) & 1:
                s += a[j]
        if s == w:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
