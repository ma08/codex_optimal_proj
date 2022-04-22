
def main():
    N, M = map(int, input().split())
    card_list = [0] * (N + 1)  # 入力されたカードの番号のリスト
    for i in range(M):
        L, R = map(int, input().split())
        for j in range(L, R + 1):
            card_list[j] = 1  # カードの番号が入力された場合は1にする
    print(sum(card_list))


if __name__ == '__main__':
    main()
