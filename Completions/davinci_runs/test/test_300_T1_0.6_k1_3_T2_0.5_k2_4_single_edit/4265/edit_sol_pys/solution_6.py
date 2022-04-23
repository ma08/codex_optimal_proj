

# 問題文
# 高橋君は、文字列 S と文字列 T を持っています。
# 高橋君は、文字列 S と文字列 T を 1 文字ずつ置き換えることで、文字列 S が文字列 T になるようにしたいです。
# 高橋君が目指すことができるか判定してください。

# 制約
# 1≤|S|,|T|≤100
# S,T は英小文字からなる

# 入力
# 入力は以下の形式で標準入力から与えられる。
# S
# T

# 出力
# 高橋君が目指すことができるなら Yes を、できないなら No を出力せよ。

# 入力例1
# xy
# yx

# 出力例1
# Yes

# 入力例2
# abc
# abc

# 出力例2
# No

# 入力例3
# aa
# aa

# 出力例3
# Yes

# 入力例4
# ab
# ba

# 出力例4
# Yes

# 入力例5
# a
# b

# 出力例5
# No

# 入力例6
# a
# a

# 出力例6
# Yes

# 入力例7
# aa
# bb

# 出力例7
# No

# 入力例8
# abc
# def

# 出力例8
# No

# 入力例9
# aa
# ab

# 出力例9
# No

# 入力例10
# ab
# ab

# 出力例10
# Yes

# 入力例11
# aa
# ab

# 出力例11
# No

# 入力例12
# ab
# ab

# 出力例12
# Yes

n = int(input())
s = input()
t = input()

# count = 0
# for i in range(n):
# 	if s[i] != t[i]:
# 		count += 1

# print(count)

# print(s)
# print(t)

# print(s[0])
# print(t[0])

# print(s[0] != t[0])
# print(s[1] != t[1])
# print(s[2] != t[2])

# print(s[0] != t[0] and s[1] != t[1] and s[2] != t[2])

# print(s == t)

# print(s != t)

# print(s[0] == t[0])
# print(s[1] == t[1])
# print(s[2] == t[2])

# print(s[0] == t[0] or s[1] == t[1] or s[2] == t[2])

# print(s[0] == t[0] or s[1] == t[1] or s[2] == t[2] or s[0] != t[0] or s[1] != t[1] or s[2] != t[2])

# print(s[0] == t[0] or s[1] == t[1] or s[2] == t[2] or s[0] != t[0] or s[1] != t[1] or s[2] != t[2] or s[0] == t[0] and s[1] == t[1] and s[2] == t[2])

# print(s[0] == t[0] or s[1] == t[1] or s[2] == t[2] or s[0] != t[0] or s[1] != t[1] or s[2] != t[2] or s[0] == t[0] and s[1] == t[1] and s[2] == t[2] or s[0] != t[0] and s[1] != t[1] and s[2] != t[2])

# print(s[0] == t[0] or s[1] == t[1] or s[2] == t[2] or s[0] != t[0] or s[1] != t[1] or s[2] != t[2] or s[0] == t[0] and s[1] == t[1] and s[2] == t[2] or s[0] != t[0] and s[1] != t[1] and s[2] != t[2] or s[0] == t[0] or s[1] == t[1] or s[2] == t[2] or s[0] != t[0] or s[1] != t[1] or s[2] != t[2] or s[0] == t[0] and s[1] == t[1] and s[2] == t[2] or s[0] != t[0] and s[1] != t[1] and s[2] != t[2])

# print(s[0] == t[0] or s[1] == t[1] or s[2] == t[2] or s[0] != t[0] or s[1] != t[1] or s[2] != t[2] or s[0] == t[0] and s[1] == t[1] and s[2] == t[2] or s[0] != t[0] and s[1] != t[1] and s[2] != t[2] or s[0] == t[0] or s[1] == t[1] or s[2] == t[2] or s[0] != t[0] or s[1] != t[1] or s[2] != t[2] or s[0] == t[0] and s[1] == t[1] and s[2] == t[2] or s[0] != t[0] and s[1] != t[1] and s[2] != t[2] or s[0] == t[0] or s[1] == t[1] or s[2] == t[2] or s[0] != t[0] or s[1] != t[1] or s[2] != t[2] or s[0] == t[0] and s[1] == t[1] and s[2] == t[2] or s[0] != t[0] and s[1] != t[1] and s[2] != t[2])
