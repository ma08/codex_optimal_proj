# https://codeforces.com/problemset/problem/913/A


def main():
    n, m = map(int, input().split())
    if m < n:
        print(m)
    elif m >= n:
        if m % 2 == 0:
            print(n + (m - n) // 2)
        else:
            print(n + (m - n) // 2 + 1)


if __name__ == '__main__':
    main()
