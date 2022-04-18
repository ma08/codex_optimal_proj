
# -----Answer-----

s = input()

# sから最初にAが出てくる位置を取得
a_pos = s.find('A')

# sから最後にZが出てくる位置を取得
z_pos = s.rfind('Z')

# AからZまでの長さを計算
print(z_pos - a_pos + 1)
