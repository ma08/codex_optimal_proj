# https://atcoder.jp/contests/abc151/tasks/abc151_c


def main():
    A, B = map(int, input().split())
    print(B * (A // B + 1))


if __name__ == '__main__':
    main()
