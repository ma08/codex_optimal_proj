
# -----Answer-----

s = input()
t = input()

# 文字列をソートする。
s_sorted = sorted(s)
t_sorted = sorted(t)

# 文字列が等しいかどうか判定する。
if s_sorted == t_sorted:
    print('Yes')
else:
    print('No')
