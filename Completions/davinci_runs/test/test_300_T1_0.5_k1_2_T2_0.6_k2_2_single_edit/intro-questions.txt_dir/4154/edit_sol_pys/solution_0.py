
def main():
    n, m = map(int, input().split())
    card_list = [0] * (n + 1)  # 入力されたカードの番号のリスト
    for i in range(m):
        l, r = map(int, input().split())
        card_list[l:r + 1] = [1] * (r + 1 - l)
    print(card_list.count(1))


if __name__ == '__main__':
    main()
