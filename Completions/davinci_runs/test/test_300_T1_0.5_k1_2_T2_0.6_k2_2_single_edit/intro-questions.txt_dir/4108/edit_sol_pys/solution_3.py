

# -----Answer-----

s = input()  # 文字列の入力
t = input()  # 文字列の入力

# 文字列をソート
s_sorted = sorted(s)  # 文字列をソートしたもの
t_sorted = sorted(t)  # 文字列をソートしたもの

# 文字列が等しいかどうか判定
if s_sorted == t_sorted:
    print("Yes")
else:
    print("No")
