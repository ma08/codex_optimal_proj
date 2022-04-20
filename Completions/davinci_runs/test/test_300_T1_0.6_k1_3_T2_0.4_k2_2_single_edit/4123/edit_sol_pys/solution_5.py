

input_n = int(input())  # 入力される文字列の長さ
input_s = input()  # 文字列

max_count = 0  # 最大出現回数
max_gram = ""  # 最大出現回数の文字列
for i in range(input_n-1):  # iは0からinput_n-2まで
    gram = input_s[i:i+2]  # 2文字ずつ切り出す
    if input_s.count(gram) > max_count:  # gramが出現した回数が最大出現回数より大きい場合
        max_count = input_s.count(gram)  # 最大出現回数を更新
        max_gram = gram  # 最大出現回数の文字列を更新
print(max_gram)  # 最大出現回数の文字列を出力
