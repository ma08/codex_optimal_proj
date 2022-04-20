

s = input()

# 入力された文字列を一文字ずつリストに格納する
s_list = list(s)

# 入力された文字列の最大値
max_len = 0

# 入力された文字列の最大値を求めるためのループ
for i in range(len(s_list)):
    # 入力された文字列の最大値を求めるためのカウンターを初期化
    count = 0
    # 入力された文字列の最大値を求めるためのループ
    for j in range(i, len(s_list)):
        # 文字列がACGTのどれかであればカウンターを増やす
        if s_list[j] == "A" or s_list[j] == "C" or s_list[j] == "G" or s_list[j] == "T":
            count += 1
        # 文字列がACGTのどれでもなければループを抜けて次の文字列を調べる
        else:
            break
    # 入力された文字列の最大値を更新
    if max_len < count:
        max_len = count

# 入力された文字列の最大値を出力
print(max_len)
