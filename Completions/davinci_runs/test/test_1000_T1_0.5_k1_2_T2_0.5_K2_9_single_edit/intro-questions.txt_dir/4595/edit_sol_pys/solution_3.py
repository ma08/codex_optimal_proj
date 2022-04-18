

# -----Answer-----

s = input()

# sから最初にAが出てくる位置を取得し、a_posに格納
a_pos = s.find('A')

# sから最後にZが出てくる位置を取得し、z_posに格納
z_pos = s.rfind('Z')

# AからZまでの長さを計算し、出力
print(z_pos - a_pos + 1)
