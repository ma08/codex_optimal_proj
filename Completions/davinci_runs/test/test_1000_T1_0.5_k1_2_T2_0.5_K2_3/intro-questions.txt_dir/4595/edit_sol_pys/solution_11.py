
# -----Answer-----

s = input()

# sから最初に A が出てくる位置を取得
a_pos = s.find('A')

# sから最後に Z が出てくる位置を取得
z_pos = s.rfind('Z')

# A から Z までの長さを計算
print(z_pos - a_pos + 1)
