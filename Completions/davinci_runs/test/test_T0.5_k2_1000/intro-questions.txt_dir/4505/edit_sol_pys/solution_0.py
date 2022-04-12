
S = input()  # 文字列の入力
S_list = list(S)  # 文字列をリストに変換
S_list.sort()  # リストをソート

if S_list == ['a', 'b', 'c']:
    print("Yes")
else:
    print("No")
