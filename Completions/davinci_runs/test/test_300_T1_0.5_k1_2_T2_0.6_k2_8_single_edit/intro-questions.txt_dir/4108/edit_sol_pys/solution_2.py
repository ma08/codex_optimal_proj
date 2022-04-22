
# -----Answer-----

s = input() # 文字列s
t = input() # 文字列t

# 文字列をソート
s_sorted = sorted(s) # 文字列sをソート
t_sorted = sorted(t) # 文字列tをソート

# 文字列が等しいかどうか判定
if s_sorted == t_sorted:
    print('Yes')
else:
    print('No')
