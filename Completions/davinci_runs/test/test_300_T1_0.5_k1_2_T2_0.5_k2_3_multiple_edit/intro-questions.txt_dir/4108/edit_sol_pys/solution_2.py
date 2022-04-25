
# -----Answer----- 

s = input()
t = input()

# 文字列が等しいかどうか判定(ソートして比較)
if sorted(s) == sorted(t):
    print('Yes')
else:
    print('No')
