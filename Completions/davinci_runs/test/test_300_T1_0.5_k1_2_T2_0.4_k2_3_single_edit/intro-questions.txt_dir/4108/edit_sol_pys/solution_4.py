

# -----Answer-----

s = input()  # 文字列を受け取る
t = input()  # 文字列を受け取る

# 文字列をソートする
s_sorted = sorted(s)  # sをソートする
t_sorted = sorted(t)  # tをソートする

# 文字列が等しいかどうか判定する
if s_sorted == t_sorted:
    print('Yes')  # Yesと出力する
else:
    print('No')  # Noと出力する
