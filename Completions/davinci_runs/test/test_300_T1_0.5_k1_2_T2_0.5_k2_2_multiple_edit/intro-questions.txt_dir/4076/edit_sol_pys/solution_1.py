
# Set up 
s = input()
s = s.split()

# Solve 
# 文字列をリストに格納
word_list = []
for word in s:
    word_list.append(word)

# リストをソート
word_list.sort()

# 出力
for word in word_list:
    print(word)
