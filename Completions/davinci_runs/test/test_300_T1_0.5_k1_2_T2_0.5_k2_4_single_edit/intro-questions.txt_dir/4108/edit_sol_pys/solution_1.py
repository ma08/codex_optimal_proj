

# -----Answer-----

s = input()
t = input()

# 文字列をソート
s_sorted = sorted(s)
t_sorted = sorted(t, reverse=True)

# 文字列が等しいかどうか判定
if s_sorted == t_sorted:
    print('Yes')
else:
    print('No')
