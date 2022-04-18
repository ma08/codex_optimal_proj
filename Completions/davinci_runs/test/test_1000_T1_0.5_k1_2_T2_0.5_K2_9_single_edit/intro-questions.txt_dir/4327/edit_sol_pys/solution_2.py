# https://atcoder.jp/contests/abc139/tasks/abc139_a


def main():
    a, p = map(int, input().split())
    print(p // 2 + (a + p % 2) * 3 // 2)


if __name__ == '__main__':
    main()
