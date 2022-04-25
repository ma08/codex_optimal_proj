# coding: utf-8


def main():
    n, m = map(int, input().split())
    # 入力されたカード番号のリスト
    card_list = [0] * (n + 1)
    for i in range(m):
        l, r = map(int, input().split())
        for j in range(l, r + 1):
            # カード番号が入力された場合は1にする
            card_list[j] = 1
    print(card_list.count(1))


if __name__ == '__main__':
    main()
