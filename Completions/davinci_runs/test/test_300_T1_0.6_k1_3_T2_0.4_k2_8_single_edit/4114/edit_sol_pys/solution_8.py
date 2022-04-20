
n = int(input())

coord_dict = {}
for i in range(n):
    x, y, h = map(int, input().split())  # 座標と高さを取得
    coord_dict[(x, y)] = h  # 辞書に追加

for x in range(101):  # 0から100までのX座標を試す
    for y in range(101):  # 0から100までのY座標を試す
        h = -1  # 最初は-1
        for (x_, y_), h_ in coord_dict.items():  # 辞書から座標と高さを取り出す
            if h == -1:  # 最初のループの時は高さを設定
                h = h_ + abs(x - x_) + abs(y - y_)  # 高さを設定
            elif h != h_ + abs(x - x_) + abs(y - y_):  # 高さが一致しない時は次のループに進む
                break  # 次のループに進む
        else:  # 全てのループが終了した時
            print(x, y, h)  # 答えを出力
            exit()  # 終了
