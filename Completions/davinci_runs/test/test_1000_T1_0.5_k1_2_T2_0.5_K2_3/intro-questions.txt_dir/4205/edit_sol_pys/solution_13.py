# 与えられた配列をソートして、
# 順番に比較して、隣り合う数字が違うなら、その数字が何番目にあるかを記録する
# その記憶した数字が2つ以上あるなら、NOを出力する
# そうでなければ、YESを出力する

n = int(input())
p = list(map(int, input().split()))

# 配列をソートする
sorted_p = sorted(p)

# 数字が違う隣り合う数字の位置を記録するための配列
diff_index = []

# 順番に比較して、隣り合う数字が違うなら、その数字が何番目にあるかを記録する
for i in range(n):
    if p[i] != sorted_p[i]:
        diff_index.append(i)

# 記録した数字が2つ以上あるなら、NOを出力する
# そうでなければ、YESを出力する
if len(diff_index) > 2:
    print('NO')
else:
    print('YES')
