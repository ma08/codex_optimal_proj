
n, x = map(int, input().split())  # 入力を読み込み
l_list = list(map(int, input().split()))  # 入力を読み込み
coord_list = [0]  # 座標を格納するリスト
for i in range(n):  # すべての座標を計算する
    coord_list.append(coord_list[i] + l_list[i])  # 座標を計算する
print(len(list(filter(lambda x: x <= x, coord_list))))  # 座標のうちX以下の個数を出力
