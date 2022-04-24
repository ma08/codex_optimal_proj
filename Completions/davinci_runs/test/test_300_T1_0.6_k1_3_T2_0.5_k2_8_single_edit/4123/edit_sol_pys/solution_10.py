# 解答
# 文字列の最頻値を求める問題
# 文字列の中で最も出現回数が多い2文字のグラムを求める
# 最終的に出現回数が同じ場合は、辞書順が小さい方を出力する
# 入力
#   N文字の文字列S
# 出力
#   最頻値の2文字のグラム


input_n = int(input())
input_s = input()

max_count = 0
max_gram = ""
for i in range(input_n-1):
    gram = input_s[i:i+2]
    if input_s.count(gram) > max_count:
        max_count = input_s.count(gram)
        max_gram = gram
print(max_gram)
