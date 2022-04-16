
# coding:utf-8
# -----Answer-----

s = input()

# sから最初にAが出てくる位置を取得する
a_pos = s.find('A')

# sから最後にZが出てくる位置を取得する
z_pos = s.rfind('Z')

# AからZまでの長さを計算する
print(z_pos - a_pos + 1)
