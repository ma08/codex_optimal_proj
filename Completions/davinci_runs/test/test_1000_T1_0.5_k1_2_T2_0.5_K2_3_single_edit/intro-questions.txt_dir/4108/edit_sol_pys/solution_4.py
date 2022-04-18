

# -----Answer-----

s = input()
t = input()
s_sorted = ''.join(sorted(s))
t_sorted = ''.join(sorted(t, reverse=True))
# 文字列が等しいかどうか判定
if s_sorted == t_sorted:
    print('Yes')
else:
    print('No')
