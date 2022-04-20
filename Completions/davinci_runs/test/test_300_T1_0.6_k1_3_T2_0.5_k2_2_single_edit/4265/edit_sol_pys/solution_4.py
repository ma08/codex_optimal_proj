# coding: utf-8


n = int(input()) # 文字列の長さ
s = input() # 入力文字列
t = input() # 入力文字列

count = 0 # 不一致文字数
for i in range(n):
	if s[i] != t[i]:
		count += 1

print(count)
