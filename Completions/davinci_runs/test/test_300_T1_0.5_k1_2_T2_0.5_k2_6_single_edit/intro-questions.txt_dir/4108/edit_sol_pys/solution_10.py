

# -----Answer-----

s = input()
t = input()

# 文字列をソート(昇順)
s_sorted = sorted(s, reverse=False)
t_sorted = sorted(t, reverse=False)

# 文字列が等しいかどうか判定
if s_sorted == t_sorted:
    print('Yes')
else:
    print('No')
