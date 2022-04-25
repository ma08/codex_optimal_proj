N, M = map(int, input().split())
card_list = [0] * (N + 1)  # 入力されたカードの番号のリスト
for i in range(M):
    l, r = map(int, input().split())
    for j in range(l, r + 1):
        card_list[j] = 1  # カードの番号が入力された場合は1にする
print(card_list.count(1))
