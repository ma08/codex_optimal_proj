# https://atcoder.jp/contests/abc071/tasks/arc081_a


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort()
    b.sort()
    c.sort()
    a_i = 0
    b_i = 0
    c_i = 0
    ans = 0
    while b_i < m:
        if a[a_i] <= b[b_i] <= c[c_i]:
            ans += 1
            a_i += 1
            b_i += 1
            c_i += 1
        elif b[b_i] < a[a_i]:
            b_i += 1
        elif c[c_i] < b[b_i]:
            c_i += 1
    print(ans)


if __name__ == '__main__':
    main()
