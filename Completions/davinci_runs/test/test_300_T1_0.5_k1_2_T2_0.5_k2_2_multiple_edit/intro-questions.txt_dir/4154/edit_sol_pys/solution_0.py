# https://atcoder.jp/contests/abc095/tasks/arc096_a


def main():
    n, m = map(int, input().split())
    card_list = [0] * (n + 1)
    for i in range(m):
        l, r = map(int, input().split())
        for j in range(l, r + 1):
            card_list[j] = 1
    print(card_list.count(1))


if __name__ == '__main__':
    main()
