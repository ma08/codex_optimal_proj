

n = int(input())  # 標準入力から整数を取得
d_list = []  # d_listという空のリストを作成
for i in range(n):  # n回繰り返す
    d_list.append(int(input()))  # d_listに標準入力から整数を追加
d_set = set(d_list)  # d_listをsetに変換
print(len(d_set))  # d_setの長さを出力
