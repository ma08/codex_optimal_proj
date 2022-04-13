
# -----Answer-----

s = input()

# sから最初にaが出てくる位置を取得
a_pos = s.find('a')

# sから最後にzが出てくる位置を取得
z_pos = s.rfind('z')

# aからzまでの長さを計算
print(z_pos - a_pos + 1)
