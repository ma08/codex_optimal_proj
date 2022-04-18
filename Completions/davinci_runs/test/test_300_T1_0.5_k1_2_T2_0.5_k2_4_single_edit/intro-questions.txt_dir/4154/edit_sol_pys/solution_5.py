#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#



#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


def main():
    n, m = map(int, input().split())
    card_list = [0] * (n + 1)  # 入力されたカードの番号のリスト
    for i in range(m):
        l, r = map(int, input().split())
        for j in range(l, r + 1):
            card_list[j] = 1  # カードの番号が入力された場合は1にする
    print(card_list.count(1))


if __name__ == '__main__':
    main()
