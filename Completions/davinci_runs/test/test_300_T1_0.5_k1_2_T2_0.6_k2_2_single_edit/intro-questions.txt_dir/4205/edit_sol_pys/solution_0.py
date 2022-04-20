

n = int(input())
a = list(map(int, input().split()))

# 与えられた配列をソートして、
# 順番に比較して、隣り合う数字が違うなら、その数字が何番目にあるかを記憶する
# その記憶した数字が2つ以上あるなら、NOを出力する
# そうでなければ、YESを出力する

# 配列をソートする
sorted_a = sorted(a)

# 数字が違う隣り合う数字の位置を記憶するための配列
diff_index = []

# 順番に比較して、隣り合う数字が違うなら、その数字が何番目にあるかを記憶する
for i in range(n):
    if a[i] != sorted_a[i]:
        diff_index.append(i)

# 記憶した数字が2つ以上あるなら、NOを出力する
# そうでなければ、YESを出力する
if len(diff_index) > 2:
    print('NO')
else:
    print('YES')
